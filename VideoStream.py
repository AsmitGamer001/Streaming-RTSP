class VideoStream:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'rb')
        except:
            raise IOError
        self.frameNum = 0

    def nextFrame(self):
    

        length_bytes = self.file.read(4)
        if len(length_bytes) < 4:
            return None

        framelength = int.from_bytes(length_bytes, byteorder='big')


        data = self.file.read(framelength)
        self.frameNum += 1
        return data

    def frameNbr(self):

        return self.frameNum