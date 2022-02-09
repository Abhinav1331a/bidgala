from django.conf import settings

def getEmailVerificationTemplate(confirmation_link):
  """
    This templete is used for email verification purpose.

  """
  email_template = """
        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

        <head>
          <meta charset="utf-8"> <!-- utf-8 works for most cases -->
          <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
          <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
          <title>Please verify you email address</title> <!-- The title tag shows in email notifications, like Android 4.4. -->
          <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

          <!-- CSS Reset : BEGIN -->
          <style type="text/css">
            /* What it does: Remove spaces around the email design added by some email clients. */
            /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
            html,
            body {
              margin: 0 auto !important;
              padding: 0 !important;
              height: 100% !important;
              width: 100% !important;
              background: #fff;
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
              -ms-interpolation-mode: bicubic;
            }

            /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
            a {
              text-decoration: none;
            }

            /* What it does: A work-around for email clients meddling in triggered links. */
            *[x-apple-data-detectors],
            /* iOS */
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
              color: #111 !important;
            }

            /* If the above doesn't work, add a .g-img class to any image in question. */
            img.g-img+div {
              display: none !important;
            }

            /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
            /* Create one of these media queries for each additional viewport size you'd like to fix */

            /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
            @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
              u~div .email-container {
                min-width: 320px !important;
              }
            }

            /* iPhone 6, 6S, 7, 8, and X */
            @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
              u~div .email-container {
                min-width: 375px !important;
              }
            }

            /* iPhone 6+, 7+, and 8+ */
            @media only screen and (min-device-width: 414px) {
              u~div .email-container {
                min-width: 414px !important;
              }
            }
          </style>
          <!-- Progressive Enhancements : BEGIN -->
          <style>
            .bg_white{
                background: #ffffff;
            }

            .btn{
                padding: 10px 15px;
                display: inline-block;
            }
            .btn.btn-black-outline{
                border-radius: 0px;
                background: transparent;
                border: 2px solid #000;
                color: #000;
                font-weight: 700;
            }
          </style>
        </head>

        <body>
          <center style="width: 100%; background-color: #fff;">
            <table cellpadding="0" cellspacing="0" width="600px">
              <tr>
                <td bgcolor="#fff" style="font-size: 0; line-height: 0; padding:30px 0 25px 0; border-bottom: 1px solid #f0efee; width: 100%" align="center" class="responsive-image">
                  <img src='cid:logo' width="160px" alt="bidgala-logo">
                </td>
              </tr>
              <tr>
                <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
              </tr>
              <tr>
                <td style="text-align: center; color: #111">
                  <h2 style="margin: 0"><b>Thanks for Signing Up</b></h2>
                </td>
              </tr>
              <tr>
                <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
              </tr>
            </table>
            <table cellpadding="0" cellspacing="0" width="600px">
              <tr>
                <td style="text-align: center; width: 50%;">
                    <h3 style="float:left; width:100%; font-family:'Work Sans',sans-serif; color: #000000; margin-top: 0; font-weight: 400;">(You clearly have good taste.)</h3>
                    <br />
                    <a href='https://thebidgala.com/confirmation/ """ + confirmation_link + """' class="btn btn-black-outline">ACTIVATE YOUR ACCOUNT</a>
                </td>

                <td style="text-align: center; width: 50%;">
                    <img src="cid:img1" style="width:50%;" alt="top-img">
                </td>
              </tr>
              <tr>
                <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
              </tr>
              <tr>
                <td>
                  <table cellpadding="0" cellspacing="0" align="left">
                    <tr>
                      <td style="text-align: center">
                        <img src="cid:img2" style="width:50%;" alt="bottom-img">
                      </td>
                    </tr>
                  </table>
                </td>
                <td>
                  <table cellpadding="0" cellspacing="0" align="right">
                    <tr>
                      <td style="text-align: center">
                        <h3 style="float:left; width:100%; font-family: 'Work Sans',sans-serif; color: #000000; margin-top: 0; font-weight: 400;">Our mission is to expand the fine arts market to support up-and-coming artists.</h3>
                        <br />
                        <a href="https://bidgala.com/bidgala101" class="btn btn-black-outline">BIDGALA 101</a>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
            <table cellpadding="0" cellspacing="0" width="600px">
              <tr>
                <td style="font-size: 0; line-height: 0; border-bottom: 1px solid #f0efee;" height="50px">&nbsp;</td>
              </tr>
              <tr>
                <td style="padding: 10px 0;">
                  <table cellpadding="0" cellspacing="0" align="left" width="49%">
                    <tr>
                      <td>
                        <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin" alt="linkedin-logo" style="width: 16px;"></a>
                        <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook" alt="facebook-logo" style="width: 16px;"></a>
                        <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter" alt="twitter-logo" style="width: 16px;"></a>
                        <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram" alt="instagram-logo" style="width: 16px;"></a>
                        <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest" alt="pinterest-logo" style="width: 16px;"></a>
                      </td>
                    </tr>
                  </table>
                  <table cellpadding="0" cellspacing="0" align="right" width="49%">
                    <tr>
                      <td style="text-align: right;padding-left:10px; color: #111;">
                        <p style="margin: 0;">12042142 Canada Inc.</p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td style="text-align:center">
                  <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center;">Bidgala is an online marketplace where art lovers can buy directly from artists.</p>
                  <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
                </td>
              </tr>
            </table>
          </center>
        </body>
        </html>
      """
  return email_template






