from dynaconf import Dynaconf

settings = Dynaconf(
    load_dotenv=True,
    environments=True,
    settings_files=['settings.toml'],
    loaders=['dynaconf.loaders.vault_loader'],
)
