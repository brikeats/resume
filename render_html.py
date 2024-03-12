import argparse
from glob import glob
import json
from os import environ, path, makedirs, getcwd
import shutil
import sys
from jinja2 import Template


TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')
TEMPLATE_NAMES = [path.basename(name).replace('.html','') for name in sorted(glob('templates/*.html'))]


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Fill in an HTML template with resume data')
    parser.add_argument('--out', '-o', default='html/resume.html')
    parser.add_argument('--template', choices=TEMPLATE_NAMES, default='default')
    parser.add_argument('json_data', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="JSON file (or piped stdin) containing your data")
    args = parser.parse_args()

    # read the data & template
    json_data = json.loads(args.json_data.read())
    template_fn = path.join(TEMPLATE_DIR, args.template+'.html')
    with open(template_fn) as f:
        template = Template(f.read())

    # render the HTML
    html = template.render(json_data)
    out_dir = path.dirname(args.out)
    if out_dir:
        makedirs(out_dir, exist_ok=True)
    with open(args.out, 'wt') as f:
        f.write(html)
    print(f'Rendering HTML result saved to {args.out}')

    # copy static files to output directory
    if path.abspath(out_dir) != path.abspath(getcwd()):
        shutil.copytree('static', path.join(out_dir, 'static'), dirs_exist_ok=True)