def getWelcomeTemplate(name):
  email_template = """

    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <meta charset="utf-8"> <!-- utf-8 works for most cases -->
      <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
      <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
      <title>Please verify you email address</title> <!-- The title tag shows in email notifications, like Android 4.4. -->
      <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

      <!-- CSS Reset : BEGIN -->
      <style type="text/css">
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
          margin: 0 auto !important;
          padding: 0 !important;
          height: 100% !important;
          width: 100% !important;
          background: #fff;
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
          -ms-interpolation-mode: bicubic;
        }

        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
          text-decoration: none;
        }

        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],
        /* iOS */
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
          color: #111 !important;
        }

        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img+div {
          display: none !important;
        }

        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */

        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
          u~div .email-container {
            min-width: 320px !important;
          }
        }

        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
          u~div .email-container {
            min-width: 375px !important;
          }
        }

        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
          u~div .email-container {
            min-width: 414px !important;
          }
        }
      </style>
      <!-- Progressive Enhancements : BEGIN -->
      <style>
        .bg_white {
          background: #ffffff;
        }

        .btn {
          padding: 10px 15px;
          display: inline-block;
        }

        .btn.btn-black-outline {
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
      </style>
    </head>

    <body>
      <center style="width: 100%; background-color: #fff;">
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td bgcolor="#fff" style="font-size: 0; line-height: 0; padding:30px 0 25px 0; border-bottom: 1px solid #f0efee;" align="center" class="responsive-image">
              <img width="160px" src='cid:logo' alt="bidgala-logo" />
            </td>
          </tr>
          <tr>
            <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
          </tr>
          <tr>
            <td style="text-align: center; color:#111;">
              <h2 style="margin: 0"><b>Welcome to Bidgala</b></h2>
            </td>
          </tr>
          <tr>
            <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
          </tr>
        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td colspan="2" style="width:100%; color:#111;">
              <p>Dear """ + name + """,</p>
              <p>Welcome to Bidgala! We are thrilled that you've joined our art community composed of artists, consumers, and professionals alike. Bidgala is the online visual arts Community Marketplace where up and coming artists can
                sell art online directly to art buyers. Bidgala’s low art prices, variety of art, and simple web navigation help to make designing your home affordable, personalized, simple, and easy. Buy sculptures, buy photographs, buy paintings and
                more on Bidgala.
              </p>
              <p>If there's anything you need assistance with, please don't hesitate to contact us at <a href="mailto:info@thebidgala.com">info@thebidgala.com.</a>
              </p>
            </td>
          </tr>
          <tr>
            <td style="font-size: 0; line-height: 0;" height="50px">&nbsp;</td>
          </tr>
          <tr>
            <td style="width:50%; text-align: center;">
              <img src="cid:img1" style="width:50%;">
            </td>
            <td style="width:50%; text-align: center;">
              <h3 style="float:left; width:100%; font-family: 'Work Sans',sans-serif; color: #000000; margin-top: 0; font-weight: 400;">Our mission is to expand the fine arts market to support up-and-coming artists.</h3>
              <br />
              <a href="https://thebidgala.com" class="btn btn-black-outline">BIDGALA 101</a>
            </td>
          </tr>

        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td style="font-size: 0; line-height: 0; border-bottom: 1px solid #f0efee;" height="50px">&nbsp;</td>
          </tr>
          <tr>
            <td style="padding: 10px 0;">
              <table cellpadding="0" cellspacing="0" align="left" width="49%">
                <tr>
                  <td>
                    <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin/jpg;base64,<linkedin>" alt="linkedin-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook/jpg;base64,<facebook>" alt="facebook-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter/jpg;base64,<twitter>" alt="twitter-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram/jpg;base64,<instagram>" alt="instagram-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest/jpg;base64,<pinterest>" alt="pinterest-logo" style="width: 16px;"></a>
                  </td>
                </tr>
              </table>
              <table cellpadding="0" cellspacing="0" align="right" width="49%">
                <tr>
                  <td style="text-align: right;padding-left:10px; color: #111;">
                    <p style="margin: 0;">12042142 Canada Inc.</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="text-align:center">
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center;">Bidgala is an online marketplace where art lovers can buy directly from artists.</p>
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
            </td>
          </tr>
        </table>
      </center>
    </body>

    </html>

      """
  return email_template




