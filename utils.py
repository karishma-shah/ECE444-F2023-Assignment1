class Utils:
    @staticmethod
    def reversed(num):
        return int(str(num)[::-1])
    
    @staticmethod
    def formatter(num):
        binary = bin(num)
        octal = oct(num)
        return (binary, octal)
