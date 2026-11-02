TOOLS = {}


def register_tool(name, function):
    TOOLS[name] = function


def get_tool(name):
    return TOOLS.get(name)


def list_tools():
    return list(TOOLS.keys())