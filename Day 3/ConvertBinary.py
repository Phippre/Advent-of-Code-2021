def convertToDecimal(binary):
    return int(binary,2)

oxygen = convertToDecimal("010110010011")
scrubber = convertToDecimal("100111000110")

print(oxygen * scrubber)
