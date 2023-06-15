from django.utils import timezone


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = timezone.now()
        response = get_response(request, *args, **kwargs)
        end_time = timezone.now()
        print(f'(function) Executed in {end_time - start_time}')
        return response

    return middleware


class MeasureTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        start_time = timezone.now()
        response = self.get_response(request, *args, **kwargs)
        end_time = timezone.now()
        print(f'(class) Executed in {end_time - start_time}')
        return response
