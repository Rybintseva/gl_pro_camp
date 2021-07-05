import os

import yaml

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Configuration:
    config_path = os.path.join(HOME_PATH, 'core', 'config.yaml')

    @classmethod
    def get_config(cls, key: str):
        """Get configuration from different sources"""
        env_var_config = cls._get_config_from_env_var()
        yaml_config = cls._get_config_from_file(cls.config_path)
        config_providers = [env_var_config, yaml_config]
        for provider in config_providers:
            result = provider.get(key)
            if result is not None:
                return result
        return None

    @classmethod
    def _get_config_from_env_var(cls):
        """Get configuration from environment variables"""
        config = {}
        for key, value in cls._get_config_from_file(cls.config_path).items():
            if key in os.environ:
                config[key] = os.environ[key]
        return config

    @classmethod
    def _get_config_from_file(cls, file_path):
        """Get configuration from file"""
        with open(file_path, encoding='utf8') as fh:
            config = yaml.full_load(fh)
        return config