def getWelcomeProfessionalTemplate(name):
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

                          <h3><b>Become our partner, not just a buyer! Earn 10% Commission</b></h3>

                          <p style="color: #000">Dear """ + name + """,</p>
                          <p style="color: #000"><b>We are so happy to have you as a part of our global community! Your design professional account is under review.</b><br/>We work with design professionals from around the world. If you are an interior designer, home stager, art consultant, or simply in the decorating business, our platform is designed to fit your needs.You will have the ability to purchase local art, supplement your income with 10% commission on every Bidgala purchase, gain free promotion of your services to art buyers, and refine your search criteria.<br/>For now, you are categorized as a common “Buyer”. Once your account is verified by a Bidgala team member, you will get an email notification validating you as a design professional. Verification normally takes <b>less than 5 business days</b>.
                          </p>

                          <p style="color: #000">Thank you for joining the Bidgala community!</p>

                          <p style="color: #000">Please don’t hesitate to contact us at (514)706-1818 or by emailing <a href="mailto:info@thebidgala.com">info@thebidgala.com</a>.
                          </p>

                          <p style="color: #000">Regards,<br/>Team Bidgala</p>

                        </div>
                      </td>
                    </tr>

                  </table>
                </td>
                </tr><!-- end tr -->

                </table>

                </div>
                </center>
              </body>
            </html>

      """
  return email_template





def getProfessionalConfirmTemplate(name):
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
                          <p style="color: #000">Your professional account has been verified.</p>

                          <p style="color: #000">Thank you for joining the Bidgala community! We’re happy to have you on board.</p>

                          <p style="color: #000">Please don’t hesitate to contact us at (514)706-1818 or by emailing <a href="mailto:info@bidgala.com">info@bidgala.com</a>.
                          </p>

                          <p style="color: #000">Regards,<br/>Team Bidgala</p>

                        </div>
                      </td>
                    </tr>

                  </table>
                </td>
                </tr><!-- end tr -->

                </table>

                </div>
                </center>
              </body>
            </html>

      """
  return email_template


