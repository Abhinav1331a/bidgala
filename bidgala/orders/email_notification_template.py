from django.conf import settings


def orderAcceptedTemplate(name, productName, ownerID):
  BASE_URL = settings.HOST_BASE_URL
  CHAT_URL = BASE_URL + 'messages/' + str(ownerID)

  email_template = """ 
      
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
      <head>
        <meta charset="utf-8"> <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->
        <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">
        <!-- CSS Reset : BEGIN -->
        <style>
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: #f1f1f1;
        }
        /* What it does: Stops email clients resizing small text. */
        * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
        }
        /* What it does: Centers email on Android 4.4 */
        div[style*="margin: 16px 0"] {
        margin: 0 !important;
        }
        /* What it does: Stops Outlook from adding extra spacing to tables. */
        table,
        td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
        }
        /* What it does: Fixes webkit padding issue. */
        table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        margin: 0 auto !important;
        }
        /* What it does: Uses a better rendering method when resizing images in IE. */
        img {
        -ms-interpolation-mode:bicubic;
        }
        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
        text-decoration: none;
        }
        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],  /* iOS */
        .unstyle-auto-detected-links *,
        .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        }
        /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
        .a6S {
        display: none !important;
        opacity: 0.01 !important;
        }
        /* What it does: Prevents Gmail from changing the text color in conversation threads. */
        .im {
        color: inherit !important;
        }
        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img + div {
        display: none !important;
        }
        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */
        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
        u ~ div .email-container {
        min-width: 320px !important;
        }
        }
        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        u ~ div .email-container {
        min-width: 375px !important;
        }
        }
        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
        u ~ div .email-container {
        min-width: 414px !important;
        }
        }
        </style>
        <!-- CSS Reset : END -->
        <!-- Progressive Enhancements : BEGIN -->
        <style>
          .primary{
          background: #17bebb;
        }
        .bg_white{
          background: #ffffff;
        }
        .bg_light{
          background: #f7fafa;
        }
        .bg_black{
          background: #000000;
        }
        .bg_dark{
          background: rgba(0,0,0,.8);
        }
        .email-section{
          padding:2.5em;
        }
        /*BUTTON*/
        .btn{
          padding: 10px 15px;
          display: inline-block;
        }
        .btn.btn-primary{
          border-radius: 5px;
          background: #17bebb;
          color: #ffffff;
        }
        .btn.btn-white{
          border-radius: 5px;
          background: #ffffff;
          color: #000000;
        }
        .btn.btn-white-outline{
          border-radius: 5px;
          background: transparent;
          border: 1px solid #fff;
          color: #fff;
        }
        .btn.btn-black-outline{
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
        .btn-custom{
          color: rgba(0,0,0,.3);
          text-decoration: underline;
        }
        h1,h2,h3,h4,h5,h6{
          font-family: 'Work Sans', sans-serif;
          color: #000000;
          margin-top: 0;
          font-weight: 400;
        }
        body{
          font-family: 'Work Sans', sans-serif;
          font-weight: 400;
          font-size: 15px;
          line-height: 1.8;
          color: rgba(0,0,0,.4);
        }
        a{
          color: #17bebb;
        }
        table{
        }
        /*LOGO*/
        .logo h1{
          margin: 0;
        }
        .logo h1 a{
          color: #000000;
          font-size: 24px;
          font-weight: 700;
          font-family: 'Work Sans', sans-serif;
        }
        /*HERO*/
        .hero{
          position: relative;
          z-index: 0;
        }
        .hero .text{
          color: rgba(0,0,0,.3);
        }
        .hero .text h2{
          color: #000;
          font-size: 34px;
          margin-bottom: 15px;
          font-weight: 300;
          line-height: 1.2;
        }
        .hero .text h3{
          font-size: 24px;
          font-weight: 200;
        }
        .hero .text h2 span{
          font-weight: 600;
          color: #000;
        }
        /*PRODUCT*/
        .product-entry{
          display: block;
          position: relative;
          float: left;
          padding-top: 20px;
        }
        .product-entry .text{
          width: calc(100% - 125px);
          padding-left: 20px;
        }
        .product-entry .text h3{
          margin-bottom: 0;
          padding-bottom: 0;
        }
        .product-entry .text p{
          margin-top: 0;
        }
        .product-entry img, .product-entry .text{
          float: left;
        }
        ul.social{
          padding: 0;
        }
        ul.social li{
          display: inline-block;
          margin-right: 10px;
        }
        /*FOOTER*/
        .footer{
          border-top: 1px solid rgba(0,0,0,.05);
          color: rgba(0,0,0,.5);
        }
        .footer .heading{
          color: #000;
          font-size: 20px;
        }
        .footer ul{
          margin: 0;
          padding: 0;
        }
        .footer ul li{
          list-style: none;
          margin-bottom: 10px;
        }
        .footer ul li a{
          color: rgba(0,0,0,1);
        }
        @media screen and (max-width: 500px) {
        }
        </style>
      </head>
      <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
        <center style="width: 100%; background-color: #f1f1f1;">
        <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
          &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
          <!-- BEGIN BODY -->
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
            <tr>
              <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td class="logo">
                      
                       <img src='cid:logo' style="width:25%; height: 3.2%">
                    </td>
                  </tr>
                </table>
              </td>
              </tr><!-- end tr -->
              <tr>
                <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td style="padding: 0 2.5em; background-color: #fff;">

                        <div class="text">

                          <p style="color: #000">Dear """ + name + """,</p>
                          <p style="color: #000">Your purchase request for  """ + productName +  """ is accepted. You will receive the tracking number shortly provided by the artist.</p>

                          <p style="color: #000">If there's anything you need to know about the purchase, please don't hesitate to contact the <a href='""" + CHAT_URL + """'>artist</a>

                          </p>
                          
                          
                        </div>
                      </td>
                    </tr>
                    
                  </table>
                </td>
                </tr><!-- end tr -->
                
                <tr>
                  <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                      
                    
    
                <tr>
                  <table class="bg_white" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    
                    
                  </table>
                  </tr><!-- end tr -->
                  <!-- 1 Column Text + Button : END -->
                </table>
                <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
                 
                    <tr>
                      <td class="bg_white" style="text-align: center;">
                        <p style="margin: 0px; padding: 0px">Add us to your address book:</p>
                        <p style="margin: 0px; padding: 0px">info@thebidgala.com</p>
                        <br/>
                      </td>
                    </tr>
                  </table>
                </div>
                </center>
              </body>
            </html>

      """
  return email_template




