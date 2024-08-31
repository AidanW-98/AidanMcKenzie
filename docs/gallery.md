# Gallery

The 'Gallery' page of the site displays all images given by the '.md' in '\_gallery'. 

The '.md' files contain basic metadata (title, subtitle, date_taken) and crucially the filepath of the images to display.

It is expected for all images to be displayed in the gallery to be stored in `\assets\imgs\gallery`. As such `generate_markdown.py` exists to generate the `.md` files from the image metadata in `\assets\imgs\gallery` - JPG files are preferred for this reason.

It is a *to do* task for this python script to run in a CI/CD pipeline.