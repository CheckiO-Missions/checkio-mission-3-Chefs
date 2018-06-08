init_code = """
if not "ItalianCook" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ItalianCook'?")

ItalianCook = USER_GLOBAL['ItalianCook']

if not "JapaneseCook" in USER_GLOBAL:
    raise NotImplementedError("Where is 'JapaneseCook'?")

JapaneseCook = USER_GLOBAL['JapaneseCook']

if not "RussianCook" in USER_GLOBAL:
    raise NotImplementedError("Where is 'RussianCook'?")

RussianCook = USER_GLOBAL['RussianCook']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "Clients": [
        prepare_test(middle_code='''client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)''',
                     test="client_1.total()",
                     answer="Sushi: 40, Tea: 20, Total: 60"),

        prepare_test(middle_code='''client_2 = JapaneseCook()
client_2.add_food(1, 65)
client_2.add_drink(4, 10)
client_2.add_drink(2, 5)''',
                     test="client_2.total()",
                     answer="Sushi: 65, Tea: 50, Total: 115"),

        prepare_test(middle_code='''client_3 = RussianCook()
client_3.add_food(3, 30)
client_3.add_drink(4, 5)
client_3.add_food(1, 50)''',
                     test="client_3.total()",
                     answer="Dumplings: 140, Compote: 20, Total: 160"),

        prepare_test(middle_code='''client_4 = RussianCook()
client_4.add_food(2, 25)
client_4.add_food(2, 50)
client_4.add_drink(2, 10)
client_4.add_drink(2, 15)''',
                     test="client_4.total()",
                     answer="Dumplings: 150, Compote: 50, Total: 200"),

        prepare_test(middle_code='''client_5 = ItalianCook()
client_5.add_food(6, 25)
client_5.add_drink(5, 10)''',
                     test="client_5.total()",
                     answer="Pizza: 150, Juice: 50, Total: 200"),

        prepare_test(middle_code='''client_6 = ItalianCook()
client_6.add_food(2, 10)
client_6.add_drink(2, 10)
client_6.add_food(4, 25)
client_6.add_drink(5, 4)''',
                     test="client_6.total()",
                     answer="Pizza: 120, Juice: 40, Total: 160")
    ]

}
