import yaml

config = yaml.safe_load(open("config.yaml"))
print(config)
print(config['namaMahasiswa'])