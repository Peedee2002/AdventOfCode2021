from math import prod
import abc

class Packet:
    @abc.abstractclassmethod
    def get_value(self) -> int:
        pass

    @abc.abstractclassmethod
    def get_version(self) -> int:
        pass


class LiteralPacket(Packet):
    def __init__(self, version, string) -> None:
        self.version = version
        self.num, self.trimmed_str = LiteralPacket.__find_literal(string)
    def __find_literal(string) -> int:
        num = ""
        while string[0] == '1':
            num += string[1:5]
            string = string[5:]
        num += string[1:5]
        string = string[5:]
        num = int(num, 2)
        return num, string
    
    def get_version(self):
        return self.version
    
    def get_value(self):
        return self.num

class OperatorPacket(Packet):
    def __init__(self, version, string) -> None:
        from day16 import parse_packets
        self.version = version
        self.length_type_id = string[:1]
        string = string[1:]
        if self.length_type_id == '1':
            number_of_subpackets, string = OperatorPacket.__set_number_of_subpackets(string)
            self.packets, self.trimmed_str = parse_packets(string, number_of_subpackets)
        else:
            string_to_parse, self.trimmed_str = OperatorPacket.__set_length_of_subpackets(string)
            self.packets = parse_packets(string_to_parse)[0]

    def __set_number_of_subpackets(string) -> tuple[int, str]:
        return (int(string[:11], 2), string[11:])

    def __set_length_of_subpackets(string):
        end_of_parse = int(string[:15], 2)
        return string[15 :15 + int(string[:15], 2)], string[15 + end_of_parse:]

    def get_version(self) -> int:
        return self.version + sum(packet.get_version() for packet in self.packets)

class SumPacket(OperatorPacket):
    def get_value(self) -> int:
        return sum(packet.get_value() for packet in self.packets)

class ProductPacket(OperatorPacket):
    def get_value(self) -> int:
        return prod(packet.get_value() for packet in self.packets)

class MinPacket(OperatorPacket):
    def get_value(self) -> int:
        return min(packet.get_value() for packet in self.packets)

class MaxPacket(OperatorPacket):
    def get_value(self) -> int:
        return max(packet.get_value() for packet in self.packets)

class LessPacket(OperatorPacket):
    def get_value(self) -> int:
        return 1 if self.packets[0].get_value() < self.packets[1].get_value() else 0

class GreaterPacket(OperatorPacket):
    def get_value(self) -> int:
        return 1 if self.packets[0].get_value() > self.packets[1].get_value() else 0

class EqualPacket(OperatorPacket):
    def get_value(self) -> int:
        return 1 if self.packets[0].get_value() == self.packets[1].get_value() else 0