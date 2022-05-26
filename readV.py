import cv2
import easyocr

def read():
    op = int(input("""Selecciona la forma de lectura del problema:
1) Imagen
2) Teclado  
Opcion: """))

    if op == 1:
        return imagen()
    elif op ==2:
        return teclado()
    else: 
        print("Selecciona una opcion válida")



def imagen():
    reader = easyocr.Reader(["en"], gpu=True)
    inp = input("\nEscribe el nombre de tu imagen: ")
    image = cv2.imread(inp)
    result = reader.readtext(image)

    print(f'\nLa operación leida es: {result[0][1]}\n')

    print("\nPresiona enter para continuar")
    show(image, result)
    
    aux = result[0][1]
    return aux.replace(' ','')


def show(image, result):
    for res in result:
        pt0 = res[0][0]
        pt1 = res[0][1]
        pt2 = res[0][2]
        pt3 = res[0][3]

        cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
        cv2.putText(image, res[1], (pt0[0], pt0[1] - 3), 2, 0.8, (0,0,0), 1)
        cv2.putText(image,"Presiona enter para continuar", (pt3[0], pt3[1] + 50), 2, 0.8, (0,0,0), 1)

        cv2.rectangle(image, pt0, pt2,(166,56,242), 2)
        cv2.circle(image, pt0, 2,(255,0, 0), 2)
        cv2.circle(image, pt1, 2,(255,0, 0), 2)
        cv2.circle(image, pt2, 2,(255,0, 0), 2)
        cv2.circle(image, pt3, 2,(255,0, 0), 2)
        text = res[1]

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
def teclado():
    prob = input("\nEscribe tu problema: ")
    return prob.replace(' ', '')
    