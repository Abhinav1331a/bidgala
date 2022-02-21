from django.conf import settings

def sendEmail(message, from_user_name, from_user_id):
  BASE_URL = settings.HOST_BASE_URL
  CHAT_URL = BASE_URL + 'messages/' + str(from_user_id)

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
              <h4 style="font-weight: bold;">New message from """ + from_user_name + """</h4>
              <p>""" + message + """ </p>
              <p><a href='""" + CHAT_URL + """'>REPLY</a>
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
