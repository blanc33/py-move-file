import os


def move_file(command: str) -> None:
    command_list = command.replace("/", " ").split(" ")
    _, start_f, *finish_f = command_list
    if len(finish_f) == 1:
        os.rename(start_f, finish_f[0])
        return
    add_path = ""
    for part_path in finish_f[:-1]:
        add_path = os.path.join(add_path, part_path)
        try:
            os.mkdir(add_path)
        except FileExistsError:
            pass
    add_path = os.path.join(add_path, finish_f[-1])
    with open(start_f, "r") as start_obj, open(add_path, "w") as finish_obj:
        finish_obj.write(start_obj.read())
    os.remove(start_f)
