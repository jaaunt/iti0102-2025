"""Route all the packets."""


class Packet:
    """Packet class."""

    def __init__(self, content: str, source_ip: str, destination_ip: str, id: int, sequence_number: int):
        """Initialize packet class."""
        self.content = content
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.id = id
        self.sequence_number = sequence_number

    def __repr__(self) -> str:
        """
        Represent packet.

        Format the string of the packet as:
        '[content] from [source_ip] to [destination_ip] ([id]:[sequence_number])'
        """
        return f"{self.content} from {self.source_ip} to {self.destination_ip} ({self.id}:{self.sequence_number})"


class EndDevice:
    """End device class."""

    def __init__(self):
        """
        Initialize end device.

        End device will have an IP address if they are connected to a router.
        Also, end device will collect all packets that are sent to them.
        """
        self.ip_address = ""
        self.packet_history = []

    def get_ip_address(self) -> str:
        """Return the current IP address of the device."""
        return self.ip_address

    def set_ip_address(self, ip_address: str) -> None:
        """
        Set an IP address for the device.

        You don't need to validate the IP address here.
        """
        self.ip_address = ip_address

    def add_packet(self, packet: Packet) -> None:
        """Add a packet to end device."""
        self.packet_history.append(packet)

    def clear_packet_history(self) -> None:
        """Clear all packets from history."""
        self.packet_history.clear()

    def get_all_packets(self) -> list[Packet]:
        """Get a list of all packets in the order they were added."""
        return self.packet_history

    def get_all_packets_by_id(self, given_id: int) -> list[Packet]:
        """Get a list of all packets that have the given ID."""
        result = []
        for packet in self.packet_history:
            if packet.id == given_id:
                result.append(packet)
        return result

    def get_all_packets_by_source_ip(self, given_ip: str) -> list[Packet]:
        """Get a list of all packets that have given source IP."""
        result = []
        for packet in self.packet_history:
            if packet.source_ip == given_ip:
                result.append(packet)
        return result


class Router:
    """Router class."""

    def __validate_ipv4(self, ip_address: str) -> bool:
        """Validate IPv4."""
        parts = ip_address.split(".")
        if len(parts) != 4 or not ip_address.endswith(".1"):
            return False
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):  # no letter no neg number or bigger num
                return False
            if not part == "0" and part.startswith("0"):   # no .001. bs
                return False
        return True
    # making sure it doesnt initialize router w a non valid ip

    def __init__(self, ip_address: str):
        """
        Initialize router.

        IP address must be a string in the format "x.x.x.1"
        where x is a number in the range [0, 255], such as "192.168.0.1".

        If the IP address does not match this criteria, set the IP address to "192.168.0.1".

        The first 3 sections ("192.168.0" in this example) form a subnet. You will need this later!
        """
        if not self.__validate_ipv4(ip_address) or not ip_address.endswith(".1"):  # idk kas seda lopu osa on veel vaja kuna see kontrollib juba aga if it aint broke dont fix it
            ip_address = "192.168.0.1"  # kui pole valid annab default address
        self.ip_address = ip_address
        self.devices = []  # holds connceted devices

    def get_ip_address(self) -> str:
        """Return the current IP address of the router."""
        return self.ip_address

    def generate_ip_address(self) -> str:
        """
        Generate a valid IP address.

        The IP address must be in the router's subnet.
        This means that the first 3 sections of the IP address must be the same as in the router's IP.

        The final section can be a random number in the range [2, 254].

        Make sure you can't generate an IP address that's already in use by a device!

        If there are no possible IP addresses to generate, raise an IPv4AddressSpaceExhaustedException().
        """
        subnet = ".".join(self.ip_address.split(".")[:-1])  # first 3 parts remove last kuna essa osa peab match
        used_ips = {  # set kasutatud ip-dest vaatab lopu juppi, so aint 1 2 jne selles
            int(device.get_ip_address().split(".")[-1])
            for device in self.devices if device.get_ip_address()  # vaatab llabi koik device listis if osa selleks et aint valid ip address
        }
        for ip_end in range(2, 255):  # 0 cant ja 1 on router oma
            if ip_end not in used_ips:  # kui pole kasutusel
                return f"{subnet}.{ip_end}"  # paneb router essa jupi otsa leitud lopu

        raise IPv4AddressSpaceExhaustedException()  # kui rohkem ruumi pole enam aka after 255

    def add_device(self, device: EndDevice) -> bool:
        """
        Add end device to router.

        The same device can not be added twice.
        Each device should be assigned an unique IP address in the correct subnet.

        The method should return True if device was added, else False.
        """
        if device in self.devices:  # kui juba on olemas
            return False

        ip_address = self.generate_ip_address()  # teeb talle ip address
        device.set_ip_address(ip_address)  # set ip address function lic assignib ip addressi deviceile
        self.devices.append(device)  # paneb listi kirja
        return True

    def remove_device(self, device: EndDevice) -> bool:
        """
        Remove an end device from the router.

        If a device is removed from the router, then the router can no longer send
        packets to the device and the device's IP address is set to an empty string.

        The method should return True if device was removed, else False.
        """
        if device in self.devices:  # tootab aint ss kui uldse on listis
            device.set_ip_address("")  # votab selle ip addressi ara
            self.devices.remove(device)  # votab listist valja
            return True
        return False

    def get_devices(self) -> list[EndDevice]:
        """Get all devices that are connected to the router in the order they were connected."""
        # Write your code here
        return self.devices

    def get_device_by_ip(self, ip: str) -> EndDevice | None:
        """
        Get a device by given IP.

        If there is no device with given IP, then return None.
        Otherwise return the found device.
        """
        for device in self.devices:
            if device.get_ip_address() == ip:  # annab device kui ip match
                return device
        return None

    def receive_packet(self, packet: Packet) -> None:
        """
        Receive a packet from the Internet.

        If there is a device with the destination IP in this subnet then forward this packet to this device.
        Otherwise drop this packet. (don't do anything with it)
        """
        device = self.get_device_by_ip(packet.destination_ip)  # otsib device mis on ruuteriga uhendatud packeti destination ipga
        if device:
            device.add_packet(packet)  # kui see leitakse ss lisab packeti historisse


