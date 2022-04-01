var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var ReactCrop = ReactCrop.Component;
var Form = ReactBootstrap.Form;
var Modal = ReactBootstrap.Modal;
var Button = ReactBootstrap.Button;
var InputGroup = ReactBootstrap.InputGroup;
var Col = ReactBootstrap.Col;
var Row = ReactBootstrap.Row;
var Container = ReactBootstrap.Container;
var ButtonGroup = ReactBootstrap.ButtonGroup;
var FormCheck = ReactBootstrap.FormCheck;
var Alert = ReactBootstrap.Alert;

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

var dim_measurement = {
  Meter: 'm',
  Centimeter: 'cm',
  Inches: 'inches'
};

var styles = {
  abstract: 'Abstract',
  contemporary: 'Contemporary',
  figurative: 'Figurative',
  minimalist: 'Minimalist',
  portraiture: 'Portraiture',
  landscape: 'Landscape',
  fashion: 'Fashion',
  popart: 'Pop Art',
  other: 'Other'
};

var material = {
  canvas: 'Canvas',
  paper: 'Paper',
  wood: 'Wood',
  cardboard: 'Cardboard',
  soft: 'Soft (Yam, Cotton, Fabric)',
  plastic: 'Plastic',
  aluminum: 'Aluminum',
  glass: 'Glass',
  carbonfibre: 'Carbon Fibre',
  steel: 'Steel',
  iron: 'Iron',
  bronze: 'Bronze',
  ceramic: 'Ceramic',
  stone: 'Stone',
  stainlesssteel: 'Stainless Steel',
  marble: 'Marble',
  other: 'Other'

};

var category = {
  paintings: 'Paintings',
  prints: 'Prints',
  drawingIllustration: 'Drawing & Illustration',
  photography: 'Photography',
  sculptures: 'Sculptures',
  ceramicPottery: 'Ceramic & Pottery',
  glass: 'Glass'

};

var pallettes = [["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"], ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"], ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"], ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"], ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"], ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"], ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"], ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]];

var Helpers = function () {
  function Helpers() {
    _classCallCheck(this, Helpers);
  }

  _createClass(Helpers, null, [{
    key: 'contains',
    value: function contains(orig, filter) {
      var res = filter.map(function (item) {
        return orig.includes(item);
      });
      return !res.includes(false);
    }
  }, {
    key: 'hasDuplicates',
    value: function hasDuplicates(array) {
      return new Set(array).size !== array.length;
    }
  }]);

  return Helpers;
}();

var Tag = function Tag(_ref) {
  var name = _ref.name,
      index = _ref.index,
      onDelete = _ref.onDelete,
      hashtag = _ref.hashtag,
      hashtagStyle = _ref.hashtagStyle;

  return React.createElement(
    'li',
    { key: index },
    hashtag && React.createElement(
      'span',
      { style: Object.assign({ color: '#898989', fontWeight: 'bold' }, hashtagStyled) },
      '# '
    ),
    name,
    React.createElement(
      'button',
      { type: 'button', id: 'tag-d-btn', onClick: function onClick(e) {
          return onDelete(index, e);
        } },
      'x'
    )
  );
};

var TagsList = function TagsList(_ref2) {
  var tags = _ref2.tags,
      onTagDelete = _ref2.onTagDelete,
      hashtag = _ref2.hashtag;

  var list = tags.map(function (tag, index) {
    return React.createElement(Tag, {
      name: tag,
      onDelete: onTagDelete,
      index: index,
      hashtag: hashtag });
  });
  return React.createElement(
    'ul',
    { name: 'tagsList', className: 'tagsList' },
    list
  );
};

var TagInput = function (_React$Component) {
  _inherits(TagInput, _React$Component);

  function TagInput(props) {
    _classCallCheck(this, TagInput);

    var _this = _possibleConstructorReturn(this, (TagInput.__proto__ || Object.getPrototypeOf(TagInput)).call(this, props));

    _this.handleNewTag = function (tags) {
      if (_this.props.onNewTag) _this.props.onNewTag(tags);
      if (_this.props.onTagChange) _this.props.onTagChange(tags);
    };

    _this.handleInputChange = function (_ref3) {
      var inputValue = _ref3.target.value;

      inputValue = inputValue == ',' ? '' : inputValue;
      _this.setState({ inputValue: inputValue });
    };

    _this.handleKeyDown = function (e) {
      var keyCode = e.keyCode,
          value = e.target.value;
      var tags = _this.state.tags;

      switch (keyCode) {
        case 9:
          if (value) e.preventDefault();
        case 13:
          e.preventDefault();
        case 188:
          value = value.trim();
          if (value && _this.notDuplicate(tags, value)) {
            _this.addTag(value);
          } else {
            _this.setState({ inputValue: '' });
          }
          break;
        case 32:
          value = value.trim();
          if (value && _this.notDuplicate(tags, value)) {
            _this.addTag(value);
          }
        case 8:
          if (!value) {
            _this.handleTagDelete(tags.length - 1);
          }
          break;
      }
    };

    _this.handleTagDelete = function (index, e) {
      _this.deleteTag(index, function () {
        _this.props.onTagChange(_this.state.tags);
      });
    };

    _this.deleteTag = function (index, callback) {
      var tags = _this.state.tags.slice();

      tags.splice(index, 1);
      _this.setState({ tags: tags }, function () {
        if (callback) callback();
      });
    };

    _this.notDuplicate = function (tags, newTag) {
      return !tags.includes(newTag) || _this.props.allowDuplicates;
    };

    _this.addTag = function (tag) {
      if (_this.notDuplicate(_this.state.tags, tag)) {
        _this.setState({ tags: [].concat(_toConsumableArray(_this.state.tags), [tag]), inputValue: '' }, function () {
          _this.handleNewTag(_this.state.tags);
        });
      }
    };

    _this.state = {
      inputValue: '',
      tags: _this.props.tags || []
    };
    return _this;
  }

  _createClass(TagInput, [{
    key: 'render',
    value: function render() {
      return React.createElement(
        'span',
        { className: 'tagInputWrapper' },
        React.createElement(TagsList, {
          tags: this.state.tags,
          onTagDelete: this.handleTagDelete,
          hashtag: this.props.hashtag
        }),
        React.createElement('input', {
          name: 'tagInput',
          className: 'tagInput',
          placeholder: 'Enter tags...',
          value: this.state.inputValue,
          onChange: this.handleInputChange,
          onKeyDown: this.handleKeyDown
        })
      );
    }
  }]);

  return TagInput;
}(React.Component);

