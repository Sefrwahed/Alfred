from jinja2 import Environment, FileSystemLoader


APP_NAME = "Alfred"
WIT_TOKEN = "GMCAOZ4HFZ3Q5K7FNOFIQSR6VCM6NA47"

main_components_env = Environment(
    loader=FileSystemLoader('alfred/modules/templates'),
    autoescape=False
)
