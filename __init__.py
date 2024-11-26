loaded = []
not_loaded = []
exceptions = []

try:
    from .api_nodes import NODE_CLASS_MAPPINGS as api

    loaded.append(f"api nodes ({len([*api])})")
except Exception as e:
    api = {}
    not_loaded.append("api nodes")
    exceptions.append(e)

try:
    from .simple_utilities import NODE_CLASS_MAPPINGS as simple

    loaded.append(f"simple utility nodes ({len([*simple])})")
except Exception as e:
    simple = {}
    exceptions.append(e)
    not_loaded.append("simple utility nodes")

try:
    from .cv_nodes import NODE_CLASS_MAPPINGS as cv_nodes

    loaded.append(f"CV nodes ({len([*cv_nodes])})")
except Exception as e:
    cv_nodes = {}
    not_loaded.append("CV nodes")
    exceptions.append(e)

try:
    from .color_clip_ade20k import NODE_CLASS_MAPPINGS as cc_ade20k

    loaded.append("color clip ade20k node (1)")
except Exception as e:
    cc_ade20k = {}
    exceptions.append(e)
    not_loaded.append("color clip ade20k node")

try:
    from .extension_dependant_utilities import NODE_CLASS_MAPPINGS as extended

    loaded.append(f"extension dependent nodes ({len([*extended])})")
except Exception as e:
    extended = {}
    not_loaded.append("extension dependent nodes")
    exceptions.append(e)

import nodes

NODE_CLASS_MAPPINGS = {**api, **simple, **cv_nodes, **cc_ade20k, **extended}
WEB_DIRECTORY = "js"

__all__ = ['NODE_CLASS_MAPPINGS']


print('\n\033[1mFrom Bmad Custom Nodes\033[0m')

if not hasattr(nodes, "EXTENSION_WEB_DIRS"):
    exceptions.append(f"The version of ComfyUI is outdated. Some nodes won't work as intended.")

print(f' \033[92mLoaded {len([*NODE_CLASS_MAPPINGS])} nodes:')
for m in loaded:
    print(f'  + {m}')

if len(not_loaded) > 0:
    print(f' \033[93mNot loaded:')
    for m in not_loaded:
        print(f'  * {m}')

if len(exceptions) > 0:
    print(' \033[91mProblems:')
    for e in exceptions:
        print(f'  ! {e}')

print('\033[0m')