const ReactCrop = ReactCrop.Component;
const Form = ReactBootstrap.Form;
const Modal = ReactBootstrap.Modal;
const Button = ReactBootstrap.Button;
const InputGroup = ReactBootstrap.InputGroup;
const Col = ReactBootstrap.Col;
const Row = ReactBootstrap.Row;
const Container = ReactBootstrap.Container;
const ButtonGroup = ReactBootstrap.ButtonGroup;
const FormCheck = ReactBootstrap.FormCheck;
const Alert = ReactBootstrap.Alert;

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


const dim_measurement = {
	Meter : 'm',
	Centimeter : 'cm',
	Inches: 'inches'
}

const styles = {
	abstract:'Abstract',
	contemporary:'Contemporary',
	figurative:'Figurative',
	minimalist:'Minimalist',
	portraiture:'Portraiture',
	landscape:'Landscape', 
	fashion:'Fashion',
	popart:'Pop Art',
	other : 'Other'	
}


const material = {
	canvas : 'Canvas',
	paper : 'Paper',
	wood : 'Wood',
	cardboard : 'Cardboard',
	soft : 'Soft (Yam, Cotton, Fabric)',
	plastic : 'Plastic',
	aluminum: 'Aluminum',
	glass : 'Glass',
	carbonfibre: 'Carbon Fibre',
	steel : 'Steel',
	iron : 'Iron',
	bronze : 'Bronze',
	ceramic : 'Ceramic',
	stone : 'Stone',
	stainlesssteel : 'Stainless Steel',
	marble : 'Marble',
	other : 'Other',

}


const category = {
	paintings : 'Paintings',
	prints : 'Prints',
	drawingIllustration : 'Drawing & Illustration',
	photography : 'Photography',
	sculptures : 'Sculptures',
	ceramicPottery : 'Ceramic & Pottery',
	glass : 'Glass',
	
}


const pallettes = [
  ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
  ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
  ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
  ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
  ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
  ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
  ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
  ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
]

class Helpers {
  static contains(orig, filter) {
    let res = filter.map(item => {
      return orig.includes(item);
    });
    return !res.includes(false);
  }
  
  static hasDuplicates(array) {
    return (new Set(array)).size !== array.length
  }
}

const Tag = ({name, index, onDelete, hashtag, hashtagStyle}) => {
  return (
    <li key={index}>
      {hashtag && (
        <span style={{color: '#898989', fontWeight: 'bold', ...hashtagStyled}}># </span>
      )}
      {name} 
      <button type="button" id="tag-d-btn" onClick={e => onDelete(index, e)}>x</button>
    </li>
  );
}

const TagsList = ({tags, onTagDelete, hashtag}) => {
  let list = tags.map((tag, index) => (
    <Tag 
      name={tag} 
      onDelete={onTagDelete} 
      index={index} 
      hashtag={hashtag} />
  ));
  return (
    <ul name="tagsList" className="tagsList">
      {list}
    </ul>
  )
}


class TagInput extends React.Component {
  constructor(props) {
    super(props);
  
    this.state = {
      inputValue: '',
      tags: this.props.tags || []
    }
  }
  
  handleNewTag = (tags) => {
    if (this.props.onNewTag) this.props.onNewTag(tags);
    if (this.props.onTagChange) this.props.onTagChange(tags);
  }

  handleInputChange = ({target: { value: inputValue }}) => {
    inputValue = inputValue == ',' ? '' : inputValue;
    this.setState({inputValue});
  }
  
  handleKeyDown = (e) => {
    let { keyCode, target: {value} } = e;
    let { tags } = this.state; 
    switch (keyCode) {
      case 9:
        if (value) e.preventDefault();
      case 13:
        e.preventDefault();
      case 188:
        value = value.trim();
        if (value && this.notDuplicate(tags, value)) {
          this.addTag(value);
        } else {
          this.setState({inputValue: ''})
        }
        break;
      case 8:
        if (!value) {
          this.handleTagDelete(tags.length - 1);
        } 
        break;
    }
  }
  
  handleTagDelete = (index, e) => {
    this.deleteTag(index, () => { 
      this.props.onTagChange(this.state.tags);
    });
  }
  
  deleteTag = (index, callback) => {
    let tags = this.state.tags.slice();
    
    tags.splice(index, 1);
    this.setState({ tags }, () => {
      if (callback) callback();
    });
  }
  
  notDuplicate = (tags, newTag) => {
    return (!tags.includes(newTag) || this.props.allowDuplicates);
  }
  
  addTag = (tag) => {
    if (this.notDuplicate(this.state.tags, tag)) {
      this.setState({tags: [...this.state.tags, tag], inputValue: ''}, () => {
        this.handleNewTag(this.state.tags);
      });
    }
  }

  
  render() {
    return (
      <span className="tagInputWrapper">
        <TagsList 
          tags={this.state.tags} 
          onTagDelete={this.handleTagDelete} 
          hashtag={this.props.hashtag}
        />
        <input 
          name="tagInput" 
          className="tagInput" 
          placeholder="Enter tags..." 
          value={this.state.inputValue} 
          onChange={this.handleInputChange}
          onKeyDown={this.handleKeyDown}
        />
      </span>
    );
  }
}

