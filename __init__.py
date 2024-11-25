from .nodes.combiner import ETSplitTextNode, ETJoinTextNode
from .nodes.converter import ETATOI, ETITOA
from .nodes.formatter import ETTextFormatter2Node, ETTextFormatter5Node, ETTextFormatter10Node
from .nodes.scripting import ETPythonTextScript3Node
from .nodes.replacer import ETReplaceTextNode

et_nodes = {
    ("Split Text", ETSplitTextNode),
    ("Join Text", ETJoinTextNode),

    ("ATOI", ETATOI),
    ("ITOA", ETITOA),

    ("Text Formatter (2 Arguments)", ETTextFormatter2Node),
    ("Text Formatter (5 Arguments)", ETTextFormatter5Node),
    ("Text Formatter (10 Arguments)", ETTextFormatter10Node),

    ("Text Replacer", ETReplaceTextNode),

    ("Python Text Script (3 Arguments)", ETPythonTextScript3Node),
}

NODE_CLASS_MAPPINGS = {cls.__name__: cls for display_name, cls in et_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {cls.__name__: display_name for display_name, cls in et_nodes}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
