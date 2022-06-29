# scribe-markdown-reformatting
This script quickly reformatts markdown exported from scribehow.com (for which you need a PRO account).
It also removed credits and fixes an issue where "None." is added in front of tips and alerts.

## How to use this script
1. Export the markdown by clicking share in one of your scribes
2. Create a file in the src folder (has to be in the same folder as the main script).
3. Paste the markdown from scribehow.com
4. Add more markdown files to src if you wish
6. Run the script
5. Retrieve your reformatted markdown file (with the same name) from dst/

### Wordpress 
I use this in conjunction with Wordpress Ultimate Markdown (https://wordpress.org/plugins/ultimate-markdown/) for my blog.
This script could definitely be combined with a wordpress reformatting script in order to go from markdown input directly to wordpress.

## Requirements
Currently requires python 3.2 for the dst file creation but that should be easy to fix if need be.
