import re

def get_prefix(filename,suffix):
    """
    Strip the suffix from a filename
    """
    s = re.search("^(.*)%s"%(suffix),filename)
    prefix = s.group(1)
    return prefix

