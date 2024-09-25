class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} is now ON.")
        else:
            print(f"{self.name} is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} is now OFF.")
        else:
            print(f"{self.name} is already OFF.")

    def reset(self):
        self.is_on = False
        print(f"{self.name} has been reset.")

class SmartLight(SmartDevice):
    def __init__(self, name, brightness=100):
        super().__init__(name)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print(f"{self.name} brightness set to {self.brightness}%.")

    def turn_off(self):
        super().turn_off()

    def reset(self):
        super().reset()
        self.brightness = 100
        print(f"{self.name} brightness reset to {self.brightness}%.")

class SmartThermostat(SmartDevice):
    def __init__(self, name, temperature=72):
        super().__init__(name)
        self.temperature = temperature

    def turn_on(self):
        super().turn_on()
        print(f"{self.name} temperature set to {self.temperature}°F.")

    def turn_off(self):
        super().turn_off()

    def reset(self):
        super().reset()
        self.temperature = 72
        print(f"{self.name} temperature reset to {self.temperature}°F.")

class SmartCamera(SmartDevice):
    def __init__(self, name, recording=False):
        super().__init__(name)
        self.recording = recording

    def turn_on(self):
        super().turn_on()
        self.recording = True
        print(f"{self.name} is now recording.")

    def turn_off(self):
        super().turn_off()
        self.recording = False
        print(f"{self.name} has stopped recording.")

    def reset(self):
        super().reset()
        self.recording = False
        print(f"{self.name} recording reset.")

def main():
    devices = {
        "living_room_light": SmartLight("Living Room Light"),
        "bedroom_thermostat": SmartThermostat("Bedroom Thermostat"),
        "front_door_camera": SmartCamera("Front Door Camera")
    }

    while True:
        try:
            command = input("Enter command (turn_on, turn_off, reset, exit): ").strip().lower()
            if command == "exit":
                break

            device_name = input("Enter device name: ").strip().lower()
            if device_name in devices:
                device = devices[device_name]
                if command == "turn_on":
                    device.turn_on()
                elif command == "turn_off":
                    device.turn_off()
                elif command == "reset":
                    device.reset()
                else:
                    print("Invalid command.")
            else:
                print("Device not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
