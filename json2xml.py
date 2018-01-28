def dictRecursion(recData):
    xmlstr = ""

    for key in recData.keys():
        if type(recData[key]) == dict:
            open = '<{0}>'.format(key)
            close = '</{0}>'.format(key)
            xmlstr += '{0}{1}{2}'.format(open, dictRecursion(recData[key]), close)
        else:
            open = '<{0}>'.format(key)
            close = '</{0}>'.format(key)
            xmlstr += '{0}{1}{2}'.format(open, recData[key], close)
    return xmlstr
