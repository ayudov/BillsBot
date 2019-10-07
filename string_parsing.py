from pyparsing import Word, alphas, ZeroOrMore, Suppress, Optional, nums

rus_alphas = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
com_name = Word(rus_alphas)('command')
# full_module_name = (col_name + col_name))('modules')
text_spend = (Suppress('-') + Word(nums+','+nums))('text')
text_comment = (Suppress('-') + Word(rus_alphas + ', ' + rus_alphas))('text')
# parse_module = (Suppress('import') + full_module_name + import_as).setParseAction(lambda t: {'import': t.modules.asList(), 'as': t.import_as.asList()[0]})
command = com_name + text_spend + com_name + text_comment

def parse_string(x: str):
    res = command.parseString(x).asList()
    return res