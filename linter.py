from os import sep

from SublimeLinter.lint import WARNING, ComposerLinter


class Phpmd(ComposerLinter):
    regex = (
        r'(.+):(?P<line>\d+)\s*(?P<message>.+)$'
    )

    default_type = WARNING

    defaults = {
        'selector': 'embedding.php, source.php',
        'rulesets': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }

    def cmd(self):
        rulesets = self.settings.get('rulesets')
        rulesets = rulesets.replace('\\', sep)
        rulesets = rulesets.replace('/', sep)
        cmd = ['phpmd', '${file}', 'text', rulesets]

        return cmd
