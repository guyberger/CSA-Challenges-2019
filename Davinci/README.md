# Da vinci
We get a .pcap file so firstly we want to examine it in Wireshark.

## Identifying the device
Looking at the data transfer we see that there are lots of URB DEVICE packets which indicate that the packets are coming from a USB device.
To find which one we can examine "GET DESCRIPTOR Respone DEVICE" which is the device recognition packet.
Under "DEVICE DESCRIPTOR" we find:
> idProduct: CTL-471 [Bamboo Splash, One by Wacom (S)] (0x0300)

Now we know which device is used to send the packets, it is a drawpad connected via USB.

## Extracting information
The information transmitted is stored in the URB_INTERRUPT packets, speicfally in the "Leftover Capture Data".
Since we are only interested in these packets we can use the filter:
> usb.capdata

Note that the packets of length 37 are irrelevant and are used as a system validation of some sort.

After that we can extract the data using "File -> Export Packet Dissection -> As "C" Arrays.

## Image extraction
Now that we have the data we can start to mimic the drawpad by plotting the (x, y) coordinates as described in the solve.py file.

### Flag:
> CSA{Ju5T_1ik3_LeOn4rd0_d4_ViNc1}
