from UISelenium import *


#     "start":(url)
#     "step1":(click,),
#     "step2":(get_element_by_id('id'),),
#     "step3":(click(get_element_by_id)
#
#
#
from types import *
def instruction_parser_from_file(filename='testcases.txt'):
    instruction_list = []
    with open(filename) as file:
        ii = ''
        for line in file.readlines():
            formatted_line = line.replace('\n', '')
            if 'nextstep' in line:
                instruction_list.append(ii)
                ii = ''
            else:
                ii += formatted_line
    return instruction_list


def steps_from_instructions(instruction_parsed_from_file):

    if isinstance(instruction_parsed_from_file, list):
        instruction = instruction_parser_from_file()
        list_append = []
        for i in instruction:
            list_append.append(i.split(','))
        return list_append
    else:
       raise TypeError

print(steps_from_instructions(instruction_parser_from_file()))