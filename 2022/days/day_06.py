from typing import List
from days.day_interface import DayBaseClass


class DaySix(DayBaseClass):

    def __find_index_of_first_non_repeating_sequence(self, sequences: List[str], length_of_unique_seq: int) -> int:
        for index, batch in enumerate(sequences):
            if len(set(batch)) == length_of_unique_seq:
                return index

    def __create_batched_signal_with_sliding_window(self, signal: str, batch_size: int, sliding_window: int) -> List[str]:
        return [signal[i:i+batch_size] for i in range(0, len(signal)-batch_size+sliding_window, sliding_window)]

    def part_one(self, input_file: str) -> int:
        signal = self.parse_input(input_file)
        batch_size = 4
        batched_signal = self.__create_batched_signal_with_sliding_window(
            signal, batch_size, sliding_window=1)
        index = self.__find_index_of_first_non_repeating_sequence(
            batched_signal, batch_size)
        return batch_size + index

    def part_two(self, input_file: str) -> int:
        signal = self.parse_input(input_file)
        batch_size = 14
        batched_signal = self.__create_batched_signal_with_sliding_window(
            signal, batch_size, sliding_window=1)
        index = self.__find_index_of_first_non_repeating_sequence(
            batched_signal, batch_size)
        return batch_size + index

    def parse_input(self, input_file: str) -> str:
        return super().parse_input(input_file)[0]