var ArtUploadForm = function (_React$Component2) {
  _inherits(ArtUploadForm, _React$Component2);

  function ArtUploadForm() {
    var _ref4;

    var _temp, _this2, _ret;

    _classCallCheck(this, ArtUploadForm);

    for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    return _ret = (_temp = (_this2 = _possibleConstructorReturn(this, (_ref4 = ArtUploadForm.__proto__ || Object.getPrototypeOf(ArtUploadForm)).call.apply(_ref4, [this].concat(args))), _this2), _this2.state = {
      src: null,
      crop: {
        unit: '%',
        width: 20,
        height: 20,
      },
      img_blob: null,
      showModal: false,
      addImgOne: null,
      addImgTwo: null,
      addImgThree: null,
      addImgFour: null,
      imgZero:null,
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
      errorMsg: null
    }, _this2.toggleSwitch = function (event) {
      var shippingToggle = event.target.name;
      _this2.setState(_defineProperty({}, event.target.name, !_this2.state[shippingToggle]));
    }, _this2.setColor = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, event.target.value));
    }, _this2.showPallette = function (event) {
      _this2.setState({palletteOne: false, palletteTwo: false, palletteThree: false, palletteFour: false, palletteFive: false});
      _this2.setState(_defineProperty({}, event.target.name, true));
    }, _this2.hidePallette = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, false));
    }, _this2.resetColor = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, ""));
    }, _this2.handleChange = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, event.target.value));
      if (event.target.name == "category") {
        axios({
          method: 'post',
          url: '/get-sub-category',
          timeout: 4000,
          data: {
            category: event.target.value
          }
        }).then(function (response) {
          var subcats = response.data.data;
          _this2.setState({ subcategories: subcats });
        }).catch(function (error) {
          return console.error('timeout exceeded');
        });
      }
    }, _this2.handleStyleSelect = function (event) {
      if (event.target.checked) {
        _this2.setState(_defineProperty({}, event.target.name, [].concat(_toConsumableArray(_this2.state.styles), [event.target.value])));
      } else {
        var index = _this2.state.styles.indexOf(event.target.value);
        if (index > -1) {
          _this2.state.styles.splice(index, 1);
          _this2.setState(_defineProperty({}, event.target.name, _this2.state.styles));
        }
      }
    }, _this2.handleMaterialSelect = function (event) {
      if (event.target.checked) {
        _this2.setState(_defineProperty({}, event.target.name, [].concat(_toConsumableArray(_this2.state.materials), [event.target.value])));
      } else {
        var index = _this2.state.materials.indexOf(event.target.value);
        if (index > -1) {
          _this2.state.materials.splice(index, 1);
          _this2.setState(_defineProperty({}, event.target.name, _this2.state.materials));
        }
      }
    }, _this2.handleClose = function () {
      _this2.setState({ showModal: false });
    }, _this2.handleShow = function () {
      _this2.setState({ showModal: true });
    }, 
    _this2.onSelectFile = function (e) {
      if (e.target.files[0].size > 15000000) {
        _this2.setState({ tooBig: true });
      } else if (e.target.files && e.target.files.length > 0) {
        _this2.setState({ tooBig: false });
        var reader = new FileReader();
        reader.addEventListener('load', function () {
          
          // remove_reactcrop Remove two lines below
          $('#main_img').val( reader.result )
          $('#main_img').attr('src', reader.result )

          return _this2.setState({ src : reader.result });
          
        });
        reader.readAsDataURL(e.target.files[0]);
        // remove_reactcrop Uncomment Below Line 
        // _this2.handleShow();
      }
    },_this2.onImageLoaded = function (image) {
      _this2.imageRef = image;
    },_this2.onCropComplete = function (crop) {
      _this2.makeClientCrop(crop);
    }, _this2.onCropChange = function (crop, percentCrop) {
      // You could also use percentCrop:
      // this.setState({ crop: percentCrop });
      _this2.setState({ crop: crop });
    },_this2.onSelectAdditionalImg = function (event) {
      if (event.target.files[0].size > 15000000) {
        _this2.setState({ tooBig: true });
      }
      else if (event.target.id == 'pic1') {
        _this2.setState({ tooBig: false });
        URL.revokeObjectURL(event.target.files[0]);
        _this2.setState({ addImgOne: URL.createObjectURL(event.target.files[0]) });
        _this2.readFile(event.target.files[0], "imgOne");
      } else if (event.target.id == "pic2") {
        _this2.setState({ tooBig: false });
        URL.revokeObjectURL(event.target.files[0]);
        _this2.setState({ addImgTwo: URL.createObjectURL(event.target.files[0]) });
        _this2.readFile(event.target.files[0], "imgTwo");
      } else if (event.target.id == "pic3") {
        _this2.setState({ tooBig: false });
        URL.revokeObjectURL(event.target.files[0]);
        _this2.setState({ addImgThree: URL.createObjectURL(event.target.files[0]) });
        _this2.readFile(event.target.files[0], "imgThree");
      } else if (event.target.id == "pic4") {
        _this2.setState({ tooBig: false });
        URL.revokeObjectURL(event.target.files[0]);
        _this2.setState({ addImgFour: URL.createObjectURL(event.target.files[0]) });
        _this2.readFile(event.target.files[0], "imgFour");
      }
    }, _this2.validateCheckbox = function () {
      var materials = _this2.state.materials;
      var isChecked = materials.some(function (material) {
        return material.checked == true;
      });

      if (isChecked) {
        return true;
      }
    },
     _this2.validate = function () {
      if (_this2.state.img_blob) {
        _this2.setState({ imgError: false });
      }
      if (_this2.state.colorOne || _this2.state.colorTwo || _this2.state.colorThree || _this2.state.colorFour || _this2.state.colorFive) {
        _this2.setState({ colorError: false });
      } else {
        _this2.setState({ colorError: true });
      }
      if (_this2.state.materials.length > 0) {
        _this2.setState({ materialsError: false });
      }
      if (_this2.state.styles.length > 0) {
        _this2.setState({ stylesError: false });
      }
      if (!_this2.state.img_blob) {
        _this2.setState({ imgError: false });// remove_reactcrop make imgError: true in this if condition
      }
      if (_this2.state.materials.length < 1) {
        _this2.setState({ materialsError: true });
      }
      if (_this2.state.styles.length < 1) {
        _this2.setState({ stylesError: true });
      }
      if (!_this2.state.show_price_asia && !_this2.state.show_price_aunz && !_this2.state.show_price_can && !_this2.state.show_price_europe && !_this2.state.show_price_uk && !_this2.state.show_price_us && !_this2.state.show_price_other) {
        _this2.setState({ shippingError: "Please enter atleast one shipping price" });
      } else {
        _this2.setState({ shippingError: null });
      }
      // remove_reactcrop add  _this2.state.img_blob to below if condition
      if (!_this2.state.shippingError && _this2.state.materials.length > 0 && _this2.state.styles.length > 0 && (_this2.state.colorOne || _this2.state.colorTwo || _this2.state.colorThree || _this2.state.colorFour || _this2.state.colorFive)) {
        return true;
      } else {
        _this2.setState({ errorMsg: "Please fill in missing fields" });
        return false;
      }
    }, _this2.handleSubmit = function (event) {
      event.preventDefault();
      var form = event.currentTarget;
      if (form.checkValidity() === false) {
        _this2.setState({ errorMsg: "Please fill in missing fields" });
      }
      if (_this2.validate() === true) {
        if (form.checkValidity() === true) {
          $("#preloader-active").css("display", "block");
          axios.post('/art/add-art', {
            //remove_reactcrop Uncomment below line
            // art_img: _this2.state.img_blob,
            //remove_reactcrop Remove Below Line 
            art_img:  $('#main_img').val(),
            additional_img_1: _this2.state.imgOne,
            additional_img_2: _this2.state.imgTwo,
            additional_img_3: _this2.state.imgThree,
            additional_img_4: _this2.state.imgFour,
            color: _this2.state.colorOne,
            color_1: _this2.state.colorTwo,
            color_2: _this2.state.colorThree,
            color_3: _this2.state.colorFour,
            color_4: _this2.state.colorFive,
            title: _this2.state.title,
            desc: _this2.state.description,
            tags: _this2.state.tags,
            height: _this2.state.height,
            width: _this2.state.width,
            depth: _this2.state.depth,
            cat: _this2.state.category,
            subcat: _this2.state.subcategory,
            measure: _this2.state.unitOfMeasurement,
            price: _this2.state.price,
            s_price_can: _this2.state.shipCan,
            s_price_us: _this2.state.shipUs,
            s_price_uk: _this2.state.shipUk,
            s_price_aunz: _this2.state.shipAunz,
            s_price_asia: _this2.state.shipAsia,
            s_price_europe: _this2.state.shipEurope,
            s_price_other: _this2.state.shipOther,
            show_price_can: _this2.state.show_price_can,
            show_price_us: _this2.state.show_price_us,
            show_price_uk: _this2.state.show_price_uk,
            show_price_aunz: _this2.state.show_price_aunz,
            show_price_asia: _this2.state.show_price_asia,
            show_price_europe: _this2.state.show_price_europe,
            show_price_other: _this2.state.show_price_other,
            styles: _this2.state.styles,
            materials: _this2.state.materials,
            is_signed: _this2.state.signed,
            is_framed_ready: _this2.state.framed 
          }).then(function (response) {
            if (response.data.status === "success") {
              window.location.replace("product_view/" + response.data.product_id);
            } else if (response.data.status === "login"){
              $("#preloader-active").css("display", "none");
              $('#loginModal').modal('show'); 
              _this2.setState({ errorMsg: response.data.message });
            } else {
              $("#preloader-active").css("display", "none");
              _this2.setState({ errorMsg: response.data.status + ":" + response.data.message });
            }
          }).catch(function (error) {
            $("#preloader-active").css("display", "none");
            if (error.response) {
              _this2.setState({ errorMsg: error.response.data.status + " " + error.response.status + ":" + error.response.data.message });
            } else {
              _this2.setState({ errorMsg: "Error: Please try again later" });
            }
          });
        }
        _this2.setState({ validated: true });
      }
    }, _this2.triggerTooltip = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, true));
    }, _this2.hideTooltip = function (event) {
      _this2.setState(_defineProperty({}, event.target.name, false));
    }, _this2.handleTagChange = function (tags) {
      _this2.setState({ tags: tags });
    }, _this2.handleListTagClick = function (tag) {
      _this2.setState({ tags: [].concat(_toConsumableArray(_this2.state.tags), [tag]) });
    }, _temp), _possibleConstructorReturn(_this2, _ret);
  }

  _createClass(ArtUploadForm, [{
    key: 'makeClientCrop',
    value: function makeClientCrop(crop) {
      var _this3 = this;

      if (this.imageRef && crop.width && crop.height) {
        this.getCroppedImg(this.imageRef, crop, 'newFile.png').then(function (croppedImageUrl) {
          _this3.setState({ croppedImageUrl: croppedImageUrl });
        });
      }
    }
  }, {
    key: 'getCroppedImg',
    value: function getCroppedImg(image, crop, fileName) {
      var _this4 = this;

      var canvas = document.createElement('canvas');
      var scaleX = image.naturalWidth / image.width;
      var scaleY = image.naturalHeight / image.height;
      canvas.width = Math.ceil(crop.width * scaleX);
      canvas.height = Math.ceil(crop.height * scaleY);
      var ctx = canvas.getContext('2d');

      ctx.drawImage(image, crop.x * scaleX, crop.y * scaleY, crop.width * scaleX, crop.height * scaleY, 0, 0, crop.width * scaleX, crop.height * scaleY);

      return new Promise(function (resolve, reject) {
        canvas.toBlob(function (blob) {
          if (!blob) {
            //reject(new Error('Canvas is empty'));
            console.error('Canvas is empty');
            return;
          }
          blob.name = fileName;
          var reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onload = function (event) {
            _this4.setState({ img_blob: reader.result });
          };

          window.URL.revokeObjectURL(_this4.fileUrl);
          _this4.fileUrl = window.URL.createObjectURL(blob);
          resolve(_this4.fileUrl);
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

  }, {
    key: 'readFile',
    value: function readFile(file, imgNum) {
      var _this5 = this;

      return new Promise(function (resolve, reject) {
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function (event) {
          _this5.setState(_defineProperty({}, imgNum, reader.result));
          resolve(reader.result);
          
        };
        reader.onerror = function (error) {
          
          return reject(error);
        };
      });
    }

    // This method is for getting client pic and base64 now

  }, {
    key: 'render',
    value: function render() {
      var _this6 = this,
          _React$createElement;

      var _state = this.state,
          crop = _state.crop,
          croppedImageUrl = _state.croppedImageUrl,
          src = _state.src;

          return React.createElement(
        Container,
        { fluid: true, style: { margin: "0 auto", maxWidth: "1100px" } },
        React.createElement(
          Modal,
          { size: 'lg', show: this.state.showModal, onHide: this.handleClose },
          React.createElement(
            Modal.Header,
            { closeButton: true },
            React.createElement(
              Modal.Title,
              null,
              'Crop image'
            )
          ),


          React.createElement(
            Modal.Body,
            { style: { display: 'flex', justifyContent: 'center', alignItems: 'center' } },
            // remove_reactcrop Uncomment below section
            // src && React.createElement(ReactCrop, {
            //   src: src,
            //   crop: crop,
            //   ruleOfThirds: true,
            //   onImageLoaded: this.onImageLoaded,
            //   onComplete: this.onCropComplete,
            //   onChange: this.onCropChange
            // })
          ),
          React.createElement(
            Modal.Footer,
            null,
            React.createElement(
              Button,
              { variant: 'secondary', onClick: this.handleClose },
              'Save'
            )
          )
        ),
        React.createElement(
          Form,
          { name: 'artuploadform', id: 'artuploadform', noValidate: true, onSubmit: this.handleSubmit, validated: this.state.validated },
          React.createElement(
            'h1',
            null,
            'New Listing'
          ),
          React.createElement(
            'div',
            { className: 'photos-upload' },
            React.createElement(
              'div',
              { className: '' },
              React.createElement(
                'h4',
                { className: 'sub-heading' },
                'Photos'
              ),
              React.createElement(
                'small',
                null,
                React.createElement(
                  'i',
                  null,
                  'Maximum 15MB per image'
                )
              ),
              this.state.tooBig && React.createElement(
                Alert,
                { className: 'mt-2', variant: 'danger' },
                'Please upload a smaller image'
              )
            ),
            React.createElement(
              Row,
              { className: 'mt-3 ml-0 mr-0' },
              React.createElement(
                Col,
                { className: 'primary-image p-0' },
                React.createElement(
                  'label',
                  { htmlFor: 'custom-file', className: 'primary-img-upload', style: { border: this.state.imgError ? '1px solid #dc4245' : "none" } },
                  React.createElement('input', {
                    hidden: true,
                    required: true,
                    id: 'custom-file',
                    type: 'file', accept: 'image/*', onChange: this.onSelectFile,
                    'class': 'form-control-file'
                  }),
                  React.createElement(
                    'div',
                    { id: 'crop-preview', style: { height: '100%', width: '100%', position: 'relative' } },
                    croppedImageUrl && React.createElement(
                      Button,
                      { onClick: this.handleShow, id: 'edit-crop' },
                      'Edit Crop'
                    ),
                    croppedImageUrl && React.createElement('img', { id: 'main_img', alt: 'Crop', style: { width: '100%', height: '100%', objectFit: 'contain' }, src: '' /*remove_reactcrop add croppedImgURL to src and remove main_img id to img tags */}) ? React.createElement('img', {id: 'main_img', alt: 'Crop', style: { width: '100%', height: '100%', objectFit: 'contain' }, src: '' /*remove_reactcrop add croppedImgURL to src and remove main_img id to img tags */}) : React.createElement('img', {id: 'main_img', alt: 'Crop', style: { width: '100%', height: '100%', objectFit: 'contain' }, src: 'https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png' })
                  )
                )
              ),
              React.createElement(
                Col,
                null,
                React.createElement(
                  Row,
                  null,
                  React.createElement(
                    Col,
                    { className: 'other-images-container mb-1', style: { paddingRight: "0px" } },
                    React.createElement(
                      'label',
                      { htmlFor: 'pic1', className: 'newbtn' },
                      this.state.addImgOne ? React.createElement('img', { src: this.state.addImgOne, id: 'img_display_1', className: 'images' }) : React.createElement('img', { id: 'img_display_1', className: 'images', src: 'https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png' }),
                      React.createElement('input', { id: 'pic1', className: 'pic', accept: 'image/*', type: 'file', hidden: true, onChange: this.onSelectAdditionalImg })
                    )
                  ),
                  React.createElement(
                    Col,
                    { className: 'other-images-container', style: { paddingLeft: "10px", paddingRight: "0px" } },
                    React.createElement(
                      'label',
                      { htmlFor: 'pic2', className: 'newbtn' },
                      this.state.addImgTwo ? React.createElement('img', { src: this.state.addImgTwo, id: 'img_display_2', className: 'images' }) : React.createElement('img', { id: 'img_display_2', className: 'images', src: 'https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png' }),
                      React.createElement('input', { id: 'pic2', className: 'pic', accept: 'image/*', type: 'file', hidden: true, onChange: this.onSelectAdditionalImg })
                    )
                  )
                ),
                React.createElement(
                  Row,
                  null,
                  React.createElement(
                    Col,
                    { className: 'other-images-container mb-1', style: { paddingRight: "0px" } },
                    React.createElement(
                      'label',
                      { htmlFor: 'pic3', className: 'newbtn' },
                      this.state.addImgThree ? React.createElement('img', { src: this.state.addImgThree, id: 'img_display_3', className: 'images' }) : React.createElement('img', { id: 'img_display_3', className: 'images', src: 'https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png' }),
                      React.createElement('input', { id: 'pic3', className: 'pic', accept: 'image/*', type: 'file', hidden: true, onChange: this.onSelectAdditionalImg })
                    )
                  ),
                  React.createElement(
                    Col,
                    { className: 'other-images-container', style: { paddingLeft: "10px", paddingRight: "0px" } },
                    React.createElement(
                      'label',
                      { htmlFor: 'pic4', className: 'newbtn' },
                      this.state.addImgFour ? React.createElement('img', { src: this.state.addImgFour, id: 'img_display_4', className: 'images' }) : React.createElement('img', { id: 'img_display_4', className: 'images', src: 'https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png' }),
                      React.createElement('input', { id: 'pic4', className: 'pic', accept: 'image/*', type: 'file', hidden: true, onChange: this.onSelectAdditionalImg })
                    )
                  )
                )
              )
            )
          ),
          React.createElement(
            Form.Group,
            { className: 'section col-12 mt-4', style: { position: "relative", marginBottom: "5px" } },
            React.createElement(
              'h4',
              { className: 'sub-heading mb-1' },
              'Colour Scheme*'
            ),
            React.createElement(
              'small',
              null,
              'We recommend filling all of the colour fields to maximize the views your listing gets. Buyers often search for art by colour.'
            ),
            React.createElement(
              'div',
              { style: { width: "fit-content", padding: "5px", marginTop: "8px", display: "flex", border: this.state.colorError ? '1.5px solid #dc4245' : "none", minHeight: "30px" } },
              React.createElement(
                'div',
                { id: 'palletteOne', style: { minHeight: "30px" } },
                this.state.palletteOne && React.createElement(
                  'div',
                  { className: 'pallette' },
                  React.createElement(
                    'div',
                    { style: { display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px" } },
                    React.createElement(
                      'button',
                      { type: 'button', style: { border: "none", color: "#343a40" }, onClick: this.hidePallette, name: 'palletteOne' },
                      'x'
                    )
                  ),
                  pallettes.map(function (pallette) {
                    return React.createElement(
                      'div',
                      { className: 'd-flex align-items-center justify-content-center', style: { width: "fit-content" } },
                      pallette.map(function (color) {
                        return React.createElement('button', { type: 'button', value: color, style: { padding: "12px", backgroundColor: color, border: "none" }, onClick: _this6.setColor, name: 'colorOne' });
                      })
                    );
                  }),
                  React.createElement(
                    Button,
                    { type: 'button', variant: 'dark', size: 'sm', className: 'mt-2 btn-block', onClick: this.resetColor, name: 'colorOne' },
                    'Reset'
                  )
                ),
                React.createElement(
                  'button',
                  { type: 'button', onClick: this.showPallette, name: 'palletteOne', style: { background: this.state.colorOne ? this.state.colorOne : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4" } },
                  React.createElement('input', { type: 'text', defaultValue: this.state.colorOne, id: 'custom', name: 'custom', form: 'artuploadform', className: 'form-control input-md', hidden: true })
                )
              ),
              React.createElement(
                'div',
                null,
                this.state.palletteTwo && React.createElement(
                  'div',
                  { className: 'pallette' },
                  React.createElement(
                    'div',
                    { style: { display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px" } },
                    React.createElement(
                      'button',
                      { type: 'button', style: { border: "none", color: "#343a40" }, onClick: this.hidePallette, name: 'palletteTwo' },
                      'x'
                    )
                  ),
                  pallettes.map(function (pallette) {
                    return React.createElement(
                      'div',
                      { className: 'd-flex align-items-center justify-content-center', style: { width: "fit-content" } },
                      pallette.map(function (color) {
                        return React.createElement('button', { type: 'button', value: color, style: { padding: "12px", backgroundColor: color, border: "none" }, onClick: _this6.setColor, name: 'colorTwo' });
                      })
                    );
                  }),
                  React.createElement(
                    Button,
                    { type: 'button', variant: 'dark', size: 'sm', className: 'mt-2 btn-block', onClick: this.resetColor, name: 'colorTwo' },
                    'Reset'
                  )
                ),
                React.createElement(
                  'button',
                  { type: 'button', onClick: this.showPallette, name: 'palletteTwo', style: { background: this.state.colorTwo ? this.state.colorTwo : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4" } },
                  React.createElement('input', { type: 'text', defaultValue: this.state.colorTwo, id: 'custom', name: 'custom', form: 'artuploadform', className: 'form-control input-md', hidden: true })
                )
              ),
              React.createElement(
                'div',
                null,
                this.state.palletteThree && React.createElement(
                  'div',
                  { className: 'pallette' },
                  React.createElement(
                    'div',
                    { style: { display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px" } },
                    React.createElement(
                      'button',
                      { type: 'button', style: { border: "none", color: "#343a40" }, onClick: this.hidePallette, name: 'palletteThree' },
                      'x'
                    )
                  ),
                  pallettes.map(function (pallette) {
                    return React.createElement(
                      'div',
                      { className: 'd-flex align-items-center justify-content-center', style: { width: "fit-content" } },
                      pallette.map(function (color) {
                        return React.createElement('button', { type: 'button', value: color, style: { padding: "12px", backgroundColor: color, border: "none" }, onClick: _this6.setColor, name: 'colorThree' });
                      })
                    );
                  }),
                  React.createElement(
                    Button,
                    { type: 'button', variant: 'dark', size: 'sm', className: 'mt-2 btn-block', onClick: this.resetColor, name: 'colorThree' },
                    'Reset'
                  )
                ),
                React.createElement(
                  'button',
                  { type: 'button', onClick: this.showPallette, name: 'palletteThree', style: { background: this.state.colorThree ? this.state.colorThree : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4" } },
                  React.createElement('input', { type: 'text', defaultValue: this.state.colorThree, id: 'custom', name: 'custom', form: 'artuploadform', className: 'form-control input-md', hidden: true })
                )
              ),
              React.createElement(
                'div',
                null,
                this.state.palletteFour && React.createElement(
                  'div',
                  { className: 'pallette' },
                  React.createElement(
                    'div',
                    { style: { display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px", minWidth: "160px" } },
                    React.createElement(
                      'button',
                      { type: 'button', style: { border: "none", color: "#343a40" }, onClick: this.hidePallette, name: 'palletteFour' },
                      'x'
                    )
                  ),
                  pallettes.map(function (pallette) {
                    return React.createElement(
                      'div',
                      { className: 'd-flex align-items-center justify-content-center', style: { width: "fit-content" } },
                      pallette.map(function (color) {
                        return React.createElement('button', { type: 'button', value: color, style: { padding: "12px", backgroundColor: color, border: "none" }, onClick: _this6.setColor, name: 'colorFour' });
                      })
                    );
                  }),
                  React.createElement(
                    Button,
                    { type: 'button', variant: 'dark', size: 'sm', className: 'mt-2 btn-block', onClick: this.resetColor, name: 'colorFour' },
                    'Reset'
                  )
                ),
                React.createElement(
                  'button',
                  { type: 'button', onClick: this.showPallette, name: 'palletteFour', style: { background: this.state.colorFour ? this.state.colorFour : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4" } },
                  React.createElement('input', { type: 'text', defaultValue: this.state.colorFour, id: 'custom', name: 'custom', form: 'artuploadform', className: 'form-control input-md', hidden: true })
                )
              ),
              React.createElement(
                'div',
                null,
                this.state.palletteFive && React.createElement(
                  'div',
                  { className: 'pallette' },
                  React.createElement(
                    'div',
                    { style: { display: "flex", justifyContent: "flex-start", marginLeft: "-15px", marginTop: "-5px", marginBottom: "5px" } },
                    React.createElement(
                      'button',
                      { type: 'button', style: { border: "none", color: "#343a40" }, onClick: this.hidePallette, name: 'palletteFive' },
                      'x'
                    )
                  ),
                  pallettes.map(function (pallette) {
                    return React.createElement(
                      'div',
                      { className: 'd-flex align-items-center justify-content-center', style: { width: "fit-content" } },
                      pallette.map(function (color) {
                        return React.createElement('button', { type: 'button', value: color, style: { padding: "12px", backgroundColor: color, border: "none" }, onClick: _this6.setColor, name: 'colorFive' });
                      })
                    );
                  }),
                  React.createElement(
                    Button,
                    { type: 'button', variant: 'dark', size: 'sm', className: 'mt-2 btn-block', onClick: this.resetColor, name: 'colorFive' },
                    'Reset'
                  )
                ),
                React.createElement(
                  'button',
                  { type: 'button', onClick: this.showPallette, name: 'palletteFive', style: { background: this.state.colorFive ? this.state.colorFive : "url('https://i.imgur.com/FeZYt6x.jpg')", padding: "15px", borderRadius: "5px", marginRight: "5px", border: "1.5px solid #a4a4a4" } },
                  React.createElement('input', { type: 'text', defaultValue: this.state.colorFive, id: 'custom', name: 'custom', form: 'artuploadform', className: 'form-control input-md', hidden: true })
                )
              )
            )
          ),
          React.createElement(
            Form.Group,
            { className: 'col-12 mb-4 mt-3' },
            React.createElement(
              Form.Label,
              null,
              React.createElement(
                'h4',
                { className: 'sub-heading' },
                'Title*'
              )
            ),
            React.createElement(Form.Control, { value: this.state.title, type: 'text', id: 'artname', name: 'title', form: 'artuploadform', 'data-name': 'Art Name', onChange: this.handleChange, required: true })
          ),
          React.createElement(
            Form.Group,
            { className: 'section col-12 mb-4' },
            React.createElement(
              'div',
              { className: 'd-flex align-items-center mb-3' },
              React.createElement(
                'h4',
                { className: 'sub-heading m-0' },
                'Description*'
              ),
              React.createElement('button', { type: 'button', className: 'fas fa-question-circle', name: 'descriptionTooltip', onMouseEnter: this.triggerTooltip, onMouseLeave: this.hideTooltip, style: { position: "relative", border: "none", backgroundColor: "transparent", color: "black" } })
            ),
            this.state.descriptionTooltip && React.createElement(
              'div',
              { className: 'hover_div_des' },
              'Description (Recommended 300 characters): We recommend at least 400 characters for your description. Here are a few questions that might get your creative juices flowing. Feel free to come up with any other information you think might portray more character and give your piece a more vivid story. What inspired you to create the piece? What message and story are you trying to tell? How does this piece relate to your life? What techniques did you use and why? What does it mean to you? What does it represent in terms of your artistic work as a whole? '
            ),
            React.createElement(Form.Control, { value: this.state.description, as: 'textarea', className: 'form-control', id: 'artdescription', name: 'description', rows: '5', placeholder: 'Example (We recommend at least 300 characters): I painted this piece in 2019 while I was living in Germany. I splashed acrylic paint, and used scratching tools, pallet knives, and brushes on the canvas to add texture. I\u2019ve also used splattering, pouring, and airbrushing techniques and I made use of bright colours to depict the vibrant nightlife in Germany. This piece is special to me since it represents the ups, downs, and lessons I learned throughout my twenties. It further represents my realization that I was brought to this earth to share my ideas and connect with humanity. This piece is ideal for a curious and insightful owner.', 'data-name': 'Art Description', onChange: this.handleChange, required: true })
          ),
          React.createElement(
            'div',
            { className: 'section col-12 mb-3' },
            React.createElement(
              'h4',
              { className: 'sub-heading mb-15' },
              'Details'
            ),
            React.createElement(
              Row,
              { className: 'mb-4' },
              React.createElement(
                Col,
                { className: 'pr-0' },
                React.createElement(
                  Form.Group,
                  { className: 'mr-10' },
                  React.createElement(
                    Form.Control,
                    { as: 'select', id: 'category', defaultValue: '', name: 'category', form: 'artuploadform', 'data-name': 'Category', required: true, onChange: this.handleChange },
                    React.createElement(
                      'option',
                      { disabled: true, value: '' },
                      'Category*'
                    ),
                    Object.entries(category).map(function (_ref5) {
                      var _ref6 = _slicedToArray(_ref5, 2),
                          key = _ref6[0],
                          value = _ref6[1];

                      return React.createElement(
                        'option',
                        { value: key, name: 'category' },
                        value
                      );
                    })
                  )
                )
              ),
              React.createElement(
                Col,
                null,
                React.createElement(
                  Form.Group,
                  { id: 'fordynamicsubcategory' },
                  React.createElement(
                    Form.Control,
                    { as: 'select', defaultValue: '', name: 'subcategory', className: 'form-control', id: 'subcategory', form: 'artuploadform', required: true, onChange: this.handleChange },
                    React.createElement(
                      'option',
                      { disabled: true, value: '' },
                      'Subject'
                    ),
                    this.state.subcategories && Object.entries(this.state.subcategories).map(function (_ref7) {
                      var _ref8 = _slicedToArray(_ref7, 2),
                          key = _ref8[0],
                          value = _ref8[1];

                      return React.createElement(
                        'option',
                        { value: key, name: 'category' },
                        value
                      );
                    })
                  )
                )
              )
            ),
            React.createElement(
              Form.Group,
              { id: 'style', className: 'mb-4' },
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Style*'
                )
              ),
              React.createElement('br', null),
              Object.entries(styles).map(function (_ref9) {
                var _ref10 = _slicedToArray(_ref9, 2),
                    key = _ref10[0],
                    value = _ref10[1];

                return React.createElement(Form.Check, { inline: true, label: value, type: 'checkbox', id: key, className: _this6.state.stylesError ? "style_art error" : "style_art", value: key, name: 'styles', onChange: _this6.handleStyleSelect });
              })
            ),
            React.createElement(
              Form.Group,
              { id: 'material', className: 'mb-4' },
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Material*'
                )
              ),
              React.createElement('br', null),
              Object.entries(material).map(function (_ref11) {
                var _ref12 = _slicedToArray(_ref11, 2),
                    key = _ref12[0],
                    value = _ref12[1];

                return React.createElement(Form.Check, { inline: true, label: value, type: 'checkbox', id: key, className: _this6.state.materialsError ? "material_art error" : "material_art", name: 'materials', value: key, onChange: _this6.handleMaterialSelect });
              })
            ),
            React.createElement(
              Form.Group,
              { id: 'signed', className: 'mb-4' },
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Signed?*'
                )
              ),
              React.createElement('br', null),
              React.createElement(Form.Check, { inline: true, label: 'Yes', required: true, value: 'Yes', type: 'radio', id: 'yes-check', name: 'signed', onChange: this.handleChange }),
              React.createElement(Form.Check, { inline: true, label: 'No', required: true, type: 'radio', id: 'no-check', value: 'No', name: 'signed', onChange: this.handleChange })
            ),
            React.createElement(
              Form.Group,
              { id: 'framed' },
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Framed & ready to hang?*'
                )
              ),
              React.createElement('br', null),
              React.createElement(Form.Check, { inline: true, required: true, label: 'Yes', value: 'yes', type: 'radio', id: 'yes-check', name: 'framed', onChange: this.handleChange }),
              React.createElement(Form.Check, { inline: true, required: true, label: 'No', value: 'no', type: 'radio', id: 'no-check', name: 'framed', onChange: this.handleChange }),
              React.createElement(Form.Check, { inline: true, required: true, label: 'Other', value: 'other', type: 'radio', id: 'other-check', name: 'framed', onChange: this.handleChange })
            )
          ),
          React.createElement(
            'div',
            { className: 'section col-12 mb-3 mt-3' },
            React.createElement(
              'h4',
              { className: 'sub-heading mb-2' },
              'Size'
            ),
            React.createElement(
              Form.Group,
              { id: 'dimensions', className: 'mb-4' },
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Dimensions'
                )
              ),
              React.createElement(
                Row,
                null,
                React.createElement(
                  Col,
                  { className: 'pr-0' },
                  React.createElement(Form.Control, { type: 'number', min: '0', step: '0.01', id: 'height', name: 'height', form: 'artuploadform', placeholder: 'Height*', 'data-name': 'Height', required: true, onChange: this.handleChange })
                ),
                React.createElement(
                  Col,
                  { className: 'pr-0' },
                  React.createElement(Form.Control, { type: 'number', min: '0', step: '0.01', id: 'width', name: 'width', form: 'artuploadform', className: 'form-control', placeholder: 'Width*', required: true, 'data-name': 'Width', onChange: this.handleChange })
                ),
                React.createElement(
                  Col,
                  null,
                  React.createElement(Form.Control, (_React$createElement = { type: 'number', min: '0', step: '0.01', id: 'depth', name: 'depth', form: 'artuploadform' }, _defineProperty(_React$createElement, 'min', '0'), _defineProperty(_React$createElement, 'className', 'form-control'), _defineProperty(_React$createElement, 'placeholder', 'Depth (Optional. Leave blank if not applicable)'), _defineProperty(_React$createElement, 'onChange', this.handleChange), _React$createElement))
                )
              )
            ),
            React.createElement(
              'div',
              null,
              React.createElement(
                Form.Label,
                null,
                React.createElement(
                  'h6',
                  { className: 'sub-heading' },
                  'Unit of Measurement*'
                )
              ),
              React.createElement(
                Form.Group,
                null,
                React.createElement(
                  Form.Control,
                  { as: 'select', defaultValue: '', id: 'measure', name: 'unitOfMeasurement', form: 'artuploadform', 'data-name': 'Measurement', onChange: this.handleChange, required: true },
                  React.createElement(
                    'option',
                    { value: '', disabled: true, hidden: true },
                    'Select unit'
                  ),
                  Object.entries(dim_measurement).map(function (_ref13) {
                    var _ref14 = _slicedToArray(_ref13, 2),
                        key = _ref14[0],
                        value = _ref14[1];

                    return React.createElement(
                      'option',
                      { value: value },
                      key
                    );
                  })
                )
              )
            )
          ),
          React.createElement(
            'div',
            { className: 'section form-group col-12 mb-3 mt-3' },
            React.createElement(
              Form.Label,
              { className: 'mb-2' },
              React.createElement(
                'div',
                { className: 'd-flex align-items-center' },
                React.createElement(
                  'h4',
                  { className: 'sub-heading mb-0' },
                  'Tags*'
                ),
                React.createElement('button', { type: 'button', className: 'fas fa-question-circle', name: 'tagsTooltip', onMouseEnter: this.triggerTooltip, onMouseLeave: this.hideTooltip, style: { position: "relative", border: "none", backgroundColor: "transparent", color: "black" } })
              ),
              this.state.tagsTooltip && React.createElement(
                'div',
                { className: 'hover_div' },
                'We recommend using at least 5 tags to optimize the number of views your posts get. The more tags, the better! Tags let other users, and Bidgala, know what your content is about and can help your listing rank higher in our search results. Specifically, when a buyer searches a phrase that is similar to one of your tags, your post will show up higher in their search results page.  Tags should describe your post\u2019s content, story, message, materials, mood, etc. Imagine you are describing your painting to someone who cannot see it. Example: plastic, tape, pastel marker, happy, love, expressive, dog, person, grass, trees, zen, New York, street, dark'
              )
            ),
            React.createElement('br', null),
            React.createElement(
              'small',
              null,
              'We recommend using at least 5 tags to optimize the number of views your posts get. Example: plastic, tape, pastel marker, happy, Love, expressive, dog, person, grass, trees, zen, New York, street, dark'
            ),
            React.createElement(
              'div',
              { className: 'mt-3' },
              React.createElement(TagInput, { onTagChange: this.handleTagChange, tags: this.state.tags })
            )
          ),
          React.createElement(
            'div',
            { className: 'section col-12 mt-3' },
            React.createElement(
              Form.Label,
              { className: 'mb-15' },
              React.createElement(
                'h4',
                { className: 'sub-heading' },
                'Pricing*'
              )
            ),
            React.createElement(
              InputGroup,
              { className: 'mb-3 flex-nowrap' },
              React.createElement(
                'div',
                { className: 'input-group-prepend' },
                React.createElement(
                  InputGroup.Text,
                  null,
                  '$'
                )
              ),
              React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control', 'aria-describedby': 'basic-addon2', id: 'price', name: 'price', placeholder: 'Price', required: true, onChange: this.handleChange }),
              React.createElement(
                'div',
                { className: 'input-group-append' },
                React.createElement(
                  InputGroup.Text,
                  null,
                  'USD'
                )
              )
            )
          ),
          React.createElement(
            'div',
            { className: 'section col-12 mt-3 mb-4' },
            React.createElement(
              'label',
              { className: 'col-form-label mb-15' },
              React.createElement(
                'h4',
                { className: 'sub-heading' },
                'Shipping'
              )
            ),
            React.createElement(
              'div',
              { className: 'd-flex flex-wrap form-row' },
              React.createElement(
                'div',
                { className: 'col-xs-12 col-sm-12 col-md-6' },
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { type: 'number', min: '0', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'United States', 'aria-label': 'Ship to US', 'aria-describedby': 'basic-addon2', id: 'shipus', name: 'shipUs', onChange: this.handleChange, disabled: this.state.show_price_us ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_us', name: 'show_price_us', checked: this.state.show_price_us, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_us' })
                  )
                ),
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { type: 'number', min: '0', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'Canada', 'aria-label': 'Ship to Canada', 'aria-describedby': 'basic-addon2', id: 'shipcan', name: 'shipCan', onChange: this.handleChange, disabled: this.state.show_price_can ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_can', name: 'show_price_can', checked: this.state.show_price_can, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_can' })
                  )
                ),
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'United Kingdom', 'aria-label': 'Ship to United Kingdom', 'aria-describedby': 'basic-addon2', id: 'shipuk', name: 'shipUk', onChange: this.handleChange, disabled: this.state.show_price_uk ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_uk', name: 'show_price_uk', checked: this.state.show_price_uk, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_uk' })
                  )
                ),
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'Europe', 'aria-label': 'Ship to Europe', 'aria-describedby': 'basic-addon2', id: 'shipeurope', name: 'shipEurope', onChange: this.handleChange, disabled: this.state.show_price_europe ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_europe', name: 'show_price_europe', checked: this.state.show_price_europe, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_europe' })
                  )
                )
              ),
              React.createElement(
                'div',
                { className: 'column-two col-xs-12 col-sm-12 col-md-6' },
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'Australia/New Zealand', 'aria-label': 'Ship to Australia or New Zealand', 'aria-describedby': 'basic-addon2', id: 'shipaunz', name: 'shipAunz', onChange: this.handleChange, disabled: this.state.show_price_aunz ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_aunz', name: 'show_price_aunz', checked: this.state.show_price_aunz, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_aunz' })
                  )
                ),
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'Asia', 'aria-label': 'Ship to Asia', 'aria-describedby': 'basic-addon2', id: 'shipasia', name: 'shipAsia', onChange: this.handleChange, disabled: this.state.show_price_asia ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_asia', name: 'show_price_asia', checked: this.state.show_price_asia, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_asia' })
                  )
                ),
                React.createElement(
                  'div',
                  { className: 'd-flex' },
                  React.createElement(
                    InputGroup,
                    { className: 'mb-3' },
                    React.createElement(
                      'div',
                      { className: 'input-group-prepend' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        '$'
                      )
                    ),
                    React.createElement(Form.Control, { min: '0', type: 'number', step: '0.01', className: 'form-control atleast-one-cost', placeholder: 'Other', 'aria-label': 'Ship to Other', 'aria-describedby': 'basic-addon2', id: 'shipother', name: 'shipOther', onChange: this.handleChange, disabled: this.state.show_price_other ? "" : "disabled" }),
                    React.createElement(
                      'div',
                      { className: 'input-group-append' },
                      React.createElement(
                        InputGroup.Text,
                        null,
                        'USD'
                      )
                    )
                  ),
                  React.createElement(
                    'div',
                    { className: 'custom-control custom-switch ml-1' },
                    React.createElement('input', { type: 'checkbox', className: 'custom-control-input', id: 'show_price_other', name: 'show_price_other', checked: this.state.show_price_other, onChange: this.toggleSwitch }),
                    React.createElement('label', { className: 'custom-control-label', htmlFor: 'show_price_other' })
                  )
                )
              )
            )
          ),
          React.createElement(
            'div',
            { id: 'submit-btn-container' },
            React.createElement('span', { id: 'forerrormessage' }),
            this.state.errorMsg && React.createElement(
              Alert,
              { className: 'mt-2', variant: 'danger' },
              this.state.errorMsg
            ),
            this.state.shippingError && React.createElement(
              Alert,
              { className: 'mt-2', variant: 'danger' },
              this.state.shippingError
            ),
            React.createElement(
              Button,
              { type: 'submit', variant: 'dark', className: 'submit' },
              'Post Your Art'
            )
          )
        )
      );
    }
  }]);

  return ArtUploadForm;
}(React.Component);

ReactDOM.render(React.createElement(ArtUploadForm, null), document.getElementById('react_upload_form'));
