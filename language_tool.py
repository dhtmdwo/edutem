import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
# text = u'My naem is Peter.'
# matches = tool.check(text)
# print(len(matches))
# print(matches[0].replacements[0])
# print(matches[0].offset)
# print(matches[0].errorLength)


def correction(sent):
    matches = tool.check(sent)
    c_sent = sent
    for i in range(len(matches)):
        word = sent[matches[i].offset:matches[i].offset +
                    matches[i].errorLength]
        # print(word)
        try:
            c_sent = sent.replace(word, matches[i].replacements[0])

        except:
            print(sent + ' Error')

    return c_sent
    # print(c_sent)


text = 'My naem is Peter'
correction(text)
