import eclipse_plugin
import vscode_plugin
import xcode_plugin
import replit_plugin

def install_plugin(plugin):
    """Install a given plugin."""
    if plugin == "eclipse":
        return eclipse_plugin.install()
    elif plugin == "vscode":
        return vscode_plugin.install()
    elif plugin == "xcode":
        return xcode_plugin.install()
    elif plugin == "replit":
        return replit_plugin.install()
    else:
        raise ValueError(f"Invalid plugin name: {plugin}")

def use_plugin(plugin):
    """Use a given plugin."""
    if plugin == "eclipse":
        return eclipse_plugin.use()
    elif plugin == "vscode":
        return vscode_plugin.use()
    elif plugin == "xcode":
        return xcode_plugin.use()
    elif plugin == "replit":
        return replit_plugin.use()
    else:
        raise ValueError(f"Invalid plugin name: {plugin}")

PLUGINS = {
    "eclipse": install_eclipse_plugin,
    "vscode": install_vscode_plugin,
    "xcode": install_xcode_plugin,
    "replit": install_replit_plugin,
}

def install_plugin_by_name(plugin_name):
    """Install a plugin by its name."""
    return PLUGINS[plugin_name]()

PLUGIN_ACTIONS = {
    "use": use_plugin,
}

def use_plugin_by_name(plugin_name, action="use"):
    """Use a plugin by its name and the action to perform on it."""
    plugin_func = PLUGIN_ACTIONS[action]
    return plugin_func(plugin_name)
