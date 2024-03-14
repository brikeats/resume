# HTML Resume Builder

A collection of scripts and templates for building a resume from JSON data.

## Quickstart

I'm running this in a Python 3.11 conda environment. 

* `pip install Jinja2`
* Add data to `resume_data.json`
* Render html page using the default template and save result as `html/resume.html`: `python render_html.py --template default --out html/resume.html resume_data.json`
* Convert to pdf with Chrome. Change to the build folder (`cd html`) and run:
    * Linux: `google-chrome --headless --no-sandbox --disable-gpu --print-to-pdf --no-pdf-header-footer file://$(pwd)/html/resume.html`
    * MacOS: `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --no-sandbox --disable-gpu --print-to-pdf --no-pdf-header-footer file://$(pwd)/html/resume.html`