class IPv4AddressSpaceExhaustedException(Exception):
    """Raised when there are no more available IP addresses."""


if __name__ == "__main__":
    """Main for testing the functions."""
    # Initialize router
    router = Router("192.168.1.1")
    print(router.get_ip_address())  # 192.168.1.1
    print(router.get_devices())     # []
    print()

    # Initialize end devices
    device1 = EndDevice()
    device2 = EndDevice()
    print(f"{device1.get_ip_address()!a}")     # ''
    print()

    # Add devices to router
    print(router.add_device(device1))   # True
    print(router.add_device(device1))   # False (no duplicates allowed)
    print(router.add_device(device2))   # True
    print(len(router.get_devices()))    # 2
    print()

    # Check generated IP addresses
    print(device1.get_ip_address().startswith("192.168.1."))                # True (correct subnet)
    print(1 < int(device1.get_ip_address().split(".")[-1]) < 255)           # True (correct ending)
    print(device1.get_ip_address() == device2.get_ip_address())             # False (different IP addresses generated)
    print(router.get_device_by_ip(device1.get_ip_address()) == device1)     # True
    print()

    # Create packet from device1 to device2
    packet1 = Packet("message1", device1.get_ip_address(), device2.get_ip_address(), 1, 1)
    print(packet1)                          # message1 from 192.168.1.[some number] to 192.168.1.[some number](1:1)
    router.receive_packet(packet1)          # (this should send packet to device2)
    print(len(device2.get_all_packets()))   # 1
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets_by_id(1)))    # 1
    print(len(device2.get_all_packets_by_source_ip(device1.get_ip_address())))  # 1
    print()

    # Create packet from device1 to unknown destination
    packet2 = Packet("message2", device1.get_ip_address(), "10.0.255.44", 2, 1)
    router.receive_packet(packet2)          # (this should drop the packet)
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets()))   # 1
    print()

    # Remove end device from router
    print(router.remove_device(device1))    # True
    print(router.remove_device(device1))    # False (already removed)
    print(f"{device1.get_ip_address()!a}")  # ''
    print(len(router.get_devices()))        # 1