def orderDeclinedTemplate(name, productName, ownerID):
  BASE_URL = settings.HOST_BASE_URL
  CHAT_URL = BASE_URL + 'messages/' + str(ownerID)

  email_template = """ 
      
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
      <head>
        <meta charset="utf-8"> <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->
        <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">
        <!-- CSS Reset : BEGIN -->
        <style>
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: #f1f1f1;
        }
        /* What it does: Stops email clients resizing small text. */
        * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
        }
        /* What it does: Centers email on Android 4.4 */
        div[style*="margin: 16px 0"] {
        margin: 0 !important;
        }
        /* What it does: Stops Outlook from adding extra spacing to tables. */
        table,
        td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
        }
        /* What it does: Fixes webkit padding issue. */
        table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        margin: 0 auto !important;
        }
        /* What it does: Uses a better rendering method when resizing images in IE. */
        img {
        -ms-interpolation-mode:bicubic;
        }
        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
        text-decoration: none;
        }
        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],  /* iOS */
        .unstyle-auto-detected-links *,
        .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        }
        /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
        .a6S {
        display: none !important;
        opacity: 0.01 !important;
        }
        /* What it does: Prevents Gmail from changing the text color in conversation threads. */
        .im {
        color: inherit !important;
        }
        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img + div {
        display: none !important;
        }
        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */
        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
        u ~ div .email-container {
        min-width: 320px !important;
        }
        }
        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        u ~ div .email-container {
        min-width: 375px !important;
        }
        }
        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
        u ~ div .email-container {
        min-width: 414px !important;
        }
        }
        </style>
        <!-- CSS Reset : END -->
        <!-- Progressive Enhancements : BEGIN -->
        <style>
          .primary{
          background: #17bebb;
        }
        .bg_white{
          background: #ffffff;
        }
        .bg_light{
          background: #f7fafa;
        }
        .bg_black{
          background: #000000;
        }
        .bg_dark{
          background: rgba(0,0,0,.8);
        }
        .email-section{
          padding:2.5em;
        }
        /*BUTTON*/
        .btn{
          padding: 10px 15px;
          display: inline-block;
        }
        .btn.btn-primary{
          border-radius: 5px;
          background: #17bebb;
          color: #ffffff;
        }
        .btn.btn-white{
          border-radius: 5px;
          background: #ffffff;
          color: #000000;
        }
        .btn.btn-white-outline{
          border-radius: 5px;
          background: transparent;
          border: 1px solid #fff;
          color: #fff;
        }
        .btn.btn-black-outline{
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
        .btn-custom{
          color: rgba(0,0,0,.3);
          text-decoration: underline;
        }
        h1,h2,h3,h4,h5,h6{
          font-family: 'Work Sans', sans-serif;
          color: #000000;
          margin-top: 0;
          font-weight: 400;
        }
        body{
          font-family: 'Work Sans', sans-serif;
          font-weight: 400;
          font-size: 15px;
          line-height: 1.8;
          color: rgba(0,0,0,.4);
        }
        a{
          color: #17bebb;
        }
        table{
        }
        /*LOGO*/
        .logo h1{
          margin: 0;
        }
        .logo h1 a{
          color: #000000;
          font-size: 24px;
          font-weight: 700;
          font-family: 'Work Sans', sans-serif;
        }
        /*HERO*/
        .hero{
          position: relative;
          z-index: 0;
        }
        .hero .text{
          color: rgba(0,0,0,.3);
        }
        .hero .text h2{
          color: #000;
          font-size: 34px;
          margin-bottom: 15px;
          font-weight: 300;
          line-height: 1.2;
        }
        .hero .text h3{
          font-size: 24px;
          font-weight: 200;
        }
        .hero .text h2 span{
          font-weight: 600;
          color: #000;
        }
        /*PRODUCT*/
        .product-entry{
          display: block;
          position: relative;
          float: left;
          padding-top: 20px;
        }
        .product-entry .text{
          width: calc(100% - 125px);
          padding-left: 20px;
        }
        .product-entry .text h3{
          margin-bottom: 0;
          padding-bottom: 0;
        }
        .product-entry .text p{
          margin-top: 0;
        }
        .product-entry img, .product-entry .text{
          float: left;
        }
        ul.social{
          padding: 0;
        }
        ul.social li{
          display: inline-block;
          margin-right: 10px;
        }
        /*FOOTER*/
        .footer{
          border-top: 1px solid rgba(0,0,0,.05);
          color: rgba(0,0,0,.5);
        }
        .footer .heading{
          color: #000;
          font-size: 20px;
        }
        .footer ul{
          margin: 0;
          padding: 0;
        }
        .footer ul li{
          list-style: none;
          margin-bottom: 10px;
        }
        .footer ul li a{
          color: rgba(0,0,0,1);
        }
        @media screen and (max-width: 500px) {
        }
        </style>
      </head>
      <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
        <center style="width: 100%; background-color: #f1f1f1;">
        <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
          &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
          <!-- BEGIN BODY -->
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
            <tr>
              <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td class="logo">
                      
                       <img src='cid:logo' style="width:25%; height: 3.2%">
                    </td>
                  </tr>
                </table>
              </td>
              </tr><!-- end tr -->
              <tr>
                <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td style="padding: 0 2.5em; background-color: #fff;">

                        <div class="text">

                          <p style="color: #000">Dear """ + name + """,</p>
                          <p style="color: #000">Your purchase request for  """ + productName +  """ is declined.</p>

                          <p style="color: #000">If there's anything you need to know about the purchase, please don't hesitate to contact the <a href='""" + CHAT_URL + """'>artist</a>

                          </p>
                          
                          
                        </div>
                      </td>
                    </tr>
                    
                  </table>
                </td>
                </tr><!-- end tr -->
                
                <tr>
                  <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                      
                    
    
                <tr>
                  <table class="bg_white" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    
                    
                  </table>
                  </tr><!-- end tr -->
                  <!-- 1 Column Text + Button : END -->
                </table>
                <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
                 
                    <tr>
                      <td class="bg_white" style="text-align: center;">
                        <p style="margin: 0px; padding: 0px">Add us to your address book:</p>
                        <p style="margin: 0px; padding: 0px">info@thebidgala.com</p>
                        <br/>
                      </td>
                    </tr>
                  </table>
                </div>
                </center>
              </body>
            </html>

      """
  return email_template