def receiveReferralTemplate(name, link):
  email_template = """
  <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <meta charset="utf-8"> <!-- utf-8 works for most cases -->
      <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
      <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
      <title>Your Friend Has Invited You To Join Bidgala’s Art-Loving Community</title> <!-- The title tag shows in email notifications, like Android 4.4. -->
      <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

      <!-- CSS Reset : BEGIN -->
      <style type="text/css">
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
          margin: 0 auto !important;
          padding: 0 !important;
          height: 100% !important;
          width: 100% !important;
          background: #fff;
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
          -ms-interpolation-mode: bicubic;
        }

        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
          text-decoration: none;
        }

        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],
        /* iOS */
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
          color: #111 !important;
        }

        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img+div {
          display: none !important;
        }

        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */

        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
          u~div .email-container {
            min-width: 320px !important;
          }
        }

        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
          u~div .email-container {
            min-width: 375px !important;
          }
        }

        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
          u~div .email-container {
            min-width: 414px !important;
          }
        }
      </style>
      <!-- Progressive Enhancements : BEGIN -->
      <style>
        .bg_white {
          background: #ffffff;
        }

        .btn {
          padding: 10px 15px;
          display: inline-block;
        }

        .btn.btn-black-outline {
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
      </style>
    </head>

    <body>
      <center style="width: 100%; background-color: #fff;">
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td bgcolor="#fff" style="font-size: 0; line-height: 0; padding:30px 0 25px 0; border-bottom: 1px solid #f0efee;" align="center" class="responsive-image">
              <img width="160px" src='cid:logo' alt="bidgala-logo" />
            </td>
          </tr>
        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
          <tr>
            <td colspan="2" style="width:100%; color: #111;">
              <p>Hey there!</p>
              <p>Your friend """ + name + """ has invited you to join Bidgala’s online art community &amp; marketplace. Buy &amp; sell art, share your story, and join the art-loving community! Use """ + name + """’s invitation and join for free. You will
                automatically get 50 Bidgala credits that you can donate towards charity. </p>
              <br>
              <p style="text-align: center;"><a style="width: 100%; text-decoration: none; color: #fff; background-color: #111; font-size: 14px; border: 1px solid #111; padding: 10px 46px; font-weight: 500; margin-right: 10px; text-align: center; display: inline-block; min-width: 90px; font-family:'plain','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif; line-height: 25px; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;" href='"""+ link +"""'>Claim Invitation</a></p>
              <br>
              <p>Bidgala is a global dynamic marketplace and community for independent artists and art lovers. We put artists and their stories at the centre of everything because we believe that together we can change the world. </p>
              <p style="margin-bottom: 40px;">Warm Regards,
                <br>
                Team Bidgala
              </p>
            </td>
          </tr>
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td style="padding: 10px 0; border-top: 1px solid #f0efee;">
              <table cellpadding="0" cellspacing="0" align="left" width="49%">
                <tr>
                  <td>
                    <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin" alt="linkedin-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook" alt="facebook-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter" alt="twitter-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram" alt="instagram-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest" alt="pinterest-logo" style="width: 16px;"></a>
                  </td>
                </tr>
              </table>
              <table cellpadding="0" cellspacing="0" align="right" width="49%">
                <tr>
                  <td style="text-align: right;padding-left:10px; color: #111;">
                    <p style="margin: 0;">12042142 Canada Inc.</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="text-align:center">
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center;">Bidgala is an online marketplace where art lovers can buy directly from artists.</p>
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
            </td>
          </tr>
        </table>
      </center>
    </body>

    </html>

  """
  return email_template


