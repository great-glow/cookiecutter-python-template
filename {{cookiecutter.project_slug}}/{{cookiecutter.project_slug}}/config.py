from dynaconf import Dynaconf

settings = Dynaconf(
    load_dotenv=True,
    environments=True,
    settings_files=['settings.toml'],
{%- if cookiecutter.enable_vault_loader == 'y' %} 
    loaders=['dynaconf.loaders.vault_loader'],
{%- endif %}
)
