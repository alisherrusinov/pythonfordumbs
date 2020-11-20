from django.shortcuts import render, HttpResponseRedirect
from .models import TestModel
import os


# Create your views here.
def index(request):
    return render(request, 'compiler/index.html')


def security_check(code: str):
    danger_modules = [
        'os',
        'sys',
        'pwd',
        'subprocess',
        'commands',
        'tarfile',
        'stat'
    ]
    for danger in danger_modules:
        if (f'import {danger}' in code):
            return False
        elif (f'from {danger} import' in code):
            return False
    return True


def editor(request):
    if (request.method == 'POST'):
        code = request.POST.get('code')
        is_secure = security_check(code)
        if (not is_secure):  # Если код небезопасный
            return render(request, 'compiler/editor.html', {'errors': 'Вы шакал сервак мне не надо ломать'})
        tests = TestModel.objects.all()
        for test in tests:
            input_text = test.test_input  # request.POST.get('input')
            correct_out = test.test_output

            file_name = 'testing.py'
            input_file = 'input.txt'
            error_file = 'error.txt'

            command = f'python3 {file_name} < {input_file} 2> {error_file}'

            file_code = open(file_name, 'w+')
            file_code.write(code)
            file_code.close()

            file_input = open(input_file, 'w+')
            file_input.write(input_text)
            file_input.close()

            os.popen(f'touch {error_file}')  # создать файл для вывода ошибок

            output = os.popen(command).read()[:-1]  # Нужен срез потому что при чтении вывода \
            # на конце будет перенос строки
            file_error = open(error_file, 'r')
            errors = file_error.read()

            os.popen(f'rm {file_name}')
            os.popen(f'rm {input_file}')
            os.popen(f'rm {error_file}')

            if (len(errors) == 0):
                if (output == correct_out):
                    continue
                else:
                    return render(request, 'compiler/editor.html',
                                  {'errors': f'Правильный вывод: {correct_out}\nВаш вывод: {output}'}
                                  )
            else:
                return render(request, 'compiler/editor.html', {'output': output, 'errors': errors})
        return render(request, 'compiler/editor.html', {'output': 'Все тесты пройдены успешно'})
    else:
        return render(request, 'compiler/editor.html')


def editor_without_tests(request):
    if (request.method == 'POST'):
        code = request.POST.get('code')
        is_secure = security_check(code)
        if (not is_secure):  # Если код небезопасный
            return render(request, 'compiler/editor.html', {'errors': 'Вы шакал сервак мне не надо ломать'})

        input_text = request.POST.get('input')

        file_name = 'testing.py'
        input_file = 'input.txt'
        error_file = 'error.txt'

        command = f'python3 {file_name} < {input_file} 2> {error_file}'

        file_code = open(file_name, 'w+')
        file_code.write(code)
        file_code.close()

        file_input = open(input_file, 'w+')
        file_input.write(input_text)
        file_input.close()

        os.popen(f'touch {error_file}')  # создать файл для вывода ошибок

        output = os.popen(command).read()
        file_error = open(error_file, 'r')
        errors = file_error.read()

        os.popen(f'rm {file_name}')
        os.popen(f'rm {input_file}')
        os.popen(f'rm {error_file}')

        if (len(errors) == 0):
            return render(request, 'compiler/editor.html', {'output': output})
        else:
            return render(request, 'compiler/editor.html', {'output': output, 'errors': errors})
    else:
        return render(request, 'compiler/editor.html')
