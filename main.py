from seq import Seq
from fasta_reader import FastaReader


def demo_seq_class():
    """Демонстрация работы класса Seq"""
    print("=== ДЕМОНСТРАЦИЯ КЛАССА Seq ===")

    # Создаём тестовые последовательности
    protein_seq = Seq("sp|P12345|TEST_PROTEIN", "MAGWHIMSICALSEQUENCE")
    dna_seq = Seq("chr1:100-200", "ATCGATCGATCG")

    # Демонстрируем методы класса Seq
    print("1. Белковая последовательность:")
    print(protein_seq)
    print(f"   Длина: {len(protein_seq)}")
    print(f"   Алфавит: {protein_seq.get_alphabet()}")

    print("\n2. ДНК последовательность:")
    print(dna_seq)
    print(f"   Длина: {len(dna_seq)}")
    print(f"   Алфавит: {dna_seq.get_alphabet()}")


def demo_fasta_reader():
    """Демонстрация работы класса FastaReader"""
    print("\n" + "=" * 50)
    print("=== ДЕМОНСТРАЦИЯ КЛАССА FastaReader ===")

    # Создаём объект FastaReader
    reader = FastaReader("test.fasta")

    # Проверяем валидность файла
    print(f"Файл valid: {reader.is_valid_fasta()}")

    # Читаем и выводим все записи
    print("\nЗаписи из FASTA файла:")
    for i, record in enumerate(reader.read_records(), 1):
        print(f"\n{i}. {record.header}")
        print(f"   Последовательность: {record.sequence[:30]}...")  # Показываем первые 30 символов
        print(f"   Длина: {len(record)}")
        print(f"   Алфавит: {record.get_alphabet()}")


if __name__ == "__main__":
    demo_seq_class()
    demo_fasta_reader()