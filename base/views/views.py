from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
from django.views.decorators.cache import cache_page



# def main(request):
#     return HttpResponse('Сайт о задачах пользователя и помощи их организации.')


# def user_tasks(request):
#     return HttpResponse("Задачи пользователя.")

# def index(request):
#     return render(request, "tasks.html")


# tasks = [{"task": "some task", "status":"started", "category": "work"}]
# users = [{"name": "some name", "age": 22, "phone": "some phone"}]

# def task(request):
#     header = "Задачи пользователей"
#     tasks = [tasks] = [{"task": "завтрак", "status": "начат", "category": "важно",
#                         "task1": "играть в лего", "status1": "активен", "category1": "досуг",
#                         "task2": "тренировка", "status2": "предстоит", "category2": "здоровье",
#                         "task3": "работа", "status3": "завершен", "category3": "важно"
#                         }]
#
#     context = {"header": header, "tasks": tasks}
#     return render(request, 'tasks.html', context=context)


@cache_page(60 * 30, cache='default')
def users(request):
    header = "Пользователи и информация о них"
    users = [users] = [{"name": "Олег", "name1": "Саша", "name2": "Оля", "name3": "Коля",
                        "age": 20, "age1": 10, "age2": 42, "age3": 30,
                        "phone": +375291111110, "phone1": +375291111112, "phone2": +375291111111, "phone3": +375291111117
                        }]

    context = {"header": header, "users": users}
    sleep(10)
    return render(request, 'users.html', context=context)