def receiveCuratorPicks(name, title, price, dim, url):
  price = str(price)
  email_template = """
  <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <meta charset="utf-8"> <!-- utf-8 works for most cases -->
      <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
      <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
      <title>Notification on your curator pick</title> <!-- The title tag shows in email notifications, like Android 4.4. -->
      <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

      <!-- CSS Reset : BEGIN -->
      <style type="text/css">
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
          margin: 0 auto !important;
          padding: 0 !important;
          height: 100% !important;
          width: 100% !important;
          background: #fff;
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
          -ms-interpolation-mode: bicubic;
        }

        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
          text-decoration: none;
        }

        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],
        /* iOS */
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
          color: #111 !important;
        }

        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img+div {
          display: none !important;
        }

        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */

        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
          u~div .email-container {
            min-width: 320px !important;
          }
        }

        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
          u~div .email-container {
            min-width: 375px !important;
          }
        }

        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
          u~div .email-container {
            min-width: 414px !important;
          }
        }
      </style>
      <!-- Progressive Enhancements : BEGIN -->
      <style>
        .bg_white {
          background: #ffffff;
        }

        .btn {
          padding: 10px 15px;
          display: inline-block;
        }

        .btn.btn-black-outline {
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
      </style>
    </head>

    <body>
      <center style="width: 100%; background-color: #fff;">
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td bgcolor="#fff" style="font-size: 0; line-height: 0; padding:30px 0 25px 0; border-bottom: 1px solid #f0efee;" align="center" class="responsive-image">
              <img width="160px" src='cid:logo' alt="bidgala-logo" />
            </td>
          </tr>

        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
          <tr>
            <td colspan="2" style="width:100%; color:#111;">
              <p>Hey """+ name +"""!</p>
              <p style="line-height: 25px;">Congratulations! Your art piece <em>"""+ title +"""</em> has been selected to be part of Bidgala’s Curator Picks collection.</p>
              <a href='"""+url+"""'><em>Link to your art piece</em></a>
              <p style="margin-bottom: 8px;"><em>Title: """+ title +"""</em></p>
              <p style="margin: 8px 0;">Price: """+ price +"""</p>
              <p style="margin-top: 8px">Size: """+ dim +"""</p>
              <p style="line-height: 25px;">We all love your work! We are so excited to have you as a part of the Bidgala community. </p>
              <br>
              <p style="text-align: center;">
                <a href="#"
                  style="width: 100%; text-decoration: none; color: #fff; background-color: #111; font-size: 14px; border: 1px solid #111; padding: 10px 46px; font-weight: 500; margin-right: 10px; text-align: center; display: inline-block; min-width: 90px; font-family: &quot;plain&quot;,&quot;Helvetica Neue&quot;,&quot;Helvetica&quot;,Helvetica,Arial,sans-serif; line-height: 25px; -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */ -moz-box-sizing: border-box;    /* Firefox, other Gecko */ box-sizing: border-box;">
                  Post More Art Now
                </a>
              </p>
              <br>
              <p>Warm Regards,
                <br>
                Team Bidgala
              </p>
            </td>
          </tr>
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td style="padding: 10px 0; border-top: 1px solid #f0efee;">
              <table cellpadding="0" cellspacing="0" align="left" width="49%">
                <tr>
                  <td>
                    <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin" alt="linkedin-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook" alt="facebook-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter" alt="twitter-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram" alt="instagram-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest" alt="pinterest-logo" style="width: 16px;"></a>
                  </td>
                </tr>
              </table>
              <table cellpadding="0" cellspacing="0" align="right" width="49%">
                <tr>
                  <td style="text-align: right;padding-left:10px; color: #111;">
                    <p style="margin: 0;">12042142 Canada Inc.</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="text-align:center">
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center;">Bidgala is an online marketplace where art lovers can buy directly from artists.</p>
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
            </td>
          </tr>
        </table>
      </center>
    </body>

    </html>

  """
  return email_template


