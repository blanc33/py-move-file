import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3 or command_list[0] != "mv":
        return
    _, source_file, destiny_file = command_list
    if not os.path.dirname(destiny_file):
        os.rename(source_file, destiny_file)
        return

    os.makedirs(os.path.dirname(destiny_file), exist_ok=True)

    with (open(source_file, "r") as start_obj,
          open(destiny_file, "w") as finish_obj):
        finish_obj.write(start_obj.read())
    os.remove(source_file)
