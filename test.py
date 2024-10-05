class CarEngine:
    def __init__(self):
        self.ignition_on = False
        self.key_position = "off"
        self.rpm = 0
        self.temperature = 90
        self.oil_pressure = 40
        self.warning_lights = {"oil_pressure": False, "coolant_temperature": False}
        self.battery_voltage = 12

    def start_engine(self, ignition_on, key_position):
        if ignition_on and key_position == "start" and self.battery_voltage > 0:
            self.ignition_on = True
            self.rpm = 1000
            return True
        else:
            return False

    def accelerate(self, pedal_position):
        if self.ignition_on:
            self.rpm += pedal_position * 100
            if self.rpm > 6000:
                self.rpm = 6000  # Limiting RPM to a maximum value

    def decelerate(self, pedal_position):
        if self.ignition_on:
            self.rpm -= pedal_position * 100
            if self.rpm < 0:
                self.rpm = 0  # Prevent RPM from going negative

    def get_rpm(self):
        return self.rpm

    def get_temperature(self):
        return self.temperature

    def get_oil_pressure(self):
        return self.oil_pressure

    def get_warning_lights(self):
        return self.warning_lights

    def set_oil_pressure(self, pressure):
        self.oil_pressure = pressure
        self.warning_lights["oil_pressure"] = pressure < 30

    def set_coolant_temperature(self, temperature):
        self.temperature = temperature
        self.warning_lights["coolant_temperature"] = temperature > 120

    def get_battery_voltage(self):
        return self.battery_voltage

    def stop_engine(self):
        self.ignition_on = False
        self.rpm = 0

    def idle(self):
        if self.ignition_on:
            self.rpm = 500

    def get_status(self):
        return "on" if self.ignition_on else "off"

    def get_fuel_injection_status(self):
        return "ok"

    def get_air_filter_status(self):
        return "clean"

    def get_spark_plug_status(self):
        return "ok"

    def get_crankshaft_position_sensor_status(self):
        return "ok"

    def get_camshaft_position_sensor_status(self):
        return "ok"

    def get_throttle_position_sensor_status(self):
        return "ok"

def test_car_engine():
    engine = CarEngine()

    # Test Case 1: Verify that the engine starts when the ignition is turned on and the key is in the "start" position.
    assert engine.start_engine(ignition_on=True, key_position="start") == True

    # Test Case 2: Verify that the engine does not start when the ignition is turned off.
    assert engine.start_engine(ignition_on=False, key_position="start") == False

    # Test Case 3: Verify that the engine RPM increases when the accelerator pedal is pressed.
    engine.accelerate(pedal_position=50)
    assert engine.get_rpm() > 1000

    # Test Case 4: Verify that the engine RPM decreases when the accelerator pedal is released.
    engine.decelerate(pedal_position=50)
    assert engine.get_rpm() < 1000

    # Test Case 5: Verify that the engine temperature remains within a safe range during operation.
    assert 80 < engine.get_temperature() < 120

    # Test Case 6: Verify that the engine oil pressure is within a safe range during operation.
    assert 30 < engine.get_oil_pressure() < 60

    # Test Case 7: Verify that the engine warning lights turn on when the oil pressure is low.
    engine.set_oil_pressure(20)
    assert engine.get_warning_lights()["oil_pressure"] == True

    # Test Case 8: Verify that the engine warning lights turn off when the oil pressure returns to normal.
    engine.set_oil_pressure(40)
    assert engine.get_warning_lights()["oil_pressure"] == False

    # Test Case 9: Verify that the engine speed governor prevents the engine from exceeding a maximum RPM.
    engine.accelerate(pedal_position=100)
    assert engine.get_rpm() <= 6000

    # Test Case 10: Verify that the engine idle speed is within a safe range.
    engine.idle()
    assert 500 <= engine.get_rpm() < 1000

    # Test Case 11: Verify that the engine shuts off when the ignition is turned off.
    engine.stop_engine()
    assert engine.get_status() == "off"

    # Test Case 12: Verify that the engine does not start when the battery is dead.
    engine.battery_voltage = 0
    assert engine.start_engine(ignition_on=True, key_position="start") == False

    # Test Case 13: Verify that the battery voltage is correctly reported.
    assert engine.get_battery_voltage() == 0

    # Test Case 14: Verify that the coolant temperature warning light turns on when temperature exceeds safe levels.
    engine.set_coolant_temperature(130)
    assert engine.get_warning_lights()["coolant_temperature"] == True

    # Test Case 15: Verify that the coolant temperature warning light turns off when temperature returns to normal.
    engine.set_coolant_temperature(100)
    assert engine.get_warning_lights()["coolant_temperature"] == False

    print("All test cases passed!")

test_car_engine()
