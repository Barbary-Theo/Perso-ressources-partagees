import os as system
import pathlib


def to_red(text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(170, 0, 0, text)


class Server:

    def __init_(self, path):
        self.path = str(pathlib.Path().resolve()) + "/" + path

    def mkfifo(self):
        try:
            system.remove(self.path)
            system.mkfifo(self.path, 0o0600)
        except Exception as e:
            print(to_red(e.__str__()))


def prog():
    server = Server()
    server.path = "tube_test.fifo"
    server.mkfifo()

    pid = system.fork()

    if pid < 0:
        print(to_red(" -> Error to fork"))

    elif pid == 0:

        try:
            pipeline = open(server.path, "w")
            pipeline.write("je suis le fiston fréro")
            pipeline.close()

            print("done 2")
        except Exception as e:
            print(to_red(e.__str__()))

    else:
        try:
            pipeline = open(server.path, "w")
            pipeline.write("je suis le daron fréro")
            pipeline.close()

            print("done 1")
        except Exception as e:
            print(to_red(e.__str__()))

    print("oui")


if __name__ == "__main__":
    prog()
