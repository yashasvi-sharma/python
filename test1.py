import time
import random

class CarEngineTest:
    def __init__(self):
        self.start_time = None
        self.idle_rpm = 700
        self.max_rpm = 6000
        self.temperature = 90  # degrees Celsius
        self.oil_pressure = 30  # PSI
        self.fuel_consumption = 0.5  # liters/hour
        self.vibration = 1.0  # G-force
        self.noise_level = 70  # dB
        self.charging_voltage = 14  # Volts
        self.exhaust_emissions = {'CO2': 0.02, 'NOx': 0.005}  # example values
        self.sensors = {
            'crankshaft': True,
            'oxygen': True
        }

    def start_engine(self):
        self.start_time = time.time()
        print("Engine started.")

    def stop_engine(self):
        stop_time = time.time() - self.start_time
        print(f"Engine stopped after {stop_time:.2f} seconds.")
        return stop_time

    def test_idle_speed_stability(self):
        stable = self.idle_rpm >= 650 and self.idle_rpm <= 750
        print(f"Idle RPM stability: {'Pass' if stable else 'Fail'}")
        return stable

    def test_acceleration_response(self):
        response_time = random.uniform(0.5, 1.5)  # simulated response time in seconds
        print(f"Acceleration response time: {response_time:.2f} seconds.")
        return response_time

    def test_max_rpm(self):
        print(f"Max RPM reached: {self.max_rpm}")
        return self.max_rpm

    def test_fuel_consumption(self):
        print(f"Fuel consumption rate: {self.fuel_consumption:.2f} liters/hour.")
        return self.fuel_consumption

    def test_emissions(self):
        emissions_pass = self.exhaust_emissions['CO2'] < 0.03 and self.exhaust_emissions['NOx'] < 0.01
        print(f"Exhaust emissions: {'Pass' if emissions_pass else 'Fail'}")
        return emissions_pass

    def test_oil_pressure(self):
        pressure_ok = self.oil_pressure > 25 and self.oil_pressure < 50
        print(f"Oil pressure consistency: {'Pass' if pressure_ok else 'Fail'}")
        return pressure_ok

    def test_temperature_stability(self):
        temp_stable = self.temperature >= 85 and self.temperature <= 100
        print(f"Temperature stability: {'Pass' if temp_stable else 'Fail'}")
        return temp_stable

    def test_vibration_levels(self):
        vibration_ok = self.vibration < 2.0
        print(f"Vibration levels: {'Pass' if vibration_ok else 'Fail'}")
        return vibration_ok

    def test_noise_levels(self):
        noise_ok = self.noise_level < 75
        print(f"Noise levels: {'Pass' if noise_ok else 'Fail'}")
        return noise_ok

    def test_battery_charging_efficiency(self):
        charging_ok = self.charging_voltage >= 13.5 and self.charging_voltage <= 14.5
        print(f"Battery charging efficiency: {'Pass' if charging_ok else 'Fail'}")
        return charging_ok

    def test_sensors(self):
        sensors_ok = all(self.sensors.values())
        print(f"Sensors operation: {'Pass' if sensors_ok else 'Fail'}")
        return sensors_ok

    def run_all_tests(self):
        self.start_engine()
        time.sleep(2)  # Simulate engine running time
        results = {
            "Idle Speed Stability": self.test_idle_speed_stability(),
            "Acceleration Response": self.test_acceleration_response(),
            "Max RPM": self.test_max_rpm(),
            "Fuel Consumption": self.test_fuel_consumption(),
            "Emissions": self.test_emissions(),
            "Oil Pressure": self.test_oil_pressure(),
            "Temperature Stability": self.test_temperature_stability(),
            "Vibration Levels": self.test_vibration_levels(),
            "Noise Levels": self.test_noise_levels(),
            "Battery Charging Efficiency": self.test_battery_charging_efficiency(),
            "Sensors Operation": self.test_sensors()
        }
        self.stop_engine()
        return results

# Example of running the tests
engine_test = CarEngineTest()
results = engine_test.run_all_tests()
for test, result in results.items():
    print(f"{test}: {'Pass' if result else 'Fail'}")