class ArtUploadForm extends React.Component {
  state = {
    src: null,
    crop: {
      unit: '%',
      width: 20,
      height: 20
    },
    img_blob: null,
    showModal: false,
    addImgOne: null,
    addImgTwo: null,
    addImgThree: null,
    addImgFour: null,
    imgOne: null,
    imgTwo: null,
    imgThree: null,
    imgFour: null,
    colorOne: "",
    colorTwo: "",
    colorThree: "",
    colorFour: "",
    colorFive: "",
    title: "",
    description: "",
    category: "",
    subcategory: "",
    styles: [],
    materials: [],
    signed: "",
    framed: "",
    height: "",
    width: "",
    depth: "",
    unitOfMeasurement: "",
    tags: [],
    price: null,
    shipUs: null,
    shipCan: null,
    shipUk: null,
    shipEurope: null,
    shipAunz: null,
    shipAsia: null,
    shipOther: null,
    show_price_can: true,
    show_price_us: true,
    show_price_uk: true,
    show_price_aunz: true,
    show_price_asia: true,
    show_price_europe: true,
    show_price_other: true, 
    palletteOne: false,
    palletteTwo: false,
    palletteThree: false,
    palletteFour: false,
    palletteFive: false,
    tagsTooltip: false,
    descriptionTooltip: false,
    tooBig: false,
    imgError: false,
    colorError: false,
    materialsError: false,
    stylesError: false,
    errorMsg: null,
  };

  toggleSwitch = (event) => {
    const shippingToggle =  event.target.name
    this.setState({[event.target.name]: !this.state[shippingToggle]});
  }

  setColor = (event) => {
    this.setState({[event.target.name]: event.target.value});
  }

  showPallette = (event) => {
    this.setState({[event.target.name]: true})
  }

  hidePallette = (event) => {
    this.setState({[event.target.name]: false})
  }

  resetColor = (event) => {
    this.setState({[event.target.name]: ""})
  }

  handleChange = (event) => {
    this.setState({[event.target.name] : event.target.value})
    if (event.target.name == "category") {
      axios({
        method: 'post',
        url: '/get-sub-category',
        timeout: 4000,  
        data: {
          category: event.target.value
        }
      })
      .then(response => {
        var subcats = response.data.data
        this.setState({subcategories : subcats})
      })
      .catch(error => console.error('timeout exceeded'))


    }
  }

  handleStyleSelect = (event) => {
    if (event.target.checked) {
      this.setState({[event.target.name] : [...this.state.styles, event.target.value]})
    } else {
      var index = this.state.styles.indexOf(event.target.value)
      if (index > -1 ) {
        this.state.styles.splice(index, 1);
        this.setState({[event.target.name] : this.state.styles})
      }
    }
  }

  handleMaterialSelect = (event) => {
    if (event.target.checked) {
      this.setState({[event.target.name] : [...this.state.materials, event.target.value]})
    } else {
      var index = this.state.materials.indexOf(event.target.value)
      if (index > -1 ) {
        this.state.materials.splice(index, 1);
        this.setState({[event.target.name] : this.state.materials})
      }
    }
  }


  handleClose = () => {
    this.setState({showModal: false});
  }

  handleShow = () => {
    this.setState({showModal: true});
  }





  onSelectFile = e => {
    if (e.target.files[0].size > 15000000) {
      this.setState({tooBig: true});
    } else if (e.target.files && e.target.files.length > 0) {
      this.setState({tooBig: false});
      const reader = new FileReader();
      reader.addEventListener('load', () =>
        this.setState({ src: reader.result })
        );
        reader.readAsDataURL(e.target.files[0]);
        this.handleShow()
    }
  };

  onImageLoaded = image => {
    this.imageRef = image;
  };

  onCropComplete = crop => {
    this.makeClientCrop(crop);
  };

  onCropChange = (crop, percentCrop) => {
    // You could also use percentCrop:
    // this.setState({ crop: percentCrop });
    this.setState({ crop });
  };


  makeClientCrop(crop) {
    if (this.imageRef && crop.width && crop.height) {
      this.getCroppedImg(
        this.imageRef,
        crop,
        'newFile.png'
      ).then((croppedImageUrl) => {
        this.setState({ croppedImageUrl });
      })
    }
  }

  getCroppedImg(image, crop, fileName) {
    const canvas = document.createElement('canvas');
    const scaleX = image.naturalWidth / image.width;
    const scaleY = image.naturalHeight / image.height;
    canvas.width = Math.ceil(crop.width*scaleX);
    canvas.height = Math.ceil(crop.height*scaleY);
    const ctx = canvas.getContext('2d');

    ctx.drawImage(
      image,
      crop.x * scaleX,
      crop.y * scaleY,
      crop.width * scaleX,
      crop.height * scaleY,
      0,
      0,
      crop.width * scaleX,
      crop.height * scaleY,
    );

    return new Promise((resolve, reject) => {
      canvas.toBlob(blob => {
        if (!blob) {
          //reject(new Error('Canvas is empty'));
          console.error('Canvas is empty');
          return;
        }
        blob.name = fileName;
        var reader = new FileReader();        
        reader.readAsDataURL(blob);        
        reader.onload = (event) => {  
            this.setState({img_blob: reader.result});
        }

        
        window.URL.revokeObjectURL(this.fileUrl);
        this.fileUrl = window.URL.createObjectURL(blob);
        resolve(this.fileUrl);
      }, 'image/png', 1);
    });
  }


