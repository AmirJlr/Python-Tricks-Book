# with is related to "Context Manager" Concept

class ContextManager:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class FileManager:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


fm = FileManager('sample.txt', 'r')
with fm as file:  # file = fm.__enter__()
    print(file.readline())
    raise ValueError()
    # fm.__exit__()

print(file.closed)
