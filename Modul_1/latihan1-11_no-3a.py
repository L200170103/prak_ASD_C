#No3
def jmlVokal(string):
    vkl = 0
    a = "Kartasura"
    for car in string.lower():
        if car in a:
            vkl += 1
    vokal = len(string)
    return(vokal,vkl)
