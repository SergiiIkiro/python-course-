from configs import password

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'noreply.storesales@gmail.com'
users = ['innovationsolutions2019@gmail.com', 'sanchezs@ukr.net']
all_users = ", ".join(users)

message = MIMEMultipart('alternative')
message['Subject'] = 'Store updates'
message['From'] = sender
message['To'] = all_users

text = """
Hi there, 
This is the first try of sending an update email.
Please reach the www.google.com for more details.
"""

html_text = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
    <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]-->
    <!--[if !mso]><!-- -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700,700i" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i" rel="stylesheet">
    <!--<![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#eff2f7"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table class="es-header esd-header-popover" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" bgcolor="transparent" style="background-color: transparent;" esd-custom-block-id="78531">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#0c66ff" align="center" style="background-color: #0c66ff;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b es-p15r es-p15l" align="left">
                                                        <table cellspacing="0" cellpadding="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r esd-container-frame" width="570" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p15b">
                                                                                        <p>Put your preheader text here</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-m-txt-c" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/88111573468980834.png" alt style="display: block;" width="150"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/49631573482762301.png" alt style="display: block;" width="600"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b es-p15r es-p15l" align="left" bgcolor="transparent" style="background-color: transparent;">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-menu" esd-tmp-menu-font-size="16px" esd-tmp-menu-font-weight="bold" esd-tmp-menu-padding="0|0" esd-tmp-menu-color="#ffffff">
                                                                                        <table cellpadding="0" cellspacing="0" width="100%" class="es-menu">
                                                                                            <tbody>
                                                                                                <tr class="links">
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 0px; padding-top: 0px;"><a target="_blank" href="https://viewstripo.email/" style="font-size: 16px; font-weight: bold; color: #ffffff;">HOME</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 0px; padding-top: 0px;"><a target="_blank" href="https://viewstripo.email/" style="font-size: 16px; font-weight: bold; color: #ffffff;">ELECTRONICS</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l es-mobile-hidden" style="padding-bottom: 0px; padding-top: 0px;"><a target="_blank" href="https://viewstripo.email/" style="font-size: 16px; font-weight: bold; color: #ffffff;">ALL CATEGORY</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 0px; padding-top: 0px;"><a target="_blank" href="https://viewstripo.email/" style="font-size: 16px; font-weight: bold; color: #ffffff;">SALE</a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#fefefe" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p20b es-p15r es-p15l" align="left" esd-custom-block-id="78533">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h1>RECENT FROM BLOG</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h3 style="color: #0c66ff;">SIMPLE SOLUTIONS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p15r es-p15l" align="left" esdev-config="h1">
                                                        <!--[if mso]><table  width="570" cellpadding="0" cellspacing="0"><tr><td width="285" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="left" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="285" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img b_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/2331573473316766.jpg" alt style="display: block;" width="285"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="265" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="265" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text es-m-txt-l">
                                                                                        <h3 style="color: #0c66ff;" class="b_category">COMPILATION</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text es-m-txt-l es-p10b">
                                                                                        <h1 class="b_title">BEST DEVICES</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text">
                                                                                        <p class="b_description">Lorem Ipsum is simply dummy text of the printing and typesetting industry.&nbsp;</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-button es-m-txt-l es-p20t es-p20b"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">READ MORE</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p15r es-p15l" align="left" esd-custom-block-id="78545" esdev-config="h2">
                                                        <!--[if mso]><table  width="570" cellpadding="0" cellspacing="0"><tr><td width="285" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="left" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="285" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img b_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/78231573473330004.jpg" alt style="display: block;" width="285"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="265" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="265" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text es-m-txt-l">
                                                                                        <h3 style="color: #0c66ff;" class="b_category">SOLUTIONS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text es-m-txt-l es-p10b">
                                                                                        <h1 class="b_title">EASY WORK</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text">
                                                                                        <p class="b_description">Lorem Ipsum is simply dummy text of the printing and typesetting industry.&nbsp;</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-button es-m-txt-l es-p20t es-p20b"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">READ MORE</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left" esd-custom-block-id="78551">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-l"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">SHOW MORE POST</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" bgcolor="#0050d8" style="background-color: #0050d8;" esd-custom-block-id="78546">
                                        <table bgcolor="#0c66ff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #0c66ff;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-infoblock es-m-txt-c">
                                                                                        <h1 style="color: #ffffff;">WHERE DOES IT COME FROM?</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-infoblock es-m-txt-c es-p20t es-p20b">
                                                                                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-p20t es-m-txt-c"><span class="es-button-border" style="background: #ffffff;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="color: #0c66ff; background: #ffffff; border-color: #ffffff;">BUY NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#fefefe" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left" esd-custom-block-id="78534">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h1>BEST SALE</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h3 style="color: #2dca8c;">SPECIAL OFFER</h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20b es-p15r es-p15l" align="left" esd-custom-block-id="78549">
                                                        <!--[if mso]><table  width="570" cellpadding="0" cellspacing="0"><tr><td width="275" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="left" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="275" valign="top" align="center" esdev-config="h6">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#eff2f7" style="background-color: #eff2f7;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p20t es-p10r es-p10l" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/15091573478329666.png" alt style="display: block;" height="180"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t es-p10r es-p10l es-m-txt-c">
                                                                                        <h3 style="color: #2dca8c;" class="p_category">LAPTOPS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20b es-p10r es-p10l es-m-txt-c">
                                                                                        <h1 class="p_name">Acer Nitro 5&nbsp;Black</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p10r es-p10l">
                                                                                        <p><strong><s class="p_old_price es-p10r p_old_price" style="vertical-align:middle;">$933</s><span class="p_price" style="color:#2dca8c;font-size:22px;vertical-align:middle;">$811</span></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-c es-p20t es-p20b es-p10r es-p10l"><span class="es-button-border" style="background: #2dca8c;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #2dca8c; border-color: #2dca8c;">BUY NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="275" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="275" valign="top" align="center" esdev-config="h7">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#eff2f7" style="background-color: #eff2f7;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p20t es-p10r es-p10l" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/12931573478337840.png" alt style="display: block;" width="255"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p10r es-p10l">
                                                                                        <h3 style="color: #2dca8c;" class="p_category">KEYBOARDS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20b es-p10r es-p10l">
                                                                                        <h1 class="p_name">HyperX Alloy Origins</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p10r es-p10l">
                                                                                        <p><strong><s class="p_old_price es-p10r p_old_price" style="vertical-align:middle;">$135</s><span class="p_price" style="color:#2dca8c;font-size:22px;vertical-align:middle;">$119</span></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-c es-p20t es-p20b es-p10r es-p10l"><span class="es-button-border" style="background: #2dca8c;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #2dca8c; border-color: #2dca8c;">BUY NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20b es-p15r es-p15l" align="left">
                                                        <!--[if mso]><table  width="570" cellpadding="0" cellspacing="0"><tr><td width="275" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="left" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="275" valign="top" align="center" esdev-config="h8">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#eff2f7" style="background-color: #eff2f7;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p20t es-p10r es-p10l" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/78251573478345058.png" alt style="display: block;" height="180"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p10r es-p10l">
                                                                                        <h3 style="color: #2dca8c;" class="p_category">MONITORS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20b es-p10r es-p10l">
                                                                                        <h1 class="p_name">LG UltraGear</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p10r es-p10l">
                                                                                        <p><strong><s class="p_old_price es-p10r p_old_price" style="vertical-align:middle;">$969</s><span class="p_price" style="color:#2dca8c;font-size:22px;vertical-align:middle;">$899</span></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-c es-p20t es-p20b es-p10r es-p10l"><span class="es-button-border" style="background: #2dca8c;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #2dca8c; border-color: #2dca8c;">BUY NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="275" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="275" valign="top" align="center" esdev-config="h9">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#eff2f7" style="background-color: #eff2f7;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p20t es-p10r es-p10l" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/19121573478878688.png" alt style="display: block;" height="180"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p10r es-p10l">
                                                                                        <h3 style="color: #2dca8c;" class="p_category">SYSTEM UNITS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20b es-p10r es-p10l">
                                                                                        <h1 class="p_name">Qbox I0625</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p10r es-p10l">
                                                                                        <p><strong><s class="p_old_price es-p10r p_old_price" style="vertical-align:middle;">$690</s><span class="p_price" style="color:#2dca8c;font-size:22px;vertical-align:middle;">$590</span></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-c es-p20t es-p20b es-p10r es-p10l"><span class="es-button-border" style="background: #2dca8c;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #2dca8c; border-color: #2dca8c;">BUY NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p40b es-p15r es-p15l" align="left" esd-custom-block-id="78552">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button"><span class="es-button-border" style="background: #2dca8c;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #2dca8c; border-color: #2dca8c;">MORE GOODS</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" bgcolor="#52d8a3" style="background-color: #52d8a3;" esd-custom-block-id="78557">
                                        <table bgcolor="#2dca8c" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #2dca8c;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p5r es-p5l" align="left">
                                                        <!--[if mso]><table width="590" cellpadding="0" cellspacing="0"><tr><td width="199" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="194" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p40t es-p20b" style="font-size:0"><a target="_blank"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/21671573466877223.png" alt style="display: block;" width="64"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p40b es-m-txt-c">
                                                                                        <h2 style="color: #ffffff;">Deals and promocode</h2>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td class="es-hidden" width="5"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="193" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="193" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#24a06f" style="background-color: #24a06f;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p40t es-p20b" style="font-size:0"><a target="_blank"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/87151573466611596.png" alt style="display: block;" width="64"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p40b es-m-txt-c">
                                                                                        <h2 style="color: #ffffff;">Secure&nbsp;Payments</h2>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="5"></td><td width="193" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="193" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p40t es-p20b" style="font-size:0"><a target="_blank"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/63821573466764525.png" alt style="display: block;" width="64"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p40b es-m-txt-c">
                                                                                        <h2 style="color: #ffffff;">24/7 Customer service</h2>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" esd-custom-block-id="78014">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left" esd-custom-block-id="78535">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h1>SETS FOR WORK</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <h3 style="color: #ff294a;">BEST KITS</h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p15r es-p15l" align="left" esd-custom-block-id="78561" esdev-config="h3">
                                                        <!--[if mso]><table dir="rtl" width="570" cellpadding="0" 
                        cellspacing="0"><tr><td dir="ltr" width="285" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="285" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/72271573484566998.jpg" alt style="display: block;" width="285"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td dir="ltr" width="20"></td><td dir="ltr" width="265" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="265" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t es-p20b">
                                                                                        <h2 class="p_name">BEGINNERS KIT</h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <p class="p_description">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p20b" esd-links-color="#ff294a">
                                                                                        <p><strong><a target="_blank" style="color: #ff294a;" href="https://viewstripo.email/">BUY NOW ⯈</a></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p15r es-p15l" align="left" esd-custom-block-id="78562" esdev-config="h4">
                                                        <!--[if mso]><table width="570" cellpadding="0" 
                        cellspacing="0"><tr><td width="285" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="285" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/47801573484575131.jpg" alt style="display: block;" width="285"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="265" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="265" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t es-p20b">
                                                                                        <h2 class="p_name">ADVANCED SET</h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <p class="p_description">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p20b" esd-links-color="#ff294a">
                                                                                        <p><strong><a target="_blank" style="color: #ff294a;" href="https://viewstripo.email/">BUY NOW ⯈</a></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p15r es-p15l" align="left" esdev-config="h5">
                                                        <!--[if mso]><table dir="rtl" width="570" cellpadding="0" 
                        cellspacing="0"><tr><td dir="ltr" width="285" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="285" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img p_image" src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/51451573484583153.jpg" alt style="display: block;" width="285"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td dir="ltr" width="20"></td><td dir="ltr" width="265" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="265" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t es-p20b">
                                                                                        <h2 class="p_name">SET FOR PROFESSIONAL</h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c">
                                                                                        <p class="p_description">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p20b" esd-links-color="#ff294a">
                                                                                        <p><strong><a target="_blank" style="color: #ff294a;" href="https://viewstripo.email/">BUY NOW ⯈</a></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left" esd-custom-block-id="78553">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-m-txt-l"><span class="es-button-border" style="background: #ff294a;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #ff294a; border-color: #ff294a;">SHOW MORE SETS</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" bgcolor="#ff5c75" style="background-color: #ff5c75;" esd-custom-block-id="78563">
                                        <table bgcolor="#ff294a" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #ff294a;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-infoblock es-p20b es-m-txt-c">
                                                                                        <h1 style="color: #ffffff;">PROMOCODE</h1>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="border-left:3px dashed #ff8fa0;border-right:3px dashed #ff8fa0;border-top:3px dashed #ff8fa0;border-bottom:3px dashed #ff8fa0;border-radius: 10px; border-collapse: separate;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-infoblock es-m-txt-c es-p20t es-p20b es-p10r es-p10l">
                                                                                        <h1 style="color: #ffffff;">PR2-0O1-FMO-12C-ODE</h1>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                <tr>
                                                                    <td width="570" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-p20t es-m-txt-c"><span class="es-button-border" style="background: #ffffff;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="background: #ffffff; border-color: #ffffff; color: #ff294a;">USE NOW</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-footer" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" esd-custom-block-id="78565">
                                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p15r es-p15l" align="left">
                                                        <!--[if mso]><table width="570" cellpadding="0" 
                        cellspacing="0"><tr><td width="180" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="180" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-m-txt-c" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9603655fea8888bb07fac71a5d841730/images/17351573473501663.png" alt style="display: block;" width="150"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-social es-p20t es-m-txt-c" style="font-size:0">
                                                                                        <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td align="center" valign="top" esd-tmp-icon-type="facebook" class="es-p10r"><a target="_blank" href><img src="https://uhpwio.stripocdn.email/content/assets/img/social-icons/logo-white/facebook-logo-white.png" alt="Fb" title="Facebook" width="32"></a></td>
                                                                                                    <td align="center" valign="top" esd-tmp-icon-type="twitter" class="es-p10r"><a target="_blank" href><img src="https://uhpwio.stripocdn.email/content/assets/img/social-icons/logo-white/twitter-logo-white.png" alt="Tw" title="Twitter" width="32"></a></td>
                                                                                                    <td align="center" valign="top" esd-tmp-icon-type="youtube" class="es-p10r"><a target="_blank" href><img src="https://uhpwio.stripocdn.email/content/assets/img/social-icons/logo-white/youtube-logo-white.png" alt="Yt" title="Youtube" width="32"></a></td>
                                                                                                    <td align="center" valign="top" esd-tmp-icon-type="instagram"><a target="_blank" href><img src="https://uhpwio.stripocdn.email/content/assets/img/social-icons/logo-white/instagram-logo-white.png" alt="Ig" title="Instagram" width="32"></a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="370" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="370" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text es-m-txt-c es-p20t es-p20b">
                                                                                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table bgcolor="transparent" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-infoblock made_with" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/?utm_source=templates&utm_medium=email&utm_campaign=gadgets&utm_content=gizmos"><img src="https://uhpwio.stripocdn.email/content/guids/CABINET_9df86e5b6c53dd0319931e2447ed854b/images/64951510234941531.png" alt width="125"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html_text, 'html')

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465,
                      context=context) as server:  # створення захищеного з'єднання з сервером
    server.login(user=sender, password=password)  # логування користувача до сервера
    server.ehlo()
    server.sendmail(sender, users, message.as_string())
