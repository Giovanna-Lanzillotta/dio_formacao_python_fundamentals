# Iteradores
# métodos especiais: __iter__()  e __next__()

#exemplo de código
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
    

    def __iter__(self):
        return self
    

    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration
        

# Uso do FileIterator
for line in FileIterator('large_file.txt'):
    print(line)