import os
from pathlib import Path

import yaml

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Configuration:
    ENV = os.environ.get('ENV', default='prod')
    BASE_URL = 'https://www.cosmosid.com/'
    LOGIN_PAGE = 'https://app.cosmosid.com/login'
    BROWSER = os.environ.get('BROWSER', default='firefox')

    config_path = Path.home() / 'PycharmProjects' / 'gl_pro_camp' / 'core'
    config_path_json = config_path / 'env_configs' / f'{ENV}.yaml'
    config_path_yaml = config_path / 'config.yaml'

    defaults = {
        "ENV": "uat",
        "BROWSER": "chrome",
        "BASE_URL": "https://www.cosmosid.com/",
        "LOGIN_PAGE": "https://app.cosmosid.com/login",
        "SUPPORTED_BROWSERS": ["chrome", "firefox", "edge", "opera"]
    }

    @classmethod
    def get_config(cls, key: str):
        """Get configuration hierarchically from different sources"""
        env_var_config = cls._get_config_from_env_var()
        json_config = cls._get_config_from_file(cls.config_path_json)
        yaml_config = cls._get_config_from_file(cls.config_path_yaml)
        config_providers = [env_var_config, json_config, yaml_config, cls.defaults]
        for provider in config_providers:
            result = provider.get(key)
            if result is not None:
                return result
        return None

    @classmethod
    def _get_config_from_env_var(cls):
        """Get configuration from environment variables"""
        config_data = {}
        for key, value in cls.defaults.items():
            if key in os.environ:
                config_data[key] = os.environ[key]
        return config_data

    @classmethod
    def _get_config_from_file(cls, file_path):
        """Get configuration from file"""
        with open(file_path, encoding='utf8') as fh:
            config_data = yaml.load(fh)
        return config_data
