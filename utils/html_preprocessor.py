from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class CodeBlockPreprocessor(Preprocessor):
    CODE_BLOCK_RE = re.compile(r'```(\w+)?\n(.*?)```', re.DOTALL)

    def run(self, lines):
        text = "\n".join(lines)
        def replacer(match):
            language = match.group(1) or 'plaintext'
            code = match.group(2)
            return f'<pre data-enlighter-language="{language}">{code}</pre>'
        
        return self.CODE_BLOCK_RE.sub(replacer, text).split("\n")


class CustomCodeBlockExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(CodeBlockPreprocessor(md), 'custom_code_block', 25)