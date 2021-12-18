from numpy import binary_repr, inf

from packet import Packet, LessPacket, LiteralPacket, ProductPacket, SumPacket, MinPacket, MaxPacket, GreaterPacket, EqualPacket

def parse_version(string: str) -> int:
    return int(string[:3], 2)

def get_type(string: str):
    return int(string[3:6], 2)


def parse_packet(string: str) -> tuple[Packet, str]:
    version = parse_version(string)
    type = get_type(string)
    string = string[6:]
    match (type):
        case 4:
            new = LiteralPacket(version, string)
        case 0:
            new = SumPacket(version, string)
        case 1:
            new = ProductPacket(version, string)
        case 2:
            new = MinPacket(version, string)
        case 3:
            new = MaxPacket(version, string)
        case 5:
            new = GreaterPacket(version, string)
        case 6:
            new = LessPacket(version, string)
        case 7:
            new = EqualPacket(version, string)
    
    string = new.trimmed_str
    return new, string

def parse_packets(string: str, num_packets = inf) -> tuple[list[Packet], str]:
    packets = []
    while len(string) > 8 and len(packets) < num_packets:
        new, string = parse_packet(string)
        packets.append(new)
    return packets, string

if __name__ == '__main__':
    with open('input.in') as f:
        hex = f.readline()
    binary = binary_repr(int(hex, 16), (len(hex) - 1) * 4)
    packet = parse_packets(binary, 1)[0][0]
    print(packet)
    print(packet.get_value())
    print(packet.get_version())
