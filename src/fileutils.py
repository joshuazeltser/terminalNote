def append_to_file(text, file_name, file_type):
    with open(f'{file_name}.{file_type}', 'a') as f:
        f.write(f"{text}\n")


def clear_file(file_name, file_type):
    open(f'{file_name}.{file_type}', 'w').close()
