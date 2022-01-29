from data_api import ConfigFile, DataABC, ConfigData


cfg = ConfigFile("config_copy")


class CategoryInfo (DataABC):
    def __init__(self, data):
        super().__init__(data)
        self.dict_export += ["id", "name", "pos", "override"]

class ChannelInfo (DataABC):
    def __init__(self, data):
        super().__init__(data)
        self.dict_export += ["id", "name", "emoji", "pos", "category", "override"]
    def get_override(self) : pass


class RoleCategoryInfo (DataABC):
    def __init__(self, data):
        super().__init__(data)
        self.dict_export += ["id", "name", "pos"]

class RoleInfo (DataABC):
    def __init__(self, data):
        super().__init__(data)
        self.dict_export += ["id", "name", "emoji", "pos", "category", "perms"]
    def get_override(self) : pass


category = CategoryInfo({
        "id":"",
        "name":"",
        "pos":"",
        "override":"",})

channel = ChannelInfo({
        "id":"",
        "name":"",
        "emoji":"",
        "pos":"",
        "category":"",
        "override":"",})

rolecat = RoleCategoryInfo({
        "id":"",
        "name":"",
        "pos":""})

role = RoleInfo({
        "id":"",
        "name":"",
        "emoji":"",
        "pos":"",
        "category":"",
        "perms":"",})

print(category.to_dict())
print(channel.to_dict())
print(rolecat.to_dict())
print(role.to_dict())

# {
# "user":       disnake.Permissions(517647748673),
# "helper":     disnake.Permissions(1635836620481),
# "moder":      disnake.Permissions(1635845533395),
# "admin":      disnake.Permissions(1644972470263),
# "superadmin":     disnake.Permissions(1644972470263),
# "coowner":    disnake.Permissions(1644972474359) ,
# "owner":      disnake.Permissions(1644972474359),
# }