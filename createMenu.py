#
def createMenu(optionList):
  tmp=""
  ct=1
  for opt in optionList:
    tmp+=str(ct)+". "+opt+"\n"
    ct+=1
  return tmp
