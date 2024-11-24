class ETTextFormatterNode:
    """
    Base class for nodes that take a number of inputs and format them
    into a single string.
    """

    INPUT_IS_LIST = True

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails"
    FUNCTION = "process"

    def process(self, format, arg0="", arg1="", arg2="", arg3="", arg4="", arg5="", arg6="", arg7="", arg8="", arg9="") -> tuple:
        # This looks kinda iffy, but it makes sense. I promise.
        # 
        # Technically, we just want to accept variables that we can
        # format and return a single, formatted string. But due to
        # how ComfyUI works, lists of strings can be plugged into
        # string inputs as if they were plain strings. What happens
        # then is that the system takes the length of the longest
        # list passed in, padding the other ones to the same length,
        # and calling the node's function for each entry. Finally,
        # these entries are then again returned as a list with the
        # longest length. This is not what we want for a simple
        # formatter.
        #
        # Instead, we set the input to be a list, which makes it so
        # process is only called once with all lists, which we can
        # handle as we see fit. We can also return whatever we want.
        # The caveat is that we need to handle the lists somehow,
        # so we flatten them all to one string. Easy!

        format = self.flatten(format)
        arg0 = self.flatten(arg0)
        arg1 = self.flatten(arg1)
        arg2 = self.flatten(arg2)
        arg3 = self.flatten(arg3)
        arg4 = self.flatten(arg4)
        arg5 = self.flatten(arg5)
        arg6 = self.flatten(arg6)
        arg7 = self.flatten(arg7)
        arg8 = self.flatten(arg8)
        arg9 = self.flatten(arg9)

        result = format.format(arg0=arg0, arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4, arg5=arg5, arg6=arg6, arg7=arg7, arg8=arg8, arg9=arg9)

        return (result,)

    def flatten(self, value: list) -> str:
        return " ".join([str(s) for s in value])


class ETTextFormatter2Node(ETTextFormatterNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "format": ("STRING", {"multiline": True}),
            },
            "optional": {
                "arg0": ("STRING", {"forceInput": True}),
                "arg1": ("STRING", {"forceInput": True}),
            }
        }


class ETTextFormatter5Node(ETTextFormatterNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "format": ("STRING", {"multiline": True}),
            },
            "optional": {
                "arg0": ("STRING", {"forceInput": True}),
                "arg1": ("STRING", {"forceInput": True}),
                "arg2": ("STRING", {"forceInput": True}),
                "arg3": ("STRING", {"forceInput": True}),
                "arg4": ("STRING", {"forceInput": True}),
            }
        }


class ETTextFormatter10Node(ETTextFormatterNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "format": ("STRING", {"multiline": True}),
            },
            "optional": {
                "arg0": ("STRING", {"forceInput": True}),
                "arg1": ("STRING", {"forceInput": True}),
                "arg2": ("STRING", {"forceInput": True}),
                "arg3": ("STRING", {"forceInput": True}),
                "arg4": ("STRING", {"forceInput": True}),
                "arg5": ("STRING", {"forceInput": True}),
                "arg6": ("STRING", {"forceInput": True}),
                "arg7": ("STRING", {"forceInput": True}),
                "arg8": ("STRING", {"forceInput": True}),
                "arg9": ("STRING", {"forceInput": True}),
            }
        }
