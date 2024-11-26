class ETATOI:
    """
    A node that converts a string to an integer.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("integer",)

    CATEGORY = "exectails/Strings"
    FUNCTION = "process"

    def process(self, text: str) -> tuple:
        return (int(text),)


class ETITOA:
    """
    A node that converts an integer to a string.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "integer": ("INT", {"default": 0, "min": -2000000000, "max": 2000000000}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails/Strings"
    FUNCTION = "process"

    def process(self, integer: int) -> tuple:
        return (str(integer),)
