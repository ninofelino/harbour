from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x1504,
                          idProduct=0x0006
                          inputEndPoint=0x82,
                          outputEndPoint=0x01) # Create the printer object with the connection params

# Print a image
printer.image('/home/shantanu/companylogo.gif')

printer.text("Hello World")