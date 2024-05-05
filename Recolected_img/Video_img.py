import cv2
import os


class CameraViewer:
    def __init__(self, camera, save_folder='saved_images'):
        self.cap = cv2.VideoCapture(camera)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
        self.dimensions_shown = False
        self.save_folder = save_folder
        self.image_count = 1201  # Contador para el número de imagen
        # Crear el directorio para guardar las imágenes si no existe
        os.makedirs(save_folder, exist_ok=True)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error en la cámara.")
                break
            

            if not self.dimensions_shown:
                self.display_frame_size(frame)
                self.dimensions_shown = True

            cv2.imshow("CAMERA", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord(' '):  # Si se presiona la tecla espacio
                self.save_image(frame)

        self.cap.release()
        cv2.destroyAllWindows()

    def display_frame_size(self, frame):
        height, width, channels = frame.shape
        print(f"Dimensiones del cuadro: Ancho = {width}, Altura = {height}, Canales = {channels}")

    def save_image(self, frame):
        """Guarda el cuadro actual en el folder especificado."""
        
        # Construir el nombre del archivo con el número de imagen
        filename = f"Metal_{self.image_count:04}.jpg"
        filepath = os.path.join(self.save_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"Imagen guardada en: {filepath}")
        # Incrementar el contador de imagen para la próxima imagen
        self.image_count += 1

if __name__ == "__main__":
    folder_path = "Recolected_img\Images\metal"
    viewer = CameraViewer(1, save_folder = folder_path)
    viewer.run()
