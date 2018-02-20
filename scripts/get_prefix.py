import re

def get_prefix(filename,suffix):
    """
    Strip the suffix from a filename
    """
    s = re.search("^(.*)%s"%(suffix),filename)
    prefix = s.group(1)
    return prefix

if __name__=="__main__":
    print("Do not run this script directly")

