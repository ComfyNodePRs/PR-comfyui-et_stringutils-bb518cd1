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

The nodes are useful to compose prompts based on variable inputs and
can be combined with [dynamic prompts][2] for even more flexibility.

**Example**

Insert values into a string.

Format
```text
"Hello, {arg0}! Did you know? {arg1} is the answer to everything."
```

Input
```text
arg0: "John"
arg1: 42
```

Output
```text
"Hello, John! Did you know? 42 is the answer to everything."
```

### ATOI/ITOA

Two simple nodes to convert strings to integers and vice versa.

### Python Text Script

A node that takes a number of inputs as well as a Python script that
takes the given arguments to produce a result. Intended as a brute-
force method in cases where a general purpose formatter might not
cut it and no dedicated node is available. The value assigned to
the `result` variable inside the script will be returned by the
node.

**Example**

Return a description based on a numeric input.

Script
```python
age = int(arg0)

if age < 13:
    result = "a nice child"
elif age < 22:
    result = "an angsty teenager"
else:
    result = "a mature adult"
```

Input
```text
arg0: 17
```

Onput
```text
"an angsty teenager"
```


[1]: https://docs.python.org/3/tutorial/inputoutput.html
[2]: https://github.com/exectails/comfyui-et_dynamicprompts
