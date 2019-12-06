import gpio as gp


salida_led = gp.Gpio(0)
salida_led.set_state(True)


print(salida_led.get_state())

