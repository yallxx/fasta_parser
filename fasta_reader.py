from seq import Seq


class FastaReader:


    def __init__(self, file_path: str):

        self.file_path = file_path

    def is_valid_fasta(self) -> bool:

        try:
            with open(self.file_path, 'r') as file:
                first_line = file.readline().strip()

                return first_line.startswith('>')
        except (FileNotFoundError, IOError):
            return False

    def read_records(self):

        try:
            with open(self.file_path, 'r') as file:
                current_header = ""
                current_sequence = ""

                for line in file:
                    line = line.strip()

                    if line.startswith('>'):

                        if current_header:
                            yield Seq(current_header, current_sequence)


                        current_header = line[1:]  # Убираем '>'
                        current_sequence = ""
                    else:

                        current_sequence += line


                if current_header:
                    yield Seq(current_header, current_sequence)

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except IOError:
            raise IOError(f"Ошибка чтения файла {self.file_path}")