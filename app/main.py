import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3 or command_list[0] != "mv":
        return
    _, source_file, destination_file = command_list

    if destination_file.endswith("/") or os.path.isdir(destination_file):
        destination_file = os.path.join(
            destination_file, os.path.basename(source_file)
        )

    if not os.path.dirname(destination_file):
        os.rename(source_file, destination_file)
        return

    os.makedirs(os.path.dirname(destination_file), exist_ok=True)

    with (open(source_file, "r") as start_obj,
          open(destination_file, "w") as finish_obj):
        finish_obj.write(start_obj.read())
    os.remove(source_file)
