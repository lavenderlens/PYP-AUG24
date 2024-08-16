# ensure that the command line prompt is in this dir before executing

file = open("data.txt", mode='w')
# x creates, raises error if exists
# w overwrites
# a append

# 1.write()
text = "\n\nadditional content\nadditional content\nadditional content\n"
file.write(text)

# 2.writelines()
file.writelines(text)

file.close()