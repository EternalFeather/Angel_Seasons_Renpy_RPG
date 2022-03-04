
init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def parse_monologue(path):
        """Parses a monologue text file at the given path.
        Returns a list of section objects.
        """
        import re
        import itertools
        
        file = renpy.file(path)
        text = (s.decode('utf-8').rstrip('\r\n') for s in file)
  
        sections = list()
        def section_key_fn(line):
            section_match = re.match(r'^=+(.*)$', line)
            if section_match:
                section = object()
                section.lines = list()
                section.options = section_match.group(1).strip()
                sections.append(section)

            return sections[-1] if sections else None
        
        for section, lines in itertools.groupby(text, key=section_key_fn):
            
            if section is None: break
            
            next(lines)
            buffered = list()
            
            flag = False
            for line in lines:
                if re.match(r'^-+$', line):
                    flag = not flag
                    continue

                if not line:
                    if section.lines:
                        buffered.append((flag, ['']))
                        continue
                else:
                    section.lines += buffered
                    del buffered[:]
                    section.lines.append(
                        (flag, line.split('\t') if line else (flag, [''])))
        
        file.close()
        return sections
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
