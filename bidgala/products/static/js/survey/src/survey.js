const Survey = () => {
    const [startSurvey, setStartSurvey] = React.useState('');
    const [displayFirst, setDisplayFirst] = React.useState('d-none');
    const [displaySecond, setDisplaySecond] = React.useState('d-none');
    const [displayThird, setDisplayThird] = React.useState('d-none');
    const [displayFourth, setDisplayFourth] = React.useState('d-none');
    const [displayFifth, setDisplayFifth] = React.useState('d-none');
    const [displaySixth, setDisplaySixth] = React.useState('d-none');
    const [displaySeventh, setDisplaySeventh] = React.useState('d-none');
    const [displayEighth, setDisplayEighth] = React.useState('d-none');
    const [endSurvey, setEndSurvey] = React.useState('d-none');

    const [categoryResponse, setCategoryResponse] = React.useState(null);
    const [categorySelectionCount, setCategorySelectionCount] = React.useState(0);
    const [categoryErrorMessage, setCategoryErrorMessage] = React.useState(false);
    const [userCategorySelection, setUserCategorySelection] = React.useState({});

    const [userStylesResponse, setUserStylesResponse] = React.useState(null);
    const [userStylesSelectionCount, setUserStylesSelectionCount] = React.useState(0);
    const [userStylesErrorMessage, setUserStylesErrorMessage] = React.useState(false);
    const [userStylesSelection, setUserStylesSelection] = React.useState({});

    const [userPreferenceResponse, setUserPreferenceResponse] = React.useState(null);
    const [userPreferenceSelectionCount, setUserPreferenceSelectionCount] = React.useState(0);
    const [userPreferenceErrorMessage, setUserPreferenceErrorMessage] = React.useState(false);
    const [userPreferenceSelection, setUserPreferenceSelection] = React.useState({});

    const [isHorizontalClicked, setIsHorizontalClicked] = React.useState(false);
    const [isVerticalClicked, setIsVerticalClicked] = React.useState(false);
    const [isSquareClicked, setIsSquareClicked] = React.useState(false);
    const [orientationSelected, setOrientationSelected] = React.useState({});

    const [isSmallClicked, setIsSmallClicked] = React.useState(false);
    const [isMediumClicked, setIsMediumClicked] = React.useState(false);
    const [isLargeClicked, setIsLargeClicked] = React.useState(false);
    const [isOversizeClicked, setIsOversizeClicked] = React.useState(false);
    const [sizesSelected, setSizesSelected] = React.useState({});

    const [budget, setBudget] = React.useState(0);
    const [budgetErrorMessage, setBudgetErrorMessage] = React.useState(false);

    const [firstName, setFirstName] = React.useState('');
    const [firstNameErrorMessage, setFirstNameErrorMessage] = React.useState(false);
    const [lastName, setLastName] = React.useState('');
    const [lastNameErrorMessage, setLastNameErrorMessage] = React.useState(false);
    const [email, setEmail] = React.useState('');
    const [emailErrorMessage, setEmailErrorMessage] = React.useState(false);
    const [phone, setPhone] = React.useState('');
    const [phoneErrorMessage, setPhoneErrorMessage] = React.useState(false);

    const [notes, setNotes] = React.useState('');
    const [newsletterSubscription, setNewsletterSubscription] = React.useState(true);
    // const [imageFile, setImageFile] = React.useState(null);

    const [isErrorMessage, setIsErrorMessage] = React.useState(false);
    const [errorMessage, setErrorMessage] = React.useState('');

    const handleClickStart = () => {
        setStartSurvey('d-none');
        setDisplayFirst('');
    }

    const handleClickBackFirst = () => {
        setStartSurvey('');
        setDisplayFirst('d-none');
    }

    const handleClickNextFirst = () => {
        setDisplaySecond('');
        setDisplayFirst('d-none');
    }

    const handleClickBackSecond = () => {
        setDisplayFirst('');
        setDisplaySecond('d-none');
    }

    const handleClickNextSecond = () => {
        setDisplayThird('');
        setDisplaySecond('d-none');
    }

    const handleClickBackThird = () => {
        setDisplaySecond('');
        setDisplayThird('d-none');
    }

    const handleClickNextThird = () => {
        setDisplayFourth('');
        setDisplayThird('d-none');
    }

    const handleClickBackFourth = () => {
        setDisplayThird('');
        setDisplayFourth('d-none');
    }

    const handleClickNextFourth = () => {
        setDisplayFifth('');
        setDisplayFourth('d-none');
    }

    const handleClickBackFifth = () => {
        setDisplayFourth('');
        setDisplayFifth('d-none');
    }

    const handleClickNextFifth = () => {
        setDisplaySixth('');
        setDisplayFifth('d-none');
    }

    const handleClickBackSixth = () => {
        setDisplayFifth('');
        setDisplaySixth('d-none');
    }

    const handleClickNextSixth = () => {
        if (budget >= 1000) {
            setDisplaySeventh('');
            setDisplaySixth('d-none');
        } else setBudgetErrorMessage(true);
    }

    const handleClickBackSeventh = () => {
        setDisplaySixth('');
        setDisplaySeventh('d-none');
    }

    const handleClickNextSeventh = () => {
        if (firstName === '' || firstNameErrorMessage) setFirstNameErrorMessage(true);
        else if (lastName === '' || lastNameErrorMessage) setLastNameErrorMessage(true);
        else if (email === '' || emailErrorMessage) setEmailErrorMessage(true);
        else if (!phoneErrorMessage) {
            setDisplayEighth('');
            setDisplaySeventh('d-none');
        }
    }

    const handleClickBackEighth = () => {
        setDisplaySeventh('');
        setDisplayEighth('d-none');
    }

    const handleClickNextEighth = () => {
        setEndSurvey('');
        setDisplayEighth('d-none');
        fetch('/survey/submit/advisory-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({categories: {...userCategorySelection}, styles: {...userStylesSelection}, pieces: {...userPreferenceSelection}, orientation: {...orientationSelected}, size: {...sizesSelected}, budget: budget, details: {firstName, lastName, email, phone}, additional: {notes, newsletterSubscription}})
        })
        .then(response => response.json())
        .then(data => {if (data.status === 'fail') {
            setErrorMessage(data.message);
            setIsErrorMessage(true);
        }
        } )
        .catch(() => {
            setErrorMessage("Something went wrong! Please try again later");
            setIsErrorMessage(true);
            });
    }

    const handleCategoryClicked = (event) => {
        const category = event.currentTarget.id;
        if (categorySelectionCount < 3) {
            if (!userCategorySelection[category]) {
                setUserCategorySelection({...userCategorySelection, [category]: true});
                setCategorySelectionCount(categorySelectionCount + 1);
            } else {
                setUserCategorySelection({...userCategorySelection, [category]: false});
                setCategorySelectionCount(categorySelectionCount - 1);
            }
            setCategoryErrorMessage(false);
        } else if (userCategorySelection[category]) {
            setUserCategorySelection({...userCategorySelection, [category]: false});
            setCategorySelectionCount(categorySelectionCount - 1);
            setCategoryErrorMessage(false);
        } else setCategoryErrorMessage(true);
    }

    const handleStyleClicked = (event) => {
        const style = event.currentTarget.id;
        if (userStylesSelectionCount < 3) {
            if (!userStylesSelection[style]) {
                setUserStylesSelection({...userStylesSelection, [style]: true});
                setUserStylesSelectionCount(userStylesSelectionCount + 1);
            } else {
                setUserStylesSelection({...userStylesSelection, [style]: false});
                setUserStylesSelectionCount(userStylesSelectionCount - 1);
            }
            setUserStylesErrorMessage(false);
        } else if (userStylesSelection[style]) {
            setUserStylesSelection({...userStylesSelection, [style]: false});
            setUserStylesSelectionCount(userStylesSelectionCount - 1);
            setUserStylesErrorMessage(false);
        } else setUserStylesErrorMessage(true);
    }

    const handlePieceClicked = (event) => {
        const piece = event.currentTarget.id;
        if (userPreferenceSelectionCount < 3) {
            if (!userPreferenceSelection[piece]) {
                setUserPreferenceSelection({...userPreferenceSelection, [piece]: true});
                setUserPreferenceSelectionCount(userPreferenceSelectionCount + 1);
            } else {
                setUserPreferenceSelection({...userPreferenceSelection, [piece]: false});
                setUserPreferenceSelectionCount(userPreferenceSelectionCount - 1);
            }
            setUserPreferenceErrorMessage(false);
        } else if (userPreferenceSelection[piece]) {
            setUserPreferenceSelection({...userPreferenceSelection, [piece]: false});
            setUserPreferenceSelectionCount(userPreferenceSelectionCount - 1);
            setUserPreferenceErrorMessage(false);
        } else setUserPreferenceErrorMessage(true);
    }

    const handleHorizontalClicked = () => {
        setIsHorizontalClicked(!isHorizontalClicked);
        if (!isHorizontalClicked) setOrientationSelected({...orientationSelected, horizontal: true});
        else setOrientationSelected({...orientationSelected, horizontal: false});
    }

    const handleVerticalClicked = () => {
        setIsVerticalClicked(!isVerticalClicked);
        if (!isVerticalClicked) setOrientationSelected({...orientationSelected, vertical: true});
        else setOrientationSelected({...orientationSelected, vertical: false});
    }

    const handleSquareClicked = () => {
        setIsSquareClicked(!isSquareClicked);
        if (!isSquareClicked) setOrientationSelected({...orientationSelected, square: true});
        else setOrientationSelected({...orientationSelected, square: false});
    }

    const handleSmallClicked = () => {
        setIsSmallClicked(!isSmallClicked);
        if (!isSmallClicked) setSizesSelected({...sizesSelected, small: true});
        else setSizesSelected({...sizesSelected, small: false});
    }

    const handleMediumClicked = () => {
        setIsMediumClicked(!isMediumClicked);
        if (!isMediumClicked) setSizesSelected({...sizesSelected, medium: true});
        else setSizesSelected({...sizesSelected, medium: false});
    }

    const handleLargeClicked = () => {
        setIsLargeClicked(!isLargeClicked);
        if (!isLargeClicked) setSizesSelected({...sizesSelected, large: true});
        else setSizesSelected({...sizesSelected, large: false});
    }

    const handleOversizeClicked = () => {
        setIsOversizeClicked(!isOversizeClicked);
        if (!isOversizeClicked) setSizesSelected({...sizesSelected, oversize: true});
        else setSizesSelected({...sizesSelected, oversize: false});
    }

    const handleBudget = (event) => {
        const amount = event.target.value;
        if (amount >= 1000) {
            setBudget(amount);
            setBudgetErrorMessage(false);
        } else setBudgetErrorMessage(true);
    }

    const handleFirstName = (event) => {
        const name = event.target.value;
        if (name.replace(/\s+/g, '').length >= 2) {
            setFirstName(name);
            setFirstNameErrorMessage(false);
        } else setFirstNameErrorMessage(true);
    }

    const handleLastName = (event) => {
        const name = event.target.value;
        if (name.replace(/\s+/g, '').length >= 2) {
            setLastName(name);
            setLastNameErrorMessage(false);
        } else setLastNameErrorMessage(true);
    }

    const handleEmail = (event) => {
        const email = event.target.value;
        const validEmailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (validEmailRegex.test(email)) {
            setEmail(email);
            setEmailErrorMessage(false);
        } else setEmailErrorMessage(true);
    }

    const handlePhone = (event) => {
        const phone = event.target.value;
        const validPhoneRegex = /^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
        if (phone === '') setPhoneErrorMessage(false);
        else if (validPhoneRegex.test(phone)) {
            setPhone(phone);
            setPhoneErrorMessage(false);
        } else setPhoneErrorMessage(true);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    React.useEffect(() => {
        fetch('/survey/options/user-preference-category-options')
           .then(res => res.json())
           .then(data => setCategoryResponse(data))
           .catch(error => console.error(error));

        fetch('/survey/options/user-preference-options')
           .then(res => res.json())
           .then(data => setUserPreferenceResponse(data))
           .catch(error => console.error(error));

        fetch('/survey/options/user-preference-style-options')
           .then(res => res.json())
           .then(data => setUserStylesResponse(data))
           .catch(error => console.error(error));

      
    }, []);

    return (
        <section className="survey container text-center mt-5">
            <div className={startSurvey}>
                <h2 className="h4">Welcome to Art Advisory</h2>
                <p className="w-75 m-auto pt-3 pb-4">Once you have answered a few short questions, our expert art curators will create a portfolio of art recommendations custom to your style, budget, and more. After you have completed the questionnaire, your free personal curator will send you an email with recommendations in 3-5 business days. Let's get started!</p>
                <button type="button" className="btn btn-dark" onClick={handleClickStart}>Start Survey</button>
            </div>
            <div className={displayFirst}>
                <h3 className="h5 mb-4">Your Preferred Categories</h3>
                <p className={categoryErrorMessage ? "alert alert-danger" : "d-none"}>You may select up to 3 categories</p>
                <div className="container">
                    <div className="category-row row row-cols-1 row-cols-md-2 w-75 m-auto">
                        {categoryResponse && categoryResponse.result.map(category => (
                            <div key={category.id} className="col position-relative">
                                <img src={`${categoryResponse.img_host_url}${category.image}`} alt={category.value} className={`survey-img img-fluid img-thumbnail ${userCategorySelection[category.value] ? "opacity" : ""}`} id={category.value} onClick={handleCategoryClicked} />
                                <p className={userCategorySelection[category.value] ? "text-muted" : ""}>{category.value}</p>
                                <i className={`fas fa-check position-absolute ${userCategorySelection[category.value] ? "category-clicked" : "d-none"}`} />
                            </div>
                        ))}
                    </div>
                </div>
                <div className="d-flex justify-content-between m-auto button-first">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackFirst}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextFirst}>next</button>
                </div>
            </div>
            <div className={displaySecond}>
                <h3 className="h5 mb-4">Select up to 3 Preferred Styles</h3>
                <p className={userStylesErrorMessage ? "alert alert-danger" : "d-none"}>You may select up to 3 styles</p>
                <div className="container">
                    <div className="row row-cols-1 row-cols-md-3">
                        {userStylesResponse && userStylesResponse.result.map(style => (
                            <div key={style.id} className="col position-relative">
                                <img src={`${userStylesResponse.img_host_url}${style.image}`} alt={style.value} className={`survey-img img-fluid img-thumbnail ${userStylesSelection[style.value] ? "opacity" : ""}`} id={style.value} onClick={handleStyleClicked} />
                                <p className={userStylesSelection[style.value] ? "text-muted" : ""}>{style.value}</p>
                                <i className={`fas fa-check position-absolute ${userStylesSelection[style.value] ? "style-clicked" : "d-none"}`} />
                            </div>
                        ))}
                    </div>
                </div>
                <div className="d-flex justify-content-between m-auto button-second">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackSecond}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextSecond}>next</button>
                </div>
            </div>
            <div className={displayThird}>
                <h3 className="h5 mb-4">Choose up to 3 Preferred Pieces</h3>
                <p className={userPreferenceErrorMessage ? "alert alert-danger" : "d-none"}>You may select up to 3 pieces</p>
                <div className="container">
                    <div className="row row-cols-1 row-cols-md-3">
                        {userPreferenceResponse && userPreferenceResponse.result.map(piece => (
                            <div key={piece.id} className="col position-relative">
                                <img src={`${userPreferenceResponse.img_host_url}${piece.image}`} alt={piece.value} className={`survey-img img-fluid img-thumbnail ${userPreferenceSelection[piece.value] ? "opacity" : ""}`} id={piece.value} onClick={handlePieceClicked} />
                                <p className={userPreferenceSelection[piece.value] ? "text-muted" : ""}>{piece.value}</p>
                                <i className={`fas fa-check position-absolute ${userPreferenceSelection[piece.value] ? "piece-clicked" : "d-none"}`} />
                            </div>
                        ))}
                    </div>
                </div>
                <div className="d-flex justify-content-between">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackThird}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextThird}>next</button>
                </div>
            </div>
            <div className={displayFourth}>
                <h3 className="h5 mb-4">Looking for a specific orientation? Select all that apply:</h3>
                <div className="d-flex flex-md-row flex-column justify-content-around mt-5 mb-4">
                    <span className="position-relative" id="horizontal">
                        <span className={`horizontal d-inline-block mt-md-5 ${isHorizontalClicked ? "light-grey" : "grey"}`} onClick={handleHorizontalClicked}></span>
                        <p className={isHorizontalClicked ? "text-muted" : ""}>Horizontal</p>
                        <i className={`fas fa-check position-absolute ${isHorizontalClicked ? "horizontal-clicked" : "d-none"}`} />
                    </span>
                    <span className="position-relative" id="vertical">
                        <span className={`vertical d-inline-block ${isVerticalClicked ? "light-grey" : "grey"}`} onClick={handleVerticalClicked}></span>
                        <p className={isVerticalClicked ? "text-muted" : ""}>Vertical</p>
                        <i className={`fas fa-check position-absolute ${isVerticalClicked ? "vertical-clicked" : "d-none"}`} />
                    </span>
                    <span className="position-relative" id="square">
                        <span className={`square shadow-sm d-inline-block mt-md-5 ${isSquareClicked ? "light-grey" : "grey"}`} onClick={handleSquareClicked}></span>
                        <p className={isSquareClicked ? "text-muted" : ""}>Square</p>
                        <i className={`fas fa-check position-absolute ${isSquareClicked ? "square-clicked" : "d-none"}`} />
                    </span>
                </div>
                <div className="d-flex justify-content-between m-auto button-fourth">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackFourth}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextFourth}>next</button>
                </div>
            </div>
            <div className={displayFifth}>
                <h3 className="h5 mb-4">Looking for a specific size?</h3>
                <div className="container-size d-flex flex-md-row flex-column">
                    <div className="position-relative mr-2">
                        <img src={"/static/img/survey/small.jpeg"} alt="small" className={`img-fluid img-thumbnail ${isSmallClicked ? "opacity" : ""}`} onClick={handleSmallClicked} />
                        <p className={`mt-2 ${isSmallClicked ? "text-muted" : ""}`}>Small</p>
                        <i className={`fas fa-check position-absolute ${isSmallClicked ? "sizes-clicked" : "d-none"}`} />
                    </div>
                    <div className="position-relative mr-2">
                        <img src={"/static/img/survey/medium.jpeg"} alt="medium" className={`img-fluid img-thumbnail ${isMediumClicked ? "opacity" : ""}`} onClick={handleMediumClicked} />
                        <p className={`mt-2 ${isMediumClicked ? "text-muted" : ""}`}>Medium</p>
                        <i className={`fas fa-check position-absolute ${isMediumClicked ? "sizes-clicked" : "d-none"}`} />
                    </div>
                    <div className="position-relative mr-2">
                        <img src={"/static/img/survey/large.jpeg"} alt="large" className={`img-fluid img-thumbnail ${isLargeClicked ? "opacity" : ""}`} onClick={handleLargeClicked} />
                        <p className={`mt-2 ${isLargeClicked ? "text-muted" : ""}`}>Large</p>
                        <i className={`fas fa-check position-absolute ${isLargeClicked ? "sizes-clicked" : "d-none"}`} />
                    </div>
                    <div className="position-relative">
                        <img src={"/static/img/survey/oversize.jpeg"} alt="oversize" className={`img-fluid img-thumbnail ${isOversizeClicked ? "opacity" : ""}`} onClick={handleOversizeClicked} />
                        <p className={`mt-2 ${isOversizeClicked ? "text-muted" : ""}`}>Oversize</p>
                        <i className={`fas fa-check position-absolute ${isOversizeClicked ? "sizes-clicked" : "d-none"}`} />
                    </div>
                </div>
                <div className="d-flex justify-content-between">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackFifth}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextFifth}>next</button>
                </div>
            </div>
            <div className={displaySixth}>
                <h3 className="h5 mb-4">Your Budget:</h3>
                <p>I am comfortable spending up to</p>
                <form onChange={handleBudget}>
                    <label htmlFor="budget" className="d-block">Enter Budget* (USD$)</label>
                    <input type="number" min="1000" id="budget" placeholder="1000" className="pl-3 pr-4 pt-2 pb-2 mb-3" />
                </form>
                <p className={budgetErrorMessage ? "alert alert-warning" : "d-none"}>Please enter an amount of $1000 or greater</p>
                <div className="d-flex justify-content-between w-50 m-auto">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackSixth}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextSixth}>next</button>
                </div>
            </div>
            <div className={displaySeventh}>
                <h3 className="h5 mb-4">You are almost done. Please complete the fields below:</h3>
                <form>
                    <div className="d-flex flex-wrap justify-content-around mb-4">
                        <div>
                            <label htmlFor="first-name" className="d-block">First Name*</label>
                            <input type="text" id="first-name" maxLength="50" required className={`pl-3 pr-4 pt-2 pb-2 ${!firstNameErrorMessage ? "mb-4 mb-md-0" : ""}`} onChange={handleFirstName} />
                            <p className={firstNameErrorMessage ? "alert alert-warning mt-3" : "d-none"}>Please enter at least 2 characters</p>
                        </div>
                        <div>
                            <label htmlFor="last-name" className="d-block">Last Name*</label>
                            <input type="text" id="last-name" maxLength="50" required className="pl-3 pr-4 pt-2 pb-2" onChange={handleLastName} />
                            <p className={lastNameErrorMessage ? "alert alert-warning mt-3 mb-0" : "d-none"}>Please enter at least 2 characters</p>
                        </div>
                    </div>
                    <div className="d-flex flex-wrap justify-content-around mb-4">
                        <div>
                            <label htmlFor="email" className="d-block">Email*</label>
                            <input type="email" id="email" required maxLength="50" className={`pl-3 pr-4 pt-2 pb-2 ${!emailErrorMessage ? "mb-4 mb-md-0" : ""}`} onChange={handleEmail} />
                            <p className={emailErrorMessage ? "alert alert-warning mt-3" : "d-none"}>Please enter a valid email</p>
                        </div>
                        <div>
                            <label htmlFor="phone" className="d-block">Phone (optional)</label>
                            <input type="tel" id="phone" placeholder="123-456-7890" className="pl-3 pr-4 pt-2 pb-2" onChange={handlePhone} />
                            <p className={phoneErrorMessage ? "alert alert-warning mt-3" : "d-none"}>Please enter a valid phone number</p>
                        </div>
                    </div>
                </form>
                <div className="d-flex justify-content-between w-75 m-auto">
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickBackSeventh}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase" onClick={handleClickNextSeventh}>next</button>
                </div>
            </div>
            <div className={displayEighth}>
                <p className="w-75 m-auto pb-3 text">Is there anything else you want your personal art advisor to know about the artwork you're searching for (e.g. colours, inspirations, or artists you love)? Feel free to include links to art or Pinterest boards you like.</p>
                <form>
                    <textarea rows="10" maxLength="500" placeholder="Nothing else for now." className="w-md-25 w-75 pl-3 pt-2" onChange={event => setNotes(event.target.value)} />
                    <div className="form-check text-left w-75 m-auto pt-3">
                        <input className="form-check-input" type="checkbox" id="newsletter-subscription" defaultChecked="true" onChange={event => setNewsletterSubscription(event.target.checked)} />
                        <label className="form-check-label" htmlFor="newsletter-subscription">Subscribe to Our Newsletter</label>
                    </div>
                </form>
                {/* <p className="text-left w-75 m-auto pt-4 text">Optional: share a picture of the place you want to put your new artwork.</p>
                <form className="w-50 m-auto">
                    <label htmlFor="image-upload" className="btn btn-outline-dark mt-4 mb-4">Add Image</label>
                    <input type="file" id="image-upload" accept="image/*" className="d-block m-auto" onChange={event => setImageFile(event.target.files)} />
                </form> */}
                <div className="d-flex justify-content-between w-75 m-auto">
                    <button type="button" className="btn btn-dark text-uppercase mt-4" onClick={handleClickBackEighth}>back</button>
                    <button type="button" className="btn btn-dark text-uppercase mt-4" onClick={handleClickNextEighth}>submit request</button>
                </div>
            </div>
            <div className={endSurvey}>
                {!isErrorMessage ?
                (<div>
                    <p className="h3 font-weight-bold">Thank you!</p>
                    <p className="w-75 m-auto pb-3">In 4-5 business days, your personal art advisor will send you with a handpicked selection of pieces for you to consider. Feel free to explore some original art in the meantime.</p>
                    <a href="/art/search/art/all" className="btn btn-dark">Browse All Artworks</a>
                </div>) : 
                (<div>
                    <p className="w-75 m-auto pb-3 text-danger">{errorMessage}</p>
                    <a href="/art/search/art/all" className="btn btn-dark">Browse All Artworks</a>
                </div>
                )}
            </div>
        </section>
    )
}