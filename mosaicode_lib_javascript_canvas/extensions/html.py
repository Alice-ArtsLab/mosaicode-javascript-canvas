# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate


class Html(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "canvas"
        self.language = "javascript"
        self.description = "Javascript / canvas code template"
        self.extension = ".html"
        self.command = "python -m webbrowser -t $dir_name$$filename$$extension$\n"
        self.code_parts = ["onload", "function", "declaration", "execution", "html"]
        self.code = r"""<html>
<head>
<meta http-equiv="Cache-Control" content="no-store" />
<title>Generated by Mosaicode</title>

<script>
var context = new (window.AudioContext || window.webkitAudioContext)();

$code[declaration]$

function loadme(){
$single_code[onload]$

return;
}

$single_code[function]$
$code[execution]$
$connections$
</script>
</head>

<body onload='loadme();'>
$code[html]$
</body>

</html>
"""

# -------------------------------------------------------------------------