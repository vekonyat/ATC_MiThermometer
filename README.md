# For testing only!

# Small modification of code for Xiaomi Mijia (LYWSD03MMC HW: [B1.4](https://github.com/pvvx/ATC_MiThermometer/tree/master/BoardPinout), [B1.6](https://github.com/pvvx/ATC_MiThermometer/issues/125), [B1.7](https://github.com/pvvx/ATC_MiThermometer/issues/145), [B1.9](https://github.com/pvvx/ATC_MiThermometer/issues/125))
# Use device as clock only

This fork contains modification of the custom firmware by pvvx for LYWSD03MMC Bluetooth Thermometer & Hygrometer device.

The lcd.c file is modified. The source code containes this modified file.


Please use the flasher by pvvx: - [TelinkMiFlasher.html](https://pvvx.github.io/ATC_MiThermometer/TelinkMiFlasher.html).

**Modification**

* After flashing the modified firmware, if the clock checkbox is selected, and the config is sent with the 'Send config' button, only clock will be shown on the screen.
* Changing screen is disabled.
* With unselecting the Clock ckeckbox and sending the config, the main screen will be active again.

|[Xiaomi Mijia (LYWSD03MMC)](https://pvvx.github.io/ATC_MiThermometer) |

|  <img src="https://tasmota.github.io/docs/_media/bluetooth/LYWSD03MMC.png" alt="Xiaomi Mijia (LYWSD03MMC)" width="160"/> |  

**The modified image:** ATC_Clock_or_Temp_35.bin

[LYWSD03MMC Modified Custom Firmware Version 3.5](https://github.com/vekonyat/ATC_MiThermometer/raw/master/ATC_Clock_or_Temp_35.bin) (HW: B1.4, B1.6, B1.7, B1.9)


**(Original) Custom Firmware Version:**

* [LYWSD03MMC Custom Firmware Version 3.5](https://github.com/pvvx/ATC_MiThermometer/raw/master/ATC_V35a.bin) (HW: B1.4, B1.6, B1.7, B1.9)

**Original Manufacturer Firmware Version**

* [Xiaomi LYWSD03MMC Original Firmware v1.0.0_0109)](https://github.com/pvvx/ATC_MiThermometer/raw/master/Original_OTA_Xiaomi_LYWSD03MMC_v1.0.0_0109.bin) (HW: B1.4 only)
* [Xiaomi LYWSD03MMC Original Firmware v1.0.0_0130)](https://github.com/pvvx/ATC_MiThermometer/raw/master/Original_OTA_Xiaomi_LYWSD03MMC_v1.0.0_0130.bin) (HW: B1.4..B1.9)



