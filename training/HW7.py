# TASK 1
import functools


def retry(attempts=5, desired_value=None):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print(f"Не вдалося досягнути бажаного значення {desired_value} за {attempts} спроб")
            return None

        return wrapper_retry

    return decorator_retry


# TASK 2
def copy_file(source_path, target_path):
    with open(source_path, 'rb') as source_file:
        with open(target_path, 'wb') as target_file:
            target_file.write(source_file.read())


# TASK 3
def process_file(file_path):
    num_lines = 0
    file_size = 0
    char_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            num_lines += 1
            file_size += len(line.encode())
            for char in line:
                if char != '\n' and char != ' ':
                    if char not in char_counts:
                        char_counts[char] = 1
                    else:
                        char_counts[char] += 1

    top_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    top_chars = [char for char, count in top_chars]
    return {
        'num_lines': num_lines,
        'file_size': file_size,
        'top_chars': top_chars
    }
