from FrontEndModule import FrontEndModule

def front_main():
    input_test = True
    output_test = True

    frontend_module = FrontEndModule()

    if input_test:
        print(frontend_module.get_input())

    a = input()
    if output_test:
        frontend_module.send_output('test_output.csv') #'Components/OutputComponent/test_output.csv')


if(__name__ == '__main__'):
    front_main()