def trackingNumberTemplate(name, productName, ownerID, trackingID):
  BASE_URL = settings.HOST_BASE_URL
  CHAT_URL = BASE_URL + 'messages/' + str(ownerID)

  email_template = """ 
      
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
      <head>
        <meta charset="utf-8"> <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->
        <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">
        <!-- CSS Reset : BEGIN -->
        <style>
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: #f1f1f1;
        }
        /* What it does: Stops email clients resizing small text. */
        * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
        }
        /* What it does: Centers email on Android 4.4 */
        div[style*="margin: 16px 0"] {
        margin: 0 !important;
        }
        /* What it does: Stops Outlook from adding extra spacing to tables. */
        table,
        td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
        }
        /* What it does: Fixes webkit padding issue. */
        table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        margin: 0 auto !important;
        }
        /* What it does: Uses a better rendering method when resizing images in IE. */
        img {
        -ms-interpolation-mode:bicubic;
        }
        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
        text-decoration: none;
        }
        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],  /* iOS */
        .unstyle-auto-detected-links *,
        .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        }
        /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
        .a6S {
        display: none !important;
        opacity: 0.01 !important;
        }
        /* What it does: Prevents Gmail from changing the text color in conversation threads. */
        .im {
        color: inherit !important;
        }
        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img + div {
        display: none !important;
        }
        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */
        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
        u ~ div .email-container {
        min-width: 320px !important;
        }
        }
        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        u ~ div .email-container {
        min-width: 375px !important;
        }
        }
        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
        u ~ div .email-container {
        min-width: 414px !important;
        }
        }
        </style>
        <!-- CSS Reset : END -->
        <!-- Progressive Enhancements : BEGIN -->
        <style>
          .primary{
          background: #17bebb;
        }
        .bg_white{
          background: #ffffff;
        }
        .bg_light{
          background: #f7fafa;
        }
        .bg_black{
          background: #000000;
        }
        .bg_dark{
          background: rgba(0,0,0,.8);
        }
        .email-section{
          padding:2.5em;
        }
        /*BUTTON*/
        .btn{
          padding: 10px 15px;
          display: inline-block;
        }
        .btn.btn-primary{
          border-radius: 5px;
          background: #17bebb;
          color: #ffffff;
        }
        .btn.btn-white{
          border-radius: 5px;
          background: #ffffff;
          color: #000000;
        }
        .btn.btn-white-outline{
          border-radius: 5px;
          background: transparent;
          border: 1px solid #fff;
          color: #fff;
        }
        .btn.btn-black-outline{
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
        .btn-custom{
          color: rgba(0,0,0,.3);
          text-decoration: underline;
        }
        h1,h2,h3,h4,h5,h6{
          font-family: 'Work Sans', sans-serif;
          color: #000000;
          margin-top: 0;
          font-weight: 400;
        }
        body{
          font-family: 'Work Sans', sans-serif;
          font-weight: 400;
          font-size: 15px;
          line-height: 1.8;
          color: rgba(0,0,0,.4);
        }
        a{
          color: #17bebb;
        }
        table{
        }
        /*LOGO*/
        .logo h1{
          margin: 0;
        }
        .logo h1 a{
          color: #000000;
          font-size: 24px;
          font-weight: 700;
          font-family: 'Work Sans', sans-serif;
        }
        /*HERO*/
        .hero{
          position: relative;
          z-index: 0;
        }
        .hero .text{
          color: rgba(0,0,0,.3);
        }
        .hero .text h2{
          color: #000;
          font-size: 34px;
          margin-bottom: 15px;
          font-weight: 300;
          line-height: 1.2;
        }
        .hero .text h3{
          font-size: 24px;
          font-weight: 200;
        }
        .hero .text h2 span{
          font-weight: 600;
          color: #000;
        }
        /*PRODUCT*/
        .product-entry{
          display: block;
          position: relative;
          float: left;
          padding-top: 20px;
        }
        .product-entry .text{
          width: calc(100% - 125px);
          padding-left: 20px;
        }
        .product-entry .text h3{
          margin-bottom: 0;
          padding-bottom: 0;
        }
        .product-entry .text p{
          margin-top: 0;
        }
        .product-entry img, .product-entry .text{
          float: left;
        }
        ul.social{
          padding: 0;
        }
        ul.social li{
          display: inline-block;
          margin-right: 10px;
        }
        /*FOOTER*/
        .footer{
          border-top: 1px solid rgba(0,0,0,.05);
          color: rgba(0,0,0,.5);
        }
        .footer .heading{
          color: #000;
          font-size: 20px;
        }
        .footer ul{
          margin: 0;
          padding: 0;
        }
        .footer ul li{
          list-style: none;
          margin-bottom: 10px;
        }
        .footer ul li a{
          color: rgba(0,0,0,1);
        }
        @media screen and (max-width: 500px) {
        }
        </style>
      </head>
      <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
        <center style="width: 100%; background-color: #f1f1f1;">
        <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
          &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
          <!-- BEGIN BODY -->
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
            <tr>
              <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td class="logo">
                      
                       <img src='cid:logo' style="width:25%; height: 3.2%">
                    </td>
                  </tr>
                </table>
              </td>
              </tr><!-- end tr -->
              <tr>
                <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td style="padding: 0 2.5em; background-color: #fff;">

                        <div class="text">

                          <p style="color: #000">Dear """ + name + """,</p>
                          <p style="color: #000">Your tracking number for  """ + productName +  """ is <a style='color:#0275d8' href='https://bidgala.aftership.com/""" +trackingID+"""'>"""+trackingID +"""</a>.</p>

                          <p style="color: #000">If there's anything you need to know about the purchase, please don't hesitate to contact the <a href='""" + CHAT_URL + """'>artist</a>

                          </p>
                          
                          
                        </div>
                      </td>
                    </tr>
                    
                  </table>
                </td>
                </tr><!-- end tr -->
                
                <tr>
                  <td valign="middle" class="hero bg_white" style="padding: 2em 0 2em 0;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                      
                    
    
                <tr>
                  <table class="bg_white" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    
                    
                  </table>
                  </tr><!-- end tr -->
                  <!-- 1 Column Text + Button : END -->
                </table>
                <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
                 
                    <tr>
                      <td class="bg_white" style="text-align: center;">
                        <p style="margin: 0px; padding: 0px">Add us to your address book:</p>
                        <p style="margin: 0px; padding: 0px">info@bidgala.com</p>
                        <br/>
                      </td>
                    </tr>
                  </table>
                </div>
                </center>
              </body>
            </html>

      """
  return email_template


