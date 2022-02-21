var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var Survey = function Survey() {
    var _React$useState = React.useState(''),
        _React$useState2 = _slicedToArray(_React$useState, 2),
        startSurvey = _React$useState2[0],
        setStartSurvey = _React$useState2[1];

    var _React$useState3 = React.useState('d-none'),
        _React$useState4 = _slicedToArray(_React$useState3, 2),
        displayFirst = _React$useState4[0],
        setDisplayFirst = _React$useState4[1];

    var _React$useState5 = React.useState('d-none'),
        _React$useState6 = _slicedToArray(_React$useState5, 2),
        displaySecond = _React$useState6[0],
        setDisplaySecond = _React$useState6[1];

    var _React$useState7 = React.useState('d-none'),
        _React$useState8 = _slicedToArray(_React$useState7, 2),
        displayThird = _React$useState8[0],
        setDisplayThird = _React$useState8[1];

    var _React$useState9 = React.useState('d-none'),
        _React$useState10 = _slicedToArray(_React$useState9, 2),
        displayFourth = _React$useState10[0],
        setDisplayFourth = _React$useState10[1];

    var _React$useState11 = React.useState('d-none'),
        _React$useState12 = _slicedToArray(_React$useState11, 2),
        displayFifth = _React$useState12[0],
        setDisplayFifth = _React$useState12[1];

    var _React$useState13 = React.useState('d-none'),
        _React$useState14 = _slicedToArray(_React$useState13, 2),
        displaySixth = _React$useState14[0],
        setDisplaySixth = _React$useState14[1];

    var _React$useState15 = React.useState('d-none'),
        _React$useState16 = _slicedToArray(_React$useState15, 2),
        displaySeventh = _React$useState16[0],
        setDisplaySeventh = _React$useState16[1];

    var _React$useState17 = React.useState('d-none'),
        _React$useState18 = _slicedToArray(_React$useState17, 2),
        displayEighth = _React$useState18[0],
        setDisplayEighth = _React$useState18[1];

    var _React$useState19 = React.useState('d-none'),
        _React$useState20 = _slicedToArray(_React$useState19, 2),
        endSurvey = _React$useState20[0],
        setEndSurvey = _React$useState20[1];

    var _React$useState21 = React.useState(null),
        _React$useState22 = _slicedToArray(_React$useState21, 2),
        categoryResponse = _React$useState22[0],
        setCategoryResponse = _React$useState22[1];

    var _React$useState23 = React.useState(0),
        _React$useState24 = _slicedToArray(_React$useState23, 2),
        categorySelectionCount = _React$useState24[0],
        setCategorySelectionCount = _React$useState24[1];

    var _React$useState25 = React.useState(false),
        _React$useState26 = _slicedToArray(_React$useState25, 2),
        categoryErrorMessage = _React$useState26[0],
        setCategoryErrorMessage = _React$useState26[1];

    var _React$useState27 = React.useState({}),
        _React$useState28 = _slicedToArray(_React$useState27, 2),
        userCategorySelection = _React$useState28[0],
        setUserCategorySelection = _React$useState28[1];

    var _React$useState29 = React.useState(null),
        _React$useState30 = _slicedToArray(_React$useState29, 2),
        userStylesResponse = _React$useState30[0],
        setUserStylesResponse = _React$useState30[1];

    var _React$useState31 = React.useState(0),
        _React$useState32 = _slicedToArray(_React$useState31, 2),
        userStylesSelectionCount = _React$useState32[0],
        setUserStylesSelectionCount = _React$useState32[1];

    var _React$useState33 = React.useState(false),
        _React$useState34 = _slicedToArray(_React$useState33, 2),
        userStylesErrorMessage = _React$useState34[0],
        setUserStylesErrorMessage = _React$useState34[1];

    var _React$useState35 = React.useState({}),
        _React$useState36 = _slicedToArray(_React$useState35, 2),
        userStylesSelection = _React$useState36[0],
        setUserStylesSelection = _React$useState36[1];

    var _React$useState37 = React.useState(null),
        _React$useState38 = _slicedToArray(_React$useState37, 2),
        userPreferenceResponse = _React$useState38[0],
        setUserPreferenceResponse = _React$useState38[1];

    var _React$useState39 = React.useState(0),
        _React$useState40 = _slicedToArray(_React$useState39, 2),
        userPreferenceSelectionCount = _React$useState40[0],
        setUserPreferenceSelectionCount = _React$useState40[1];

    var _React$useState41 = React.useState(false),
        _React$useState42 = _slicedToArray(_React$useState41, 2),
        userPreferenceErrorMessage = _React$useState42[0],
        setUserPreferenceErrorMessage = _React$useState42[1];

    var _React$useState43 = React.useState({}),
        _React$useState44 = _slicedToArray(_React$useState43, 2),
        userPreferenceSelection = _React$useState44[0],
        setUserPreferenceSelection = _React$useState44[1];

    var _React$useState45 = React.useState(false),
        _React$useState46 = _slicedToArray(_React$useState45, 2),
        isHorizontalClicked = _React$useState46[0],
        setIsHorizontalClicked = _React$useState46[1];

    var _React$useState47 = React.useState(false),
        _React$useState48 = _slicedToArray(_React$useState47, 2),
        isVerticalClicked = _React$useState48[0],
        setIsVerticalClicked = _React$useState48[1];

    var _React$useState49 = React.useState(false),
        _React$useState50 = _slicedToArray(_React$useState49, 2),
        isSquareClicked = _React$useState50[0],
        setIsSquareClicked = _React$useState50[1];

    var _React$useState51 = React.useState({}),
        _React$useState52 = _slicedToArray(_React$useState51, 2),
        orientationSelected = _React$useState52[0],
        setOrientationSelected = _React$useState52[1];

    var _React$useState53 = React.useState(false),
        _React$useState54 = _slicedToArray(_React$useState53, 2),
        isSmallClicked = _React$useState54[0],
        setIsSmallClicked = _React$useState54[1];

    var _React$useState55 = React.useState(false),
        _React$useState56 = _slicedToArray(_React$useState55, 2),
        isMediumClicked = _React$useState56[0],
        setIsMediumClicked = _React$useState56[1];

    var _React$useState57 = React.useState(false),
        _React$useState58 = _slicedToArray(_React$useState57, 2),
        isLargeClicked = _React$useState58[0],
        setIsLargeClicked = _React$useState58[1];

    var _React$useState59 = React.useState(false),
        _React$useState60 = _slicedToArray(_React$useState59, 2),
        isOversizeClicked = _React$useState60[0],
        setIsOversizeClicked = _React$useState60[1];

    var _React$useState61 = React.useState({}),
        _React$useState62 = _slicedToArray(_React$useState61, 2),
        sizesSelected = _React$useState62[0],
        setSizesSelected = _React$useState62[1];

    var _React$useState63 = React.useState(0),
        _React$useState64 = _slicedToArray(_React$useState63, 2),
        budget = _React$useState64[0],
        setBudget = _React$useState64[1];

    var _React$useState65 = React.useState(false),
        _React$useState66 = _slicedToArray(_React$useState65, 2),
        budgetErrorMessage = _React$useState66[0],
        setBudgetErrorMessage = _React$useState66[1];

    var _React$useState67 = React.useState(''),
        _React$useState68 = _slicedToArray(_React$useState67, 2),
        firstName = _React$useState68[0],
        setFirstName = _React$useState68[1];

    var _React$useState69 = React.useState(false),
        _React$useState70 = _slicedToArray(_React$useState69, 2),
        firstNameErrorMessage = _React$useState70[0],
        setFirstNameErrorMessage = _React$useState70[1];

    var _React$useState71 = React.useState(''),
        _React$useState72 = _slicedToArray(_React$useState71, 2),
        lastName = _React$useState72[0],
        setLastName = _React$useState72[1];

    var _React$useState73 = React.useState(false),
        _React$useState74 = _slicedToArray(_React$useState73, 2),
        lastNameErrorMessage = _React$useState74[0],
        setLastNameErrorMessage = _React$useState74[1];

    var _React$useState75 = React.useState(''),
        _React$useState76 = _slicedToArray(_React$useState75, 2),
        email = _React$useState76[0],
        setEmail = _React$useState76[1];

    var _React$useState77 = React.useState(false),
        _React$useState78 = _slicedToArray(_React$useState77, 2),
        emailErrorMessage = _React$useState78[0],
        setEmailErrorMessage = _React$useState78[1];

    var _React$useState79 = React.useState(''),
        _React$useState80 = _slicedToArray(_React$useState79, 2),
        phone = _React$useState80[0],
        setPhone = _React$useState80[1];

    var _React$useState81 = React.useState(false),
        _React$useState82 = _slicedToArray(_React$useState81, 2),
        phoneErrorMessage = _React$useState82[0],
        setPhoneErrorMessage = _React$useState82[1];

    var _React$useState83 = React.useState(''),
        _React$useState84 = _slicedToArray(_React$useState83, 2),
        notes = _React$useState84[0],
        setNotes = _React$useState84[1];

    var _React$useState85 = React.useState(true),
        _React$useState86 = _slicedToArray(_React$useState85, 2),
        newsletterSubscription = _React$useState86[0],
        setNewsletterSubscription = _React$useState86[1];
    // const [imageFile, setImageFile] = React.useState(null);

    var _React$useState87 = React.useState(false),
        _React$useState88 = _slicedToArray(_React$useState87, 2),
        isErrorMessage = _React$useState88[0],
        setIsErrorMessage = _React$useState88[1];

    var _React$useState89 = React.useState(''),
        _React$useState90 = _slicedToArray(_React$useState89, 2),
        errorMessage = _React$useState90[0],
        setErrorMessage = _React$useState90[1];

    var handleClickStart = function handleClickStart() {
        setStartSurvey('d-none');
        setDisplayFirst('');
    };

    var handleClickBackFirst = function handleClickBackFirst() {
        setStartSurvey('');
        setDisplayFirst('d-none');
    };

    var handleClickNextFirst = function handleClickNextFirst() {
        setDisplaySecond('');
        setDisplayFirst('d-none');
    };

    var handleClickBackSecond = function handleClickBackSecond() {
        setDisplayFirst('');
        setDisplaySecond('d-none');
    };

    var handleClickNextSecond = function handleClickNextSecond() {
        setDisplayThird('');
        setDisplaySecond('d-none');
    };

    var handleClickBackThird = function handleClickBackThird() {
        setDisplaySecond('');
        setDisplayThird('d-none');
    };

    var handleClickNextThird = function handleClickNextThird() {
        setDisplayFourth('');
        setDisplayThird('d-none');
    };

    var handleClickBackFourth = function handleClickBackFourth() {
        setDisplayThird('');
        setDisplayFourth('d-none');
    };

    var handleClickNextFourth = function handleClickNextFourth() {
        setDisplayFifth('');
        setDisplayFourth('d-none');
    };

    var handleClickBackFifth = function handleClickBackFifth() {
        setDisplayFourth('');
        setDisplayFifth('d-none');
    };

    var handleClickNextFifth = function handleClickNextFifth() {
        setDisplaySixth('');
        setDisplayFifth('d-none');
    };

    var handleClickBackSixth = function handleClickBackSixth() {
        setDisplayFifth('');
        setDisplaySixth('d-none');
    };

    var handleClickNextSixth = function handleClickNextSixth() {
        if (budget >= 300) {
            setDisplaySeventh('');
            setDisplaySixth('d-none');
        } else setBudgetErrorMessage(true);
    };

    var handleClickBackSeventh = function handleClickBackSeventh() {
        setDisplaySixth('');
        setDisplaySeventh('d-none');
    };

    var handleClickNextSeventh = function handleClickNextSeventh() {
        if (firstName === '' || firstNameErrorMessage) setFirstNameErrorMessage(true);else if (lastName === '' || lastNameErrorMessage) setLastNameErrorMessage(true);else if (email === '' || emailErrorMessage) setEmailErrorMessage(true);else if (!phoneErrorMessage) {
            setDisplayEighth('');
            setDisplaySeventh('d-none');
        }
    };

    var handleClickBackEighth = function handleClickBackEighth() {
        setDisplaySeventh('');
        setDisplayEighth('d-none');
    };

    var handleClickNextEighth = function handleClickNextEighth() {
        setEndSurvey('');
        setDisplayEighth('d-none');
        fetch('/survey/submit/advisory-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ categories: Object.assign({}, userCategorySelection), styles: Object.assign({}, userStylesSelection), pieces: Object.assign({}, userPreferenceSelection), orientation: Object.assign({}, orientationSelected), size: Object.assign({}, sizesSelected), budget: budget, details: { firstName: firstName, lastName: lastName, email: email, phone: phone }, additional: { notes: notes, newsletterSubscription: newsletterSubscription } })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status === 'fail') {
                setErrorMessage(data.message);
                setIsErrorMessage(true);
            }
        }).catch(function () {
            setErrorMessage("Something went wrong! Please try again later");
            setIsErrorMessage(true);
        });
    };

    var handleCategoryClicked = function handleCategoryClicked(event) {
        var category = event.currentTarget.id;
        if (categorySelectionCount < 3) {
            if (!userCategorySelection[category]) {
                setUserCategorySelection(Object.assign({}, userCategorySelection, _defineProperty({}, category, true)));
                setCategorySelectionCount(categorySelectionCount + 1);
            } else {
                setUserCategorySelection(Object.assign({}, userCategorySelection, _defineProperty({}, category, false)));
                setCategorySelectionCount(categorySelectionCount - 1);
            }
            setCategoryErrorMessage(false);
        } else if (userCategorySelection[category]) {
            setUserCategorySelection(Object.assign({}, userCategorySelection, _defineProperty({}, category, false)));
            setCategorySelectionCount(categorySelectionCount - 1);
            setCategoryErrorMessage(false);
        } else setCategoryErrorMessage(true);
    };

    var handleStyleClicked = function handleStyleClicked(event) {
        var style = event.currentTarget.id;
        if (userStylesSelectionCount < 3) {
            if (!userStylesSelection[style]) {
                setUserStylesSelection(Object.assign({}, userStylesSelection, _defineProperty({}, style, true)));
                setUserStylesSelectionCount(userStylesSelectionCount + 1);
            } else {
                setUserStylesSelection(Object.assign({}, userStylesSelection, _defineProperty({}, style, false)));
                setUserStylesSelectionCount(userStylesSelectionCount - 1);
            }
            setUserStylesErrorMessage(false);
        } else if (userStylesSelection[style]) {
            setUserStylesSelection(Object.assign({}, userStylesSelection, _defineProperty({}, style, false)));
            setUserStylesSelectionCount(userStylesSelectionCount - 1);
            setUserStylesErrorMessage(false);
        } else setUserStylesErrorMessage(true);
    };

    var handlePieceClicked = function handlePieceClicked(event) {
        var piece = event.currentTarget.id;
        if (userPreferenceSelectionCount < 3) {
            if (!userPreferenceSelection[piece]) {
                setUserPreferenceSelection(Object.assign({}, userPreferenceSelection, _defineProperty({}, piece, true)));
                setUserPreferenceSelectionCount(userPreferenceSelectionCount + 1);
            } else {
                setUserPreferenceSelection(Object.assign({}, userPreferenceSelection, _defineProperty({}, piece, false)));
                setUserPreferenceSelectionCount(userPreferenceSelectionCount - 1);
            }
            setUserPreferenceErrorMessage(false);
        } else if (userPreferenceSelection[piece]) {
            setUserPreferenceSelection(Object.assign({}, userPreferenceSelection, _defineProperty({}, piece, false)));
            setUserPreferenceSelectionCount(userPreferenceSelectionCount - 1);
            setUserPreferenceErrorMessage(false);
        } else setUserPreferenceErrorMessage(true);
    };

    var handleHorizontalClicked = function handleHorizontalClicked() {
        setIsHorizontalClicked(!isHorizontalClicked);
        if (!isHorizontalClicked) setOrientationSelected(Object.assign({}, orientationSelected, { horizontal: true }));else setOrientationSelected(Object.assign({}, orientationSelected, { horizontal: false }));
    };

    var handleVerticalClicked = function handleVerticalClicked() {
        setIsVerticalClicked(!isVerticalClicked);
        if (!isVerticalClicked) setOrientationSelected(Object.assign({}, orientationSelected, { vertical: true }));else setOrientationSelected(Object.assign({}, orientationSelected, { vertical: false }));
    };

    var handleSquareClicked = function handleSquareClicked() {
        setIsSquareClicked(!isSquareClicked);
        if (!isSquareClicked) setOrientationSelected(Object.assign({}, orientationSelected, { square: true }));else setOrientationSelected(Object.assign({}, orientationSelected, { square: false }));
    };

    var handleSmallClicked = function handleSmallClicked() {
        setIsSmallClicked(!isSmallClicked);
        if (!isSmallClicked) setSizesSelected(Object.assign({}, sizesSelected, { small: true }));else setSizesSelected(Object.assign({}, sizesSelected, { small: false }));
    };

    var handleMediumClicked = function handleMediumClicked() {
        setIsMediumClicked(!isMediumClicked);
        if (!isMediumClicked) setSizesSelected(Object.assign({}, sizesSelected, { medium: true }));else setSizesSelected(Object.assign({}, sizesSelected, { medium: false }));
    };

    var handleLargeClicked = function handleLargeClicked() {
        setIsLargeClicked(!isLargeClicked);
        if (!isLargeClicked) setSizesSelected(Object.assign({}, sizesSelected, { large: true }));else setSizesSelected(Object.assign({}, sizesSelected, { large: false }));
    };

    var handleOversizeClicked = function handleOversizeClicked() {
        setIsOversizeClicked(!isOversizeClicked);
        if (!isOversizeClicked) setSizesSelected(Object.assign({}, sizesSelected, { oversize: true }));else setSizesSelected(Object.assign({}, sizesSelected, { oversize: false }));
    };

    var handleBudget = function handleBudget(event) {
        var amount = event.target.value;
        if (amount >= 300) {
            setBudget(amount);
            setBudgetErrorMessage(false);
        } else setBudgetErrorMessage(true);
    };

    var handleFirstName = function handleFirstName(event) {
        var name = event.target.value;
        if (name.replace(/\s+/g, '').length >= 2) {
            setFirstName(name);
            setFirstNameErrorMessage(false);
        } else setFirstNameErrorMessage(true);
    };

    var handleLastName = function handleLastName(event) {
        var name = event.target.value;
        if (name.replace(/\s+/g, '').length >= 2) {
            setLastName(name);
            setLastNameErrorMessage(false);
        } else setLastNameErrorMessage(true);
    };

    var handleEmail = function handleEmail(event) {
        var email = event.target.value;
        var validEmailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (validEmailRegex.test(email)) {
            setEmail(email);
            setEmailErrorMessage(false);
        } else setEmailErrorMessage(true);
    };

    var handlePhone = function handlePhone(event) {
        var phone = event.target.value;
        var validPhoneRegex = /^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
        if (phone === '') setPhoneErrorMessage(false);else if (validPhoneRegex.test(phone)) {
            setPhone(phone);
            setPhoneErrorMessage(false);
        } else setPhoneErrorMessage(true);
    };

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    React.useEffect(function () {
        fetch('/survey/options/user-preference-category-options').then(function (res) {
            return res.json();
        }).then(function (data) {
            return setCategoryResponse(data);
        }).catch(function (error) {
            return console.error(error);
        });

        fetch('/survey/options/user-preference-options').then(function (res) {
            return res.json();
        }).then(function (data) {
            return setUserPreferenceResponse(data);
        }).catch(function (error) {
            return console.error(error);
        });

        fetch('/survey/options/user-preference-style-options').then(function (res) {
            return res.json();
        }).then(function (data) {
            return setUserStylesResponse(data);
        }).catch(function (error) {
            return console.error(error);
        });
    }, []);

    return React.createElement(
        'section',
        { className: 'survey container text-center mt-5' },
        React.createElement(
            'div',
            { className: startSurvey },
            React.createElement(
                'h2',
                { className: 'h4' },
                'Welcome to Art Advisory'
            ),
            React.createElement(
                'p',
                { className: 'w-75 m-auto pt-3 pb-4' },
                'Once you have answered a few short questions, our expert art curators will create a portfolio of art recommendations custom to your style, budget, and more. After you have completed the questionnaire, your free personal curator will send you an email with recommendations in 3-5 business days. Let\'s get started!'
            ),
            React.createElement(
                'button',
                { type: 'button', className: 'btn btn-dark', onClick: handleClickStart },
                'Start Survey'
            )
        ),
        React.createElement(
            'div',
            { className: displayFirst },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Your Preferred Categories'
            ),
            React.createElement(
                'p',
                { className: categoryErrorMessage ? "alert alert-danger" : "d-none" },
                'You may select up to 3 categories'
            ),
            React.createElement(
                'div',
                { className: 'container' },
                React.createElement(
                    'div',
                    { className: 'category-row row row-cols-1 row-cols-md-2 w-75 m-auto' },
                    categoryResponse && categoryResponse.result.map(function (category) {
                        return React.createElement(
                            'div',
                            { key: category.id, className: 'col position-relative' },
                            React.createElement('img', { src: '' + categoryResponse.img_host_url + category.image, alt: category.value, className: 'survey-img img-fluid img-thumbnail ' + (userCategorySelection[category.value] ? "opacity" : ""), id: category.value, onClick: handleCategoryClicked }),
                            React.createElement(
                                'p',
                                { className: userCategorySelection[category.value] ? "text-muted" : "" },
                                category.value
                            ),
                            React.createElement('i', { className: 'fas fa-check position-absolute ' + (userCategorySelection[category.value] ? "category-clicked" : "d-none") })
                        );
                    })
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between m-auto button-first' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackFirst },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextFirst },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displaySecond },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Select up to 3 Preferred Styles'
            ),
            React.createElement(
                'p',
                { className: userStylesErrorMessage ? "alert alert-danger" : "d-none" },
                'You may select up to 3 styles'
            ),
            React.createElement(
                'div',
                { className: 'container' },
                React.createElement(
                    'div',
                    { className: 'row row-cols-1 row-cols-md-3' },
                    userStylesResponse && userStylesResponse.result.map(function (style) {
                        return React.createElement(
                            'div',
                            { key: style.id, className: 'col position-relative' },
                            React.createElement('img', { src: '' + userStylesResponse.img_host_url + style.image, alt: style.value, className: 'survey-img img-fluid img-thumbnail ' + (userStylesSelection[style.value] ? "opacity" : ""), id: style.value, onClick: handleStyleClicked }),
                            React.createElement(
                                'p',
                                { className: userStylesSelection[style.value] ? "text-muted" : "" },
                                style.value
                            ),
                            React.createElement('i', { className: 'fas fa-check position-absolute ' + (userStylesSelection[style.value] ? "style-clicked" : "d-none") })
                        );
                    })
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between m-auto button-second' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackSecond },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextSecond },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displayThird },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Choose up to 3 Preferred Pieces'
            ),
            React.createElement(
                'p',
                { className: userPreferenceErrorMessage ? "alert alert-danger" : "d-none" },
                'You may select up to 3 pieces'
            ),
            React.createElement(
                'div',
                { className: 'container' },
                React.createElement(
                    'div',
                    { className: 'row row-cols-1 row-cols-md-3' },
                    userPreferenceResponse && userPreferenceResponse.result.map(function (piece) {
                        return React.createElement(
                            'div',
                            { key: piece.id, className: 'col position-relative' },
                            React.createElement('img', { src: '' + userPreferenceResponse.img_host_url + piece.image, alt: piece.value, className: 'survey-img img-fluid img-thumbnail ' + (userPreferenceSelection[piece.value] ? "opacity" : ""), id: piece.value, onClick: handlePieceClicked }),
                            React.createElement(
                                'p',
                                { className: userPreferenceSelection[piece.value] ? "text-muted" : "" },
                                piece.value
                            ),
                            React.createElement('i', { className: 'fas fa-check position-absolute ' + (userPreferenceSelection[piece.value] ? "piece-clicked" : "d-none") })
                        );
                    })
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackThird },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextThird },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displayFourth },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Looking for a specific orientation? Select all that apply:'
            ),
            React.createElement(
                'div',
                { className: 'd-flex flex-md-row flex-column justify-content-around mt-5 mb-4' },
                React.createElement(
                    'span',
                    { className: 'position-relative', id: 'horizontal' },
                    React.createElement('span', { className: 'horizontal d-inline-block mt-md-5 ' + (isHorizontalClicked ? "light-grey" : "grey"), onClick: handleHorizontalClicked }),
                    React.createElement(
                        'p',
                        { className: isHorizontalClicked ? "text-muted" : "" },
                        'Horizontal'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isHorizontalClicked ? "horizontal-clicked" : "d-none") })
                ),
                React.createElement(
                    'span',
                    { className: 'position-relative', id: 'vertical' },
                    React.createElement('span', { className: 'vertical d-inline-block ' + (isVerticalClicked ? "light-grey" : "grey"), onClick: handleVerticalClicked }),
                    React.createElement(
                        'p',
                        { className: isVerticalClicked ? "text-muted" : "" },
                        'Vertical'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isVerticalClicked ? "vertical-clicked" : "d-none") })
                ),
                React.createElement(
                    'span',
                    { className: 'position-relative', id: 'square' },
                    React.createElement('span', { className: 'square shadow-sm d-inline-block mt-md-5 ' + (isSquareClicked ? "light-grey" : "grey"), onClick: handleSquareClicked }),
                    React.createElement(
                        'p',
                        { className: isSquareClicked ? "text-muted" : "" },
                        'Square'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isSquareClicked ? "square-clicked" : "d-none") })
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between m-auto button-fourth' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackFourth },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextFourth },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displayFifth },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Looking for a specific size?'
            ),
            React.createElement(
                'div',
                { className: 'container-size d-flex flex-md-row flex-column' },
                React.createElement(
                    'div',
                    { className: 'position-relative mr-2' },
                    React.createElement('img', { src: "/static/img/survey/small.jpeg", alt: 'small', className: 'img-fluid img-thumbnail ' + (isSmallClicked ? "opacity" : ""), onClick: handleSmallClicked }),
                    React.createElement(
                        'p',
                        { className: 'mt-2 ' + (isSmallClicked ? "text-muted" : "") },
                        'Small'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isSmallClicked ? "sizes-clicked" : "d-none") })
                ),
                React.createElement(
                    'div',
                    { className: 'position-relative mr-2' },
                    React.createElement('img', { src: "/static/img/survey/medium.jpeg", alt: 'medium', className: 'img-fluid img-thumbnail ' + (isMediumClicked ? "opacity" : ""), onClick: handleMediumClicked }),
                    React.createElement(
                        'p',
                        { className: 'mt-2 ' + (isMediumClicked ? "text-muted" : "") },
                        'Medium'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isMediumClicked ? "sizes-clicked" : "d-none") })
                ),
                React.createElement(
                    'div',
                    { className: 'position-relative mr-2' },
                    React.createElement('img', { src: "/static/img/survey/large.jpeg", alt: 'large', className: 'img-fluid img-thumbnail ' + (isLargeClicked ? "opacity" : ""), onClick: handleLargeClicked }),
                    React.createElement(
                        'p',
                        { className: 'mt-2 ' + (isLargeClicked ? "text-muted" : "") },
                        'Large'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isLargeClicked ? "sizes-clicked" : "d-none") })
                ),
                React.createElement(
                    'div',
                    { className: 'position-relative' },
                    React.createElement('img', { src: "/static/img/survey/oversize.jpeg", alt: 'oversize', className: 'img-fluid img-thumbnail ' + (isOversizeClicked ? "opacity" : ""), onClick: handleOversizeClicked }),
                    React.createElement(
                        'p',
                        { className: 'mt-2 ' + (isOversizeClicked ? "text-muted" : "") },
                        'Oversize'
                    ),
                    React.createElement('i', { className: 'fas fa-check position-absolute ' + (isOversizeClicked ? "sizes-clicked" : "d-none") })
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackFifth },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextFifth },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displaySixth },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'Your Budget:'
            ),
            React.createElement(
                'p',
                null,
                'I am comfortable spending up to'
            ),
            React.createElement(
                'form',
                { onChange: handleBudget },
                React.createElement(
                    'label',
                    { htmlFor: 'budget', className: 'd-block' },
                    'Enter Budget* (USD)'
                ),
                React.createElement('input', { type: 'number', min: '300', id: 'budget', placeholder: '300', className: 'pl-3 pr-4 pt-2 pb-2 mb-3' })
            ),
            React.createElement(
                'p',
                { className: budgetErrorMessage ? "alert alert-warning" : "d-none" },
                'Please enter an amount of $300 or greater'
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between w-50 m-auto' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackSixth },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextSixth },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displaySeventh },
            React.createElement(
                'h3',
                { className: 'h5 mb-4' },
                'You are almost done. Please complete the fields below:'
            ),
            React.createElement(
                'form',
                null,
                React.createElement(
                    'div',
                    { className: 'd-flex flex-wrap justify-content-around mb-4' },
                    React.createElement(
                        'div',
                        null,
                        React.createElement(
                            'label',
                            { htmlFor: 'first-name', className: 'd-block' },
                            'First Name*'
                        ),
                        React.createElement('input', { type: 'text', id: 'first-name', maxLength: '50', required: true, className: 'pl-3 pr-4 pt-2 pb-2 ' + (!firstNameErrorMessage ? "mb-4 mb-md-0" : ""), onChange: handleFirstName }),
                        React.createElement(
                            'p',
                            { className: firstNameErrorMessage ? "alert alert-warning mt-3" : "d-none" },
                            'Please enter at least 2 characters'
                        )
                    ),
                    React.createElement(
                        'div',
                        null,
                        React.createElement(
                            'label',
                            { htmlFor: 'last-name', className: 'd-block' },
                            'Last Name*'
                        ),
                        React.createElement('input', { type: 'text', id: 'last-name', maxLength: '50', required: true, className: 'pl-3 pr-4 pt-2 pb-2', onChange: handleLastName }),
                        React.createElement(
                            'p',
                            { className: lastNameErrorMessage ? "alert alert-warning mt-3 mb-0" : "d-none" },
                            'Please enter at least 2 characters'
                        )
                    )
                ),
                React.createElement(
                    'div',
                    { className: 'd-flex flex-wrap justify-content-around mb-4' },
                    React.createElement(
                        'div',
                        null,
                        React.createElement(
                            'label',
                            { htmlFor: 'email', className: 'd-block' },
                            'Email*'
                        ),
                        React.createElement('input', { type: 'email', id: 'email', required: true, maxLength: '50', className: 'pl-3 pr-4 pt-2 pb-2 ' + (!emailErrorMessage ? "mb-4 mb-md-0" : ""), onChange: handleEmail }),
                        React.createElement(
                            'p',
                            { className: emailErrorMessage ? "alert alert-warning mt-3" : "d-none" },
                            'Please enter a valid email'
                        )
                    ),
                    React.createElement(
                        'div',
                        null,
                        React.createElement(
                            'label',
                            { htmlFor: 'phone', className: 'd-block' },
                            'Phone (optional)'
                        ),
                        React.createElement('input', { type: 'tel', id: 'phone', placeholder: '123-456-7890', className: 'pl-3 pr-4 pt-2 pb-2', onChange: handlePhone }),
                        React.createElement(
                            'p',
                            { className: phoneErrorMessage ? "alert alert-warning mt-3" : "d-none" },
                            'Please enter a valid phone number'
                        )
                    )
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between w-75 m-auto' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickBackSeventh },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase', onClick: handleClickNextSeventh },
                    'next'
                )
            )
        ),
        React.createElement(
            'div',
            { className: displayEighth },
            React.createElement(
                'p',
                { className: 'w-75 m-auto pb-3 text' },
                'Is there anything else you want your personal art advisor to know about the artwork you\'re searching for (e.g. colours, inspirations, or artists you love)? Feel free to include links to art or Pinterest boards you like.'
            ),
            React.createElement(
                'form',
                null,
                React.createElement('textarea', { rows: '10', maxLength: '500', placeholder: 'Nothing else for now.', className: 'w-md-25 w-75 pl-3 pt-2', onChange: function onChange(event) {
                        return setNotes(event.target.value);
                    } }),
                React.createElement(
                    'div',
                    { className: 'form-check text-left w-75 m-auto pt-3' },
                    React.createElement('input', { className: 'form-check-input', type: 'checkbox', id: 'newsletter-subscription', defaultChecked: 'true', onChange: function onChange(event) {
                            return setNewsletterSubscription(event.target.checked);
                        } }),
                    React.createElement(
                        'label',
                        { className: 'form-check-label', htmlFor: 'newsletter-subscription' },
                        'Subscribe to Our Newsletter'
                    )
                )
            ),
            React.createElement(
                'div',
                { className: 'd-flex justify-content-between w-75 m-auto' },
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase mt-4', onClick: handleClickBackEighth },
                    'back'
                ),
                React.createElement(
                    'button',
                    { type: 'button', className: 'btn btn-dark text-uppercase mt-4', onClick: handleClickNextEighth },
                    'submit request'
                )
            )
        ),
        React.createElement(
            'div',
            { className: endSurvey },
            !isErrorMessage ? React.createElement(
                'div',
                null,
                React.createElement(
                    'p',
                    { className: 'h3 font-weight-bold' },
                    'Thank you!'
                ),
                React.createElement(
                    'p',
                    { className: 'w-75 m-auto pb-3' },
                    'In 4-5 business days, your personal art advisor will send you with a handpicked selection of pieces for you to consider. Feel free to explore some original art in the meantime.'
                ),
                React.createElement(
                    'a',
                    { href: '/art/search/art/all', className: 'btn btn-dark' },
                    'Browse All Artworks'
                )
            ) : React.createElement(
                'div',
                null,
                React.createElement(
                    'p',
                    { className: 'w-75 m-auto pb-3 text-danger' },
                    errorMessage
                ),
                React.createElement(
                    'a',
                    { href: '/art/search/art/all', className: 'btn btn-dark' },
                    'Browse All Artworks'
                )
            )
        )
    );
};