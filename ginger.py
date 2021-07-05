from gingerit.gingerit import GingerIt


def Ginger_tool(text):

    # text = 'My naem is Peter.'
    parser = GingerIt()
    Ginger = parser.parse(text)
    return Ginger['result']
    # print(Ginger)


# text = 'Becuse, I cannt see the moon, I amm happies.'
# Ginger_tool(text)