def order_confirmation_receipt(name, product_name, address, order_id, date, total):
  email_template = """ 
  <!doctype html>
    <html class="no-js" lang="">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="x-ua-compatible" content="ie=edge">
            <style type="text/css">
              .top_rw{ background-color:#f4f4f4; }
      .td_w{ }
      button{ padding:5px 10px; font-size:14px;}
        .invoice-box {
            max-width: 890px;
            margin: auto;
            padding:10px;
            border: 1px solid #eee;
            box-shadow: 0 0 10px rgba(0, 0, 0, .15);
            font-size: 14px;
            line-height: 24px;
            font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            color: #555;
        }
        .invoice-box table {
            width: 100%;
            line-height: inherit;
            text-align: left;
        border-bottom: solid 1px #ccc;
        }
        .invoice-box table td {
            padding: 5px;
            vertical-align:middle;
        }
        .invoice-box table tr td:nth-child(2) {
            text-align: right;
        }
        .invoice-box table tr.top table td {
            padding-bottom: 20px;
        }
        .invoice-box table tr.top table td.title {
            font-size: 45px;
            line-height: 45px;
            color: #333;
        }
        .invoice-box table tr.information table td {
            padding-bottom: 40px;
        }
        .invoice-box table tr.heading td {
            background: #eee;
            border-bottom: 1px solid #ddd;
            font-weight: bold;
        font-size:12px;
        }
        .invoice-box table tr.details td {
            padding-bottom: 20px;
        }
        .invoice-box table tr.item td{
            border-bottom: 1px solid #eee;
        }
        .invoice-box table tr.item.last td {
            border-bottom: none;
        }
        .invoice-box table tr.total td:nth-child(2) {
            border-top: 2px solid #eee;
            font-weight: bold;
        }
        @media only screen and (max-width: 600px) {
            .invoice-box table tr.top table td {
                width: 100%;
                display: block;
                text-align: center;
            }
            .invoice-box table tr.information table td {
                width: 100%;
                display: block;
                text-align: center;
            }
        }
        /** RTL **/
        .rtl {
            direction: rtl;
            font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        }
        .rtl table {
            text-align: right;
        }
        .rtl table tr td:nth-child(2) {
            text-align: left;
        }
            </style>
           
        </head>
        <body>
            
        <div class="invoice-box">
            <table cellpadding="0" cellspacing="0">
        <tr class="top_rw">
           <td colspan="2">
              <h2 style="margin-bottom: 0px;"> Order Confirmation </h2>
            <span style=""> Order Number: """+order_id+""" Date: """+date+""" </span>
           </td>
            
        </tr>
                <tr class="top">
                    <td colspan="3">
                        <table>
                            <tr>
                                <td>
                  Dear <b>""" +name+ """</b>,<br>
                  Thank you for shopping at BIDGALA. Please allow the artist 5 business days to package your artwork safely and submit a tracking number. Once it's been processed, you'll receive a shipment confirmation email with your order's tracking number.

                  <br>
                  <br>

                  Below, you'll find a copy of your receipt and order information. Please keep it for your records.

                  <br>
                  <br>

                  If you have any questions regarding your order, please <b>contact us</b> at <b>info@thebidgala.com</b>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="information">
                      <td colspan="3">
                        <table>
                            <tr>
                                <td colspan="2">
                  <b> Shipping Address </b> <br>
                                    """ + address +"""
            
                                </td>
                                <td> <b> Billing Address:</b><br>
                                    """ + address +"""
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                                <td colspan="3">
                <table cellspacing="0px" cellpadding="2px">
                <tr class="heading">
                    <td style="width:25%;">
                        ITEM
                    </td>
            
                    <td style="width:10%; text-align:right;">
                        TOTAL PRICE (USD)
                    </td>
            
            
             
                </tr>
          <tr class="item">
                   <td style="width:25%;">
                        """ + product_name + """
                    </td>
            
                    <td style="width:10%; text-align:right;">
                        """ + total + """$""" + """
                    </td>
             
            
            
                </tr>
          
                </td>
          </table>
                
          
            </table>
        </div>


        </body>
</html>"""
  return email_template
