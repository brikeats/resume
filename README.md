# HTML Resume Builder

A collection of scripts and templates for building an HTML resume from JSON data.

## Quickstart

I'm running this in a Python 3.11 conda environment. 

* `pip install Jinja2`
* Add you data to `resume_data.json`
* Render html page using the default template and save result as `html/resume.html`: `python render_html.py --template default --out html/resume.html resume_data.json`
