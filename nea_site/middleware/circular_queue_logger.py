
from nea_site.settings import CIRCULAR_QUEUE_SIZE

# circular queue with recursive function
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] *size
        self.size = size
        self.head = 0
        self.tail = 0

    def _find_index(self, index):
        if self.queue[index] is not None:
            index = (index + 1) % self.size
            return self._find_index(index)
        return index

    def enqueue(self, item):
        if self.is_full():
            return False
        index = self._find_index(self.tail)
        self.queue[index] = item
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return item

    def is_full(self):
        return self.queue[self.tail] is not None

    def is_empty(self):
        return self.queue[self.head] is None

    def __repr__(self):
        return str(self.queue)

class CircularQueueMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.queue = CircularQueue( CIRCULAR_QUEUE_SIZE)

    def __call__(self, request):
        response = self.get_response(request)

        log = (request, response)
        self.queue.enqueue(log)

        if self.queue.is_full():
            self._write_to_file()

        return response

    def _write_to_file(self):
        with open("logs.txt", "a") as file:
            while not self.queue.is_empty():
                request, response = self.queue.dequeue()
                log = f"{request.method} {request.path} {request.user} {response.status_code}\n"
                file.write(log)
