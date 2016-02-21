import re
from StringIO import StringIO


class Translator(object):
    EOF = ''
    START_BLOCK = '{% block '
    END_BLOCK = '{% endblock %}'

    # FIXME need a strip after findall
    REG_BLOCK_NAME = re.compile(r"(?<={% block ).*(?= %})")

    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self._fp = open(self.filepath)
        self._current_line = self._fp.xreadlines()
        self._line_num = 0

        self.data = {
            'subject': '',
            'content': '',
            'style': '',
            'javascript': '',
            'is_inherited': True,
        }

        return self

    def _advance(self):
        try:
            self.peek = self._current_line.next()
        except StopIteration:
            self.peek = self.EOF
        else:
            self._line_num += 1
            # print 'peek-> ', self.peek[:-1]

    def translate(self):
        self._advance()

        while not self.peek == self.EOF:
            self._skip_blank_line()
            self._parse_block()

        return self.data

    def _skip_blank_line(self):
        while not self.peek == self.EOF and self.peek.isspace():
            self._advance()

    def _parse_block(self):
        if self.peek.startswith(self.START_BLOCK):
            k, v = self._swallow()
            self.data[k] = v
        else:
            self.error('Content must in a block', line=self.peek.strip())

    def _swallow(self):
        k = self.REG_BLOCK_NAME.findall(self.peek)[0].strip()
        cache = StringIO()

        while not self.peek == self.EOF and \
              not self.peek.startswith(self.END_BLOCK):

            self._advance()

            if self.peek.startswith(self.START_BLOCK):
                self.error('Content not in a closure block',
                           line=self.peek.strip())
            elif self.peek.startswith(self.END_BLOCK):
                break
            else:
                cache.write(self.peek)

        v = cache.getvalue()
        cache.close()

        # skip the {% end block %}
        self._advance()
        return k, v

    def error(self, msg='Invalid syntax', **extra):
        extra.update(line_num=self._line_num)
        print '\nTranslate Error:'
        print 'Line {line_num}: {line}'.format(**extra)
        print '%s' % msg
        exit(1)

    def __exit__(self, exc_type, exc_value, traceback):
        self._fp.close()