  // Keep this method for when we can implement BLOB
  // onSelectAdditionalImg = (event) => {
  //   if (event.target.id == 'pic1') {
  //     URL.revokeObjectURL(event.target.files[0]);
  //     this.setState({addImgOne: URL.createObjectURL(event.target.files[0])});
  //   } else if (event.target.id == "pic2") {
  //     URL.revokeObjectURL(event.target.files[0]);
  //     this.setState({addImgTwo: URL.createObjectURL(event.target.files[0])});
  //   } else if (event.target.id == "pic3") {
  //     URL.revokeObjectURL(event.target.files[0]);
  //     this.setState({addImgThree: URL.createObjectURL(event.target.files[0])});
  //   } else if (event.target.id == "pic4") {
  //     URL.revokeObjectURL(event.target.files[0]);
  //     this.setState({addImgFour: URL.createObjectURL(event.target.files[0])});
  //   }
  // }

  readFile(file, imgNum) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = (event) => {
        this.setState({[imgNum]: reader.result});
        resolve(reader.result);
      }
      reader.onerror = error => reject(error);
    })
  }

  // This method is for getting client pic and base64 now
  onSelectAdditionalImg = (event) => {
    if (event.target.files[0].size > 15000000) {
      this.setState({tooBig: true});
    } else if (event.target.id == 'pic1') {
      this.setState({tooBig: false});
      URL.revokeObjectURL(event.target.files[0]);
      this.setState({addImgOne: URL.createObjectURL(event.target.files[0])});
      this.readFile(event.target.files[0], "imgOne");
    } else if (event.target.id == "pic2") {
      this.setState({tooBig: false});
      URL.revokeObjectURL(event.target.files[0]);
      this.setState({addImgTwo: URL.createObjectURL(event.target.files[0])});
      this.readFile(event.target.files[0], "imgTwo");
    } else if (event.target.id == "pic3") {
      this.setState({tooBig: false});
      URL.revokeObjectURL(event.target.files[0]);
      this.setState({addImgThree: URL.createObjectURL(event.target.files[0])});
      this.readFile(event.target.files[0], "imgThree");
    } else if (event.target.id == "pic4") {
      this.setState({tooBig: false});
      URL.revokeObjectURL(event.target.files[0]);
      this.setState({addImgFour: URL.createObjectURL(event.target.files[0])});
      this.readFile(event.target.files[0], "imgFour");
    }
  }



  validateCheckbox = () => {
    const materials = this.state.materials;
    const isChecked = materials.some(material => material.checked == true);

    if(isChecked) {
      return true
    }
  }

  validate = () => {
    if (this.state.img_blob) {
      this.setState({imgError: false})
    } if (this.state.colorOne || this.state.colorTwo || this.state.colorThree || this.state.colorFour || this.state.colorFive) {
      this.setState({colorError: false})
    } else {
      this.setState({colorError: true})
    } if (this.state.materials.length > 0) {
      this.setState({materialsError: false})
    } if (this.state.styles.length > 0) {
      this.setState({stylesError: false})
    } 
    if (!this.state.img_blob) {
      this.setState({imgError: true})
    }  if (this.state.materials.length < 1) {
      this.setState({materialsError: true})
    } if (this.state.styles.length < 1) {
      this.setState({stylesError: true})
    } if (!this.state.show_price_asia && !this.state.show_price_aunz && !this.state.show_price_can && !this.state.show_price_europe && !this.state.show_price_uk && !this.state.show_price_us && !this.state.show_price_other) {
      this.setState({shippingError: "Please enter atleast one shipping price"})
    } else {
      this.setState({shippingError: null})
    }    
    if (!this.state.shippingError && this.state.img_blob && this.state.materials.length > 0 && this.state.styles.length > 0 && (this.state.colorOne || this.state.colorTwo || this.state.colorThree || this.state.colorFour || this.state.colorFive)) {
        return true;
    } else {
        this.setState({errorMsg: "Please fill in missing fields"});
        return false;
      }
    }

  handleSubmit = (event) => {
    event.preventDefault();
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      this.setState({errorMsg: "Please fill in missing fields"});
    }
    if (this.validate() === true) {
      if (form.checkValidity() === true) {
            $("#preloader-active").css("display", "block");
            axios.post('/art/add-art', {
                art_img: this.state.img_blob,
                additional_img_1: this.state.imgOne,
                additional_img_2: this.state.imgTwo,
                additional_img_3: this.state.imgThree,
                additional_img_4: this.state.imgFour,
                color: this.state.colorOne,
                color_1: this.state.colorTwo,
                color_2: this.state.colorThree,
                color_3: this.state.colorFour,
                color_4: this.state.colorFive,
                title: this.state.title,
                desc: this.state.description,
                tags: this.state.tags,
                height: this.state.height,
                width: this.state.width,
                depth: this.state.depth,
                cat: this.state.category,
                subcat: this.state.subcategory,
                measure: this.state.unitOfMeasurement,
                price: this.state.price,
                s_price_can: this.state.shipCan,
                s_price_us: this.state.shipUs,
                s_price_uk: this.state.shipUk,
                s_price_aunz: this.state.shipAunz,
                s_price_asia: this.state.shipAsia,
                s_price_europe: this.state.shipEurope,
                s_price_other: this.state.shipOther,
                show_price_can: this.state.show_price_can,
                show_price_us: this.state.show_price_us,
                show_price_uk: this.state.show_price_uk, 
                show_price_aunz: this.state.show_price_aunz,
                show_price_asia: this.state.show_price_asia,
                show_price_europe: this.state.show_price_europe,
                show_price_other: this.state.show_price_other,
                styles: this.state.styles,
                materials: this.state.materials,
                is_signed: this.state.signed,
                is_framed_ready: this.state.framed
              })
              .then(response => {
                if (response.data.status === "success") {
                  window.location.replace("product_view/"+response.data.product_id);
                } else {
                  $("#preloader-active").css("display", "none");
                  this.setState({errorMsg: response.data.status + ":" + response.data.message});
                }
              })
              .catch(error => {
                $("#preloader-active").css("display", "none");
                if (error.response) {
                  this.setState({errorMsg: error.response.data.status + " " + error.response.status + ":" + error.response.data.message});
                } else {
                  this.setState({errorMsg: "Error: Please try again later"});
                }
              })
          
      } 
        this.setState({validated: true});
    }
  } 




  triggerTooltip = (event) => {
    this.setState({[event.target.name]: true})
  };

  hideTooltip = (event) => {
    this.setState({[event.target.name]: false})
  }


  handleTagChange = (tags) => {
    this.setState({tags});
  }
  
  handleListTagClick = (tag) => {
    this.setState({tags: [...this.state.tags, tag]});
  }
  
  render() {
  
    const { crop, croppedImageUrl, src } = this.state;

  return (
    <Container fluid style={{margin: "0 auto", maxWidth: "1100px"}}>
      <Modal size="lg" show={this.state.showModal} onHide={this.handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Crop image</Modal.Title>
        </Modal.Header>
        <Modal.Body style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
        {src && (
          <ReactCrop
            src={src}
            crop={crop}
            ruleOfThirds
            onImageLoaded={this.onImageLoaded}
            onComplete={this.onCropComplete}
            onChange={this.onCropChange}
          />
        )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={this.handleClose}>
            Save
          </Button>
        </Modal.Footer>
      </Modal>

      <Form name="artuploadform" id="artuploadform" noValidate onSubmit={this.handleSubmit}  validated={this.state.validated}>
        <h1>New Listing</h1>
        <div className="photos-upload">
          <div className="">
            <h4 className="sub-heading">Photos</h4>
            <small><i>Maximum 15MB per image</i></small>
            {this.state.tooBig && <Alert className="mt-2" variant="danger">
              Please upload a smaller image
            </Alert>}
          </div>


          <Row className="mt-3 ml-0 mr-0">
            <Col className="primary-image p-0">
              <label htmlFor="custom-file" className="primary-img-upload" style={{border: this.state.imgError ? '1px solid #dc4245' : "none"}}>
                <input
                hidden 
                required
                id="custom-file"
                type="file" accept="image/*" onChange={this.onSelectFile}
                class="form-control-file" 
                />
                <div id="crop-preview" style={{ height: '100%', width: '100%', position: 'relative'}}>
                  {croppedImageUrl && <Button onClick={this.handleShow} id="edit-crop">Edit Crop</Button>}
                  {croppedImageUrl && (
                    <img alt="Crop" style={{ width: '100%', height: '100%', objectFit: 'contain'}} src={croppedImageUrl} /> 
                  ) ? <img alt="Crop" style={{ width: '100%', height: '100%', objectFit: 'contain'}} src={croppedImageUrl} /> :  <img alt="Crop" style={{ width: '100%', height: '100%', objectFit: 'contain'}} src="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png" />}
                </div>
              </label>
            </Col>

            <Col>
              <Row>
                <Col className="other-images-container mb-1" style={{paddingRight: "0px"}}>
                  <label htmlFor="pic1" className="newbtn">
                    {this.state.addImgOne ? <img src={this.state.addImgOne} id="img_display_1" className="images" /> : <img id="img_display_1" className="images"  src="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png" />}
                    <input id="pic1" className='pic'  accept="image/*"  type="file" hidden onChange={this.onSelectAdditionalImg}></input>
                  </label>
                
                </Col>
                <Col className="other-images-container" style={{paddingLeft: "10px", paddingRight: "0px"}}>
                  <label htmlFor="pic2" className="newbtn">
                    {this.state.addImgTwo ? <img src={this.state.addImgTwo} id="img_display_2" className="images" /> : <img id="img_display_2" className="images"  src="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png" />}
                    <input id="pic2" className='pic'  accept="image/*"  type="file" hidden onChange={this.onSelectAdditionalImg}></input>
                  </label>
                </Col>
              </Row>
              <Row>
                <Col className="other-images-container mb-1" style={{paddingRight: "0px"}}>
                  <label htmlFor="pic3" className="newbtn">
                    {this.state.addImgThree ? <img src={this.state.addImgThree} id="img_display_3" className="images" /> : <img id="img_display_3" className="images"  src="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png" />}
                    <input id="pic3" className='pic' accept="image/*"  type="file" hidden onChange={this.onSelectAdditionalImg}></input>
                  </label>
                </Col>
                <Col className="other-images-container" style={{paddingLeft: "10px", paddingRight: "0px"}}>
                  <label htmlFor="pic4" className="newbtn">
                    {this.state.addImgFour ? <img src={this.state.addImgFour} id="img_display_4" className="images" /> : <img id="img_display_4" className="images"  src="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png" />}
                    <input id="pic4" className='pic' accept="image/*"  type="file" hidden onChange={this.onSelectAdditionalImg}></input>
                  </label>
                </Col>
              </Row>
            </Col>
          </Row>
        </div>


        {/* Color picker */}
        <Form.Group className="section col-12 mt-4" style={{position: "relative", marginBottom: "5px"}}>
        <h4 className="sub-heading mb-1">Color Scheme*</h4>
        <small>We recommend filling all of the color fields to maximize the views your listing gets. Buyers often search for art by colour.</small>
        <div style={{width: "fit-content", padding: "5px", marginTop: "8px", display: "flex", border: this.state.colorError ? '1.5px solid #dc4245' : "none", minHeight: "30px"}}>

          {/* Color One */}
          <div id="palletteOne" style={{minHeight: "30px"}}>
            {this.state.palletteOne && <div className="pallette">
              <div style={{display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px"}}>
                <button type="button" style={{border: "none", color: "#343a40"}} onClick={this.hidePallette} name="palletteOne">x</button>
              </div>
              {pallettes.map((pallette) => (
                <div className="d-flex align-items-center justify-content-center" style={{width: "fit-content"}}>
                  {pallette.map((color) => (
                    <button type="button" value={color} style={{padding: "12px", backgroundColor:color, border: "none"}} onClick={this.setColor} name="colorOne">
                    </button>
                  ))}
                </div>
              ))} 
              <Button type="button" variant="dark" size="sm" className="mt-2 btn-block" onClick={this.resetColor} name="colorOne">Reset</Button>
            </div>}

            <button type="button" onClick={this.showPallette} name="palletteOne" style={{background: this.state.colorOne ? this.state.colorOne : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4"}}>
              <input type='text' defaultValue={this.state.colorOne} id="custom" name="custom" form="artuploadform" className="form-control input-md" hidden/>
            </button>
          </div>


          {/* Color Two */}
          <div>
            {this.state.palletteTwo && <div className="pallette">
              <div style={{display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px"}}>
                <button type="button" style={{border: "none", color: "#343a40"}} onClick={this.hidePallette} name="palletteTwo">x</button>
              </div>
              {pallettes.map((pallette) => (
                <div  className="d-flex align-items-center justify-content-center" style={{width: "fit-content"}}>
                  {pallette.map((color) => (
                    <button type="button" value={color} style={{padding: "12px", backgroundColor:color, border: "none"}} onClick={this.setColor} name="colorTwo">
                    </button>
                  ))}
                </div>
              ))} 
              <Button type="button" variant="dark" size="sm" className="mt-2 btn-block" onClick={this.resetColor} name="colorTwo">Reset</Button>
            </div>}

            <button type="button" onClick={this.showPallette} name="palletteTwo" style={{background: this.state.colorTwo ? this.state.colorTwo : "url('https://i.imgur.com/FeZYt6x.jpg')",  padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4"}}>
              <input type='text' defaultValue={this.state.colorTwo} id="custom" name="custom" form="artuploadform" className="form-control input-md" hidden/>
            </button>
          </div>

          {/* Color Three */}
          <div>
            {this.state.palletteThree && <div className="pallette">
              <div style={{display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px"}}>
                <button type="button" style={{border: "none", color: "#343a40"}} onClick={this.hidePallette} name="palletteThree">x</button>
              </div>
              {pallettes.map((pallette) => (
                <div  className="d-flex align-items-center justify-content-center" style={{width: "fit-content"}}>
                  {pallette.map((color) => (
                    <button type="button" value={color} style={{padding: "12px", backgroundColor:color, border: "none"}} onClick={this.setColor} name="colorThree">
                    </button>
                  ))}
                </div>
              ))} 
              <Button type="button" variant="dark" size="sm" className="mt-2 btn-block" onClick={this.resetColor} name="colorThree">Reset</Button>
            </div>}

            <button type="button" onClick={this.showPallette} name="palletteThree" style={{background: this.state.colorThree ? this.state.colorThree : "url('https://i.imgur.com/FeZYt6x.jpg')",  padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4"}}>
              <input type='text' defaultValue={this.state.colorThree} id="custom" name="custom" form="artuploadform" className="form-control input-md" hidden/>
            </button>
          </div>

          {/* Color Four */}
          <div>
            {this.state.palletteFour && <div className="pallette">
              <div style={{display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px"}}>
                <button type="button" style={{border: "none", color: "#343a40"}} onClick={this.hidePallette} name="palletteFour">x</button>
              </div>
              {pallettes.map((pallette) => (
                <div  className="d-flex align-items-center justify-content-center" style={{width: "fit-content"}}>
                  {pallette.map((color) => (
                    <button type="button" value={color} style={{padding: "12px", backgroundColor:color, border: "none"}} onClick={this.setColor} name="colorFour">
                    </button>
                  ))}
                </div>
              ))} 
              <Button type="button" variant="dark" size="sm" className="mt-2 btn-block" onClick={this.resetColor} name="colorFour">Reset</Button>
            </div>}

            <button type="button" onClick={this.showPallette} name="palletteFour" style={{background: this.state.colorFour ? this.state.colorFour : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4"}}>
              <input type='text' defaultValue={this.state.colorFour} id="custom" name="custom" form="artuploadform" className="form-control input-md" hidden/>
            </button>
          </div>

          {/* Color Five */}
          <div>
            {this.state.palletteFive && <div className="pallette">
              <div style={{display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px"}}>
                <button type="button" style={{border: "none", color: "#343a40"}} onClick={this.hidePallette} name="palletteFive">x</button>
              </div>
              {pallettes.map((pallette) => (
                <div  className="d-flex align-items-center justify-content-center" style={{width: "fit-content"}}>
                  {pallette.map((color) => (
                    <button type="button" value={color} style={{padding: "12px", backgroundColor: color, border: "none"}} onClick={this.setColor} name="colorFive">
                    </button>
                  ))}
                </div>
              ))} 
              <Button type="button" variant="dark" size="sm" className="mt-2 btn-block" onClick={this.resetColor} name="colorFive">Reset</Button>
            </div>}

            
            <button type="button" onClick={this.showPallette} name="palletteFive" style={{background: this.state.colorFive ? this.state.colorFive : "url('https://i.imgur.com/FeZYt6x.jpg')",  padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4"}}>
                <input type='text' defaultValue={this.state.colorFive} id="custom" name="custom" form="artuploadform" className="form-control input-md" hidden/>
            </button>
          </div>
        </div>
      </Form.Group> 

      <Form.Group className="col-12 mb-4 mt-3">
          <Form.Label><h4 className="sub-heading">Title*</h4></Form.Label>
          <Form.Control value={this.state.title} type='text' id="artname" name="title" form="artuploadform" data-name="Art Name" onChange={this.handleChange} required/>
      </Form.Group>


      <Form.Group className="section col-12 mb-4">
          <div className="d-flex align-items-center mb-3">
            <h4 className="sub-heading m-0">Description*</h4>
            <button type="button" className="fas fa-question-circle" name="descriptionTooltip" onMouseEnter={this.triggerTooltip} onMouseLeave={this.hideTooltip} style={{position: "relative", border: "none", backgroundColor: "transparent", color: "black"}}></button>
          </div>
          {this.state.descriptionTooltip && <div className="hover_div_des">Description (Recommended 300 characters): We recommend at least 400 characters for your description. Here are a few questions that might get your creative juices flowing. Feel free to come up with any other information you think might portray more character and give your piece a more vivid story. What inspired you to create the piece? What message and story are you trying to tell? How does this piece relate to your life? What techniques did you use and why? What does it mean to you? What does it represent in terms of your artistic work as a whole? </div>}
          <Form.Control value={this.state.description} as="textarea" className="form-control" id="artdescription" name="description"  rows="5" placeholder='Example (We recommend at least 300 characters): I painted this piece in 2019 while I was living in Germany. I splashed acrylic paint, and used scratching tools, pallet knives, and brushes on the canvas to add texture. I’ve also used splattering, pouring, and airbrushing techniques and I made use of bright colours to depict the vibrant nightlife in Germany. This piece is special to me since it represents the ups, downs, and lessons I learned throughout my twenties. It further represents my realization that I was brought to this earth to share my ideas and connect with humanity. This piece is ideal for a curious and insightful owner.' data-name="Art Description" onChange={this.handleChange} required></Form.Control>
        </Form.Group>

        <div className="section col-12 mb-3">
          <h4 className="sub-heading mb-15">Details</h4>

          <Row className="mb-4">
            <Col className="pr-0">
              <Form.Group className="mr-10"> 
                <Form.Control as="select" id="category" defaultValue={''} name="category" form="artuploadform" data-name="Category" required onChange={this.handleChange}>
                  <option disabled={true} value="">Category*</option>
                  {Object.entries(category).map(([key, value]) => (<option value={key} name="category">{value}</option>))}
                </Form.Control>
              </Form.Group>
            </Col>
            <Col>
              <Form.Group id="fordynamicsubcategory">
                <Form.Control as="select" defaultValue={''} name="subcategory" className="form-control" id="subcategory" form="artuploadform" required onChange={this.handleChange}>
                  <option disabled={true} value="">Subject</option>
                  {this.state.subcategories && Object.entries(this.state.subcategories).map(([key, value]) => (<option value={key} name="category">{value}</option>))}
                </Form.Control>
              </Form.Group>
            </Col>
          </Row>


          <Form.Group id="style" className="mb-4">
            <Form.Label><h6 className="sub-heading">Style*</h6></Form.Label> 
            <br/>
            {Object.entries(styles).map(([key, value]) => ( <Form.Check inline label={value} type="checkbox" id={key} className={this.state.stylesError ? "style_art error" : "style_art"} value={key} name="styles" onChange={this.handleStyleSelect}/>))}
          </Form.Group> 


          <Form.Group id="material" className="mb-4">
            <Form.Label><h6 className="sub-heading">Material*</h6></Form.Label> 
            <br/>
            {Object.entries(material).map(([key, value]) => (<Form.Check inline label={value} type="checkbox" id={key} className={this.state.materialsError ? "material_art error" : "material_art"} name="materials" value={key} onChange={this.handleMaterialSelect}/>))}
            
          </Form.Group> 

          <Form.Group id="signed" className="mb-4">
            <Form.Label><h6 className="sub-heading">Signed?*</h6></Form.Label> 
            <br/>
            <Form.Check inline label="Yes" required value="Yes" type="radio" id="yes-check" name="signed" onChange={this.handleChange}/>
            <Form.Check inline label="No" required type="radio" id="no-check" value="No" name="signed" onChange={this.handleChange}/>
          </Form.Group>

          <Form.Group id="framed">
            <Form.Label><h6 className="sub-heading">Framed & ready to hang?*</h6></Form.Label> 
            <br/>
              <Form.Check inline required label="Yes" value="yes" type="radio" id="yes-check" name="framed" onChange={this.handleChange}/>
              <Form.Check inline required label="No" value="no" type="radio" id="no-check" name="framed" onChange={this.handleChange}/>
              <Form.Check inline required label="Other" value="other" type="radio" id="other-check" name="framed" onChange={this.handleChange}/>
          </Form.Group>

        </div>

        <div className="section col-12 mb-3 mt-3">
          <h4 className="sub-heading mb-2">Size</h4>

          <Form.Group id="dimensions" className="mb-4">
            <Form.Label><h6 className="sub-heading">Dimensions</h6></Form.Label>
            <Row>
              <Col className="pr-0">
                <Form.Control type='number' min="0" step="0.01" id="height" name="height"  form="artuploadform" placeholder="Height*" data-name="Height" required onChange={this.handleChange}/>
              </Col>
              <Col  className="pr-0">
                <Form.Control type='number'  min="0" step="0.01" id="width" name="width" form="artuploadform" className="form-control" placeholder="Width*" required data-name="Width" onChange={this.handleChange}/>
              </Col>
              <Col>
                <Form.Control type='number'  min="0" step="0.01" id="depth" name="depth" form="artuploadform" min="0" className="form-control" placeholder="Depth (Optional. Leave blank if not applicable)" onChange={this.handleChange}/>
              </Col>
            </Row>        
          </Form.Group>

          <div>          
            <Form.Label><h6 className="sub-heading">Unit of Measurement*</h6></Form.Label>
            <Form.Group>
              <Form.Control as="select" defaultValue={''} id="measure" name="unitOfMeasurement" form="artuploadform" data-name="Measurement" onChange={this.handleChange} required>
                <option value="" disabled={true} hidden={true}>Select unit</option>
                {Object.entries(dim_measurement).map(([key, value]) => (<option value={value}>{key}</option>))}       
              </Form.Control>
            </Form.Group> 
          </div>

        </div>

        <div className="section form-group col-12 mb-3 mt-3">
          <Form.Label className="mb-2">
            <div className="d-flex align-items-center">
              <h4 className="sub-heading mb-0">Tags*</h4>
              <button type="button" className="fas fa-question-circle" name="tagsTooltip" onMouseEnter={this.triggerTooltip} onMouseLeave={this.hideTooltip} style={{position: "relative", border: "none", backgroundColor: "transparent", color: "black"}}></button>
            </div>
              {this.state.tagsTooltip && <div className="hover_div">We recommend using at least 5 tags to optimize the number of views your posts get. The more tags, the better! Tags let other users, and Bidgala, know what your content is about and can help your listing rank higher in our search results. Specifically, when a buyer searches a phrase that is similar to one of your tags, your post will show up higher in their search results page.  Tags should describe your post’s content, story, message, materials, mood, etc. Imagine you are describing your painting to someone who cannot see it. Example: plastic, tape, pastel marker, happy, love, expressive, dog, person, grass, trees, zen, New York, street, dark</div>}
          </Form.Label>
          <br/> 
          <small>
          We recommend using at least 5 tags to optimize the number of views your posts get. Example: plastic, tape, pastel marker, happy, Love, expressive, dog, person, grass, trees, zen, New York, street, dark
          </small>
          <div className="mt-3">
            <TagInput onTagChange={this.handleTagChange} tags={this.state.tags} />
          </div> 
        </div>  


        <div className="section col-12 mt-3">
          <Form.Label className="mb-15"><h4 className="sub-heading">Pricing*</h4></Form.Label>
          <InputGroup className="mb-3 flex-nowrap">
            <div className="input-group-prepend">
              <InputGroup.Text>$</InputGroup.Text>
            </div>
            <Form.Control  min="0" type="number" step="0.01" className="form-control" aria-describedby="basic-addon2" id="price" name="price" placeholder="Price" required onChange={this.handleChange}/>
            <div className="input-group-append">
              <InputGroup.Text>USD</InputGroup.Text>
            </div>
          </InputGroup>
        </div>

        <div className="section col-12 mt-3 mb-4">
          <label className="col-form-label mb-15"><h4 className="sub-heading">Shipping</h4></label>
            <div className="d-flex flex-wrap form-row">
              <div className="col-xs-12 col-sm-12 col-md-6">
                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control type="number"  min="0" step="0.01" className="form-control atleast-one-cost" placeholder="United States" aria-label="Ship to US" aria-describedby="basic-addon2" id="shipus" name="shipUs" onChange={this.handleChange} disabled={this.state.show_price_us ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_us" name="show_price_us" checked={this.state.show_price_us} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_us"></label>
                  </div>
                </div>

                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control type="number"  min="0" step="0.01" className="form-control atleast-one-cost" placeholder="Canada" aria-label="Ship to Canada" aria-describedby="basic-addon2" id="shipcan" name="shipCan" onChange={this.handleChange} disabled={this.state.show_price_can ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_can" name="show_price_can" checked={this.state.show_price_can} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_can"></label>
                  </div>
                </div>

                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control  min="0" type="number" step="0.01" className="form-control atleast-one-cost" placeholder="United Kingdom" aria-label="Ship to United Kingdom" aria-describedby="basic-addon2" id="shipuk" name="shipUk" onChange={this.handleChange} disabled={this.state.show_price_uk ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_uk" name="show_price_uk" checked={this.state.show_price_uk} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_uk"></label>
                  </div>
                </div>


                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control  min="0" type="number" step="0.01" className="form-control atleast-one-cost" placeholder="Europe" aria-label="Ship to Europe" aria-describedby="basic-addon2" id="shipeurope" name="shipEurope" onChange={this.handleChange} disabled={this.state.show_price_europe ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_europe" name="show_price_europe" checked={this.state.show_price_europe} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_europe"></label>
                  </div>
                </div>
              </div>

              <div className="column-two col-xs-12 col-sm-12 col-md-6">
                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control  min="0" type="number" step="0.01" className="form-control atleast-one-cost" placeholder="Australia/New Zealand" aria-label="Ship to Australia or New Zealand" aria-describedby="basic-addon2" id="shipaunz" name="shipAunz" onChange={this.handleChange} disabled={this.state.show_price_aunz ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_aunz" name="show_price_aunz" checked={this.state.show_price_aunz} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_aunz"></label>
                  </div>
                </div>


                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control  min="0" type="number" step="0.01" className="form-control atleast-one-cost" placeholder="Asia" aria-label="Ship to Asia" aria-describedby="basic-addon2" id="shipasia" name="shipAsia" onChange={this.handleChange} disabled={this.state.show_price_asia ? "" : "disabled"}/>
                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>

                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_asia" name="show_price_asia" checked={this.state.show_price_asia} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_asia"></label>
                  </div>
                </div>
            
                <div className="d-flex">
                  <InputGroup className="mb-3">
                    <div className="input-group-prepend">
                      <InputGroup.Text>$</InputGroup.Text>
                    </div>
                    <Form.Control  min="0" type="number" step="0.01" className="form-control atleast-one-cost" placeholder="Other" aria-label="Ship to Other" aria-describedby="basic-addon2" id="shipother" name="shipOther" onChange={this.handleChange} disabled={this.state.show_price_other ? "" : "disabled"}/>

                    <div className="input-group-append">
                      <InputGroup.Text>USD</InputGroup.Text>
                    </div>
                  </InputGroup>
                  <div className="custom-control custom-switch ml-1">
                    <input type="checkbox" className="custom-control-input" id="show_price_other" name="show_price_other" checked={this.state.show_price_other} onChange={this.toggleSwitch} />
                    <label className="custom-control-label" htmlFor="show_price_other"></label>
                  </div>

                  
                </div>
              </div>


          </div>
        </div>





        <div id="submit-btn-container">
          <span id="forerrormessage"></span>
          {this.state.errorMsg && <Alert className="mt-2" variant="danger">
              {this.state.errorMsg}
            </Alert>}
            {this.state.shippingError && <Alert className="mt-2" variant="danger">
              {this.state.shippingError}
            </Alert>}
          <Button type="submit" variant="dark" className="submit">Post Your Art</Button> 
        </div>
      </Form>
    
    </Container>
    );
  }
} 





ReactDOM.render(<ArtUploadForm/>, document.getElementById('react_upload_form'));