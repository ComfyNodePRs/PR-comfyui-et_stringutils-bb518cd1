class ETATOI:
    """
    A node that converts a string to an integer.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("integer",)

    CATEGORY = "exectails"
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
                "integer": ("INT", {"default": 0}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails"
    FUNCTION = "process"

    def process(self, integer: int) -> tuple:
        return (str(integer),)