def referralConfirmed(to_name, from_name):
  email_template = """
 <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <meta charset="utf-8"> <!-- utf-8 works for most cases -->
      <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
      <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
      <title>Your friend Has Invited You To Join Bidgala’s Art-Loving Community</title> <!-- The title tag shows in email notifications, like Android 4.4. -->
      <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

      <!-- CSS Reset : BEGIN -->
      <style type="text/css">
        /* What it does: Remove spaces around the email design added by some email clients. */
        /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
        html,
        body {
          margin: 0 auto !important;
          padding: 0 !important;
          height: 100% !important;
          width: 100% !important;
          background: #fff;
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
          -ms-interpolation-mode: bicubic;
        }

        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
          text-decoration: none;
        }

        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],
        /* iOS */
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
          color: #111 !important;
        }

        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img+div {
          display: none !important;
        }

        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */

        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
          u~div .email-container {
            min-width: 320px !important;
          }
        }

        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
          u~div .email-container {
            min-width: 375px !important;
          }
        }

        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
          u~div .email-container {
            min-width: 414px !important;
          }
        }
      </style>
      <!-- Progressive Enhancements : BEGIN -->
      <style>
        .bg_white {
          background: #ffffff;
        }

        .btn {
          padding: 10px 15px;
          display: inline-block;
        }

        .btn.btn-black-outline {
          border-radius: 0px;
          background: transparent;
          border: 2px solid #000;
          color: #000;
          font-weight: 700;
        }
      </style>
    </head>

    <body>
      <center style="width: 100%; background-color: #fff;">
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td bgcolor="#fff" style="font-size: 0; line-height: 0; padding:30px 0 25px 0; border-bottom: 1px solid #f0efee;" align="center" class="responsive-image">
              <img width="160px" src='cid:logo' alt="bidgala-logo" />
            </td>
          </tr>

        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
          <tr>
            <td colspan="2" style="width:100%; color:#111;">
              <p>Hey """+from_name+"""!</p>
              <p style="line-height: 25px;">Congratulations! Your friend """+to_name+""" just joined Bidgala using your referral link. You’ve just received 50 Bidgala credits that you can donate to charity through your profile. Thank you for helping to
                expand the art-loving community!</p>
              <p style="line-height: 25px;">
                Invite more friends and make a difference. Get 50 Bidgala credits for charity with every friend that joins.
              </p>
              <br>
              <p style="text-align: center;">
                <a href="#"
                  style="width: 100%; color: black; font-weight: 500; background-color: #abcdef; padding: 8px; text-decoration: none; color: #fff; background-color: #111; font-size: 14px; border: 1px solid #111; padding: 10px 46px; font-weight: 500; margin-right: 10px; text-align: center; display: inline-block; min-width: 90px; font-family: &quot;plain&quot;,&quot;Helvetica Neue&quot;,&quot;Helvetica&quot;,Helvetica,Arial,sans-serif; line-height: 25px; -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */ -moz-box-sizing: border-box;    /* Firefox, other Gecko */ box-sizing: border-box;">
                  Invite More Friends Now
                </a>
              </p>
              <br>
              <p>Warm Regards,
                <br>
                Team Bidgala
              </p>
            </td>
          </tr>
          <tr>
            <td colspan="2" style="font-size: 0; line-height: 0; width:100%;" height="40px">&nbsp;</td>
          </tr>
        </table>
        <table cellpadding="0" cellspacing="0" width="600px">
          <tr>
            <td style="padding: 10px 0; border-top: 1px solid #f0efee;">
              <table cellpadding="0" cellspacing="0" align="left" width="49%">
                <tr>
                  <td>
                    <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin" alt="linkedin-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook" alt="facebook-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter" alt="twitter-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram" alt="instagram-logo" style="width: 16px;"></a>
                    <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest" alt="pinterest-logo" style="width: 16px;"></a>
                  </td>
                </tr>
              </table>
              <table cellpadding="0" cellspacing="0" align="right" width="49%">
                <tr>
                  <td style="text-align: right;padding-left:10px; color: #111;">
                    <p style="margin: 0;">12042142 Canada Inc.</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="text-align:center">
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center;">Bidgala is an online marketplace where art lovers can buy directly from artists.</p>
              <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
            </td>
          </tr>
        </table>
      </center>
    </body>

    </html>

  """
  return email_template





