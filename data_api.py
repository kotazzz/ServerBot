import uuid
import yaml
from abc import ABC
import io
import datetime

def safe_uuid(string):
    try:
        return uuid.UUID(string)
    except (ValueError, AttributeError):
        return string

class DataABC(ABC):
    def __init__(self, data):
        self.uuid = uuid.uuid4()
        try:
            self.dict_export.append("uuid")
        except Exception:
            self.dict_export = ["uuid"]
        type_handlers = {
            str: safe_uuid,
            DataABC.to_dict: DataABC,
        }
        for k, v in data.items():
            if type(v) in type_handlers:
                handler = type_handlers[type(v)]
                v = handler(v)
            setattr(self, k, v)

    def to_dict(self):
        data = {}
        type_handlers = {
            uuid.UUID: str,
            DataABC: DataABC.to_dict,
            list: lambda l: [i.to_dict() if isinstance(i, DataABC) else i for i in l],
        }
        for key in self.dict_export:
            val = getattr(self, key)
            if type(val) in type_handlers:
                handler = type_handlers[type(val)]
                val = handler(val)
            data[key] = val
        return data


class ConfigFile:
    def __init__(self, name="config"):
        self.name = name
        self.load()

    def save(self):
        with io.open(f"{self.name}.yml", "w", encoding="utf8") as outfile:
            yaml.dump(self.data, outfile, default_flow_style=False, allow_unicode=True)

    def load(self):
        with open(f"{self.name}.yml", "r") as stream:
            self.data = yaml.safe_load(stream)


class ConfigData:
    def __init__(self, cfg, data_path):
        self.cfg_save = cfg.save
        self.data = cfg.data
        self.path = data_path
        self.watching = {}
        self.sections = {}

    def get_data(self):
        def nested_lookup(nlst, idexs):
            if len(idexs) == 1:
                return nlst[idexs[0]]
            return nested_lookup(nlst[idexs[0]], idexs[1::])

        return nested_lookup(self.data, self.path)

    def new_section(self, name, data_worker):
        self.sections[name] = data_worker

    def watch(self, section, load_element):
        try:
            self.watching[section]
        except:
            self.watching[section] = []
        self.watching[section].append(load_element)

    def save(self):
        data = {
            sect: [element.to_dict() for element in elements]
            for sect, elements in self.watching.items()
        }

        self.get_data().update(data)
        self.cfg_save()

    def load(self):
        result = {}
        self.watching = {}
        for sect, elements in self.get_data().items():
            worker = self.sections[sect]
            result[sect] = []
            self.sections[sect] = []
            for element in elements:
                dataobj = worker(element)
                result[sect].append(dataobj)
                self.watch(sect, dataobj)
                self.sections[sect].append(dataobj)
        return result

