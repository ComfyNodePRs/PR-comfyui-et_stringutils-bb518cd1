ComfyUI - String Utils
=============================================================================

Collection of custom nodes for ComfyUI dedicated to the analysis and
transformation of text strings, such as for formatting and conversions
between types.

Nodes
-----------------------------------------------------------------------------

### Text Formatter

Several nodes with varying numbers of optional inputs that can be used
in conjunction with a formatting string to create the output. The node
uses standard [python string formatting][1].

**Example**
```text
Input:
- arg0: "John"
- arg1: 42

Format:
"Hello, {arg0}! Did you know? {arg1} is the answer to everything."

Output:
"Hello, John! Did you know? 42 is the answer to everything."
```

The nodes are useful to compose prompts based on variable inputs and
can be combined with [dynamic prompts][2] for even more flexibility.

### ATOI/ITOA

Two simple nodes to convert strings to integers and vice versa.


[1]: https://docs.python.org/3/tutorial/inputoutput.html
[2]: https://github.com/exectails/comfyui-et_dynamicprompts
