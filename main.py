import readV as rv
import operations as op


if __name__ == '__main__':
   lecture = rv.read()
   resultado = op.operation(lecture)
   print(resultado)