def followingEmail(link_to_profile, following_person_name):

  email_template = """
  <!DOCTYPE html>
      <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
      <head>
          <meta charset="utf-8"> <!-- utf-8 works for most cases -->
          <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
          <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
          <title>Please verify you email address</title> <!-- The title tag shows in email notifications, like Android 4.4. -->

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
          color: #111 !important;
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

      p{
        line-height: 25px;
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

      a.confirm-button{
        width: 100%;
        color: black;
        font-weight: 500;
        background-color: #abcdef;
        padding: 8px;
        text-decoration: none;
        color: #fff;
        background-color: #111;
        font-size: 14px;
        border: 1px solid #111;
        padding: 10px 46px;
        font-weight: 500;
        margin-right: 10px;
        text-align: center;
        display: inline-block;
        min-width: 90px;
        font-family: &quot;plain&quot;,&quot;Helvetica Neue&quot;,&quot;Helvetica&quot;,Helvetica,Arial,sans-serif;
        line-height: 25px;
        -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
        -moz-box-sizing: border-box;    /* Firefox, other Gecko */
        box-sizing: border-box;
      }

      a.social-media{
        margin-left: 10px;
        opacity: 50%;
      }

      a.social-media img{
        width: 16px;
      }

          </style>


      </head>

      <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
      <center style="width:100%;background-color: #FFFFFF;">
          <div style="display:none;font-size:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;font-family:sans-serif">
            &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;<wbr>&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
          </div>
          <div style="max-width:600px;margin:0 auto" class="email-container">

            <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin:auto">
              <tbody><tr>
                <td valign="top" style="padding: 30px 0 16px 0;border-bottom: 1px solid #f0efee;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                      <td class="logo" style="text-align: left;">
                        <img src="cid:logo" alt="bidgala-logo" style="width: 118px;height: auto;">
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr>
              <tr>
                <td style="color: #222;">

                <h2 style="line-height: 45px;color: #222;">You have a new follower</h2>






                <p><u><a href='"""+link_to_profile+"""'>"""+following_person_name+"""</a></u> is following you.</p>


                </td>
            </tr>
              <tr>
                <td><table class="bg_white" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">


                </table>
              </td></tr>

            </tbody></table>
            <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin:auto;border-top: 1px solid #f0efee;background-color: #FFFFFF;">
              <tbody><tr>
                <td valign="middle" style="background-color: #FFFFFF;">
                  <table>
                    <tbody><tr>
                      <td valign="top" width="33.333%" style="padding-top:20px">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                            <td style="text-align:left;padding-right:10px">
                              <div>
                                <a href='"""+ settings.LINKEDIN_LINK +"""' style="margin: 0; opacity: 50%;"><img src="cid:linkedin" alt="linkedin-logo" style="width: 16px;"></a>
                                <a href='"""+ settings.FACEBOOK_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:facebook" alt="facebook-logo" style="width: 16px;"></a>
                                <a href='"""+ settings.TWITTER_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:twitter" alt="twitter-logo" style="width: 16px;"></a>
                                <a href='"""+ settings.INSTAGRAM_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:instagram" alt="instagram-logo" style="width: 16px;"></a>
                                <a href='"""+ settings.PINTEREST_LINK +"""' style="margin-left: 10px; opacity: 50%;"><img src="cid:pinterest" alt="pinterest-logo" style="width: 16px;"></a>

                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>

                      <td valign="top" width="33.333%" style="/* padding-top:20px */">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                            <td style="text-align: right;padding-left:10px; color: #111;">
                              <p>12042142 Canada Inc.</p>

                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr>
              <tr>
                <td class="bg_white" style="text-align:center">
                  <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-top: 60px;">
                  <span style="text-decoration: underline;">UNSUBSCRIBE</span> from these emails or <span style="text-decoration: underline;">Click here</span> to update your preferences.
                </p>
                <p style="font-size: 12px; color: #969697; line-height: 1.3; text-align: center; margin-bottom: 30px;">Bidgala 720 Avenue Upper Roslyn, Westmount, Quebec, H3Y 1H9, Canada</p>
                </td>
              </tr>
            </tbody></table>
          </div>
        </center>
        </body>
            </html>
  """
  return email_template
