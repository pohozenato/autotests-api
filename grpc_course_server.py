from dataclasses import dataclass
from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import course_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом

@dataclass
class CourseItem:
    course_id: str
    title: str = "Автотесты API"
    description: str = "Будем изучать написание API автотестов"

# Реализация gRPC-сервиса
class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса UserService"""

    def GetCourse(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetCourse для курса: {request.course_id}')
        course_item = CourseItem(course_id=request.course_id)
        #course_list = [f"{x}: {y}" for x, y in course_item.__dict__.items()]
        # Формируем и возвращаем ответное сообщение
        return course_service_pb2.GetCourseResponse(course_id=course_item.course_id, title=course_item.title, description=course_item.description)


# Функция для запуска gRPC-сервера
def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем сервис UserService на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()
