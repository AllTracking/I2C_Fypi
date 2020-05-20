from machine import I2C, Pin
Slave_Add = 16
Answer_Size = 2
data = b'9'
i2c = I2C( 0 , scl=Pin(13), sda=Pin(12), freq=100000)
RX_Data = i2c.readfrom(Slave_Add, Answer_Size)
print(RX_Data)
