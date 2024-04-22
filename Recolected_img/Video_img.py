import cv2 as cv
import os
import time 

class CameraViewer:
    def __init__(self, camera,show_fps=True, save_folder='saved_images'):
        self.cap = cv.VideoCapture(camera)
        self.display_rgb = True
        self.dimensions_shown = False
        self.save_folder = save_folder
        self.show_fps = show_fps
        self.image_count = 0  # Contador para el número de imagen
        # Crear el directorio para guardar las imágenes si no existe
        self.start_time = time.time()  # Iniciar el temporizador
        self.frames = 0 
        os.makedirs(save_folder, exist_ok=True)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error en la cámara.")
                break
            
            self.frames += 1
            if self.show_fps:
                self.show_fps_on_frame(frame)
            #fps = self.frames / elapsed_time
            #cv.putText(frame, f"FPS: {fps:.2f}", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if not self.dimensions_shown:
                self.display_frame_size(frame)
                self.dimensions_shown = True

            cv.imshow("CAMERA", frame)
            key = cv.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord(' '):  # Si se presiona la tecla espacio
                self.save_image(frame)

        self.cap.release()
        cv.destroyAllWindows()

    def display_frame_size(self, frame):
        """Imprime las dimensiones del cuadro capturado."""
        height, width, channels = frame.shape
        print(f"Dimensiones del cuadro: Ancho = {width}, Altura = {height}, Canales = {channels}")

    def show_fps_on_frame(self, frame):
        """Calcula y muestra los FPS en el frame."""
        # Calcular los FPS
        elapsed_time = time.time() - self.start_time
        fps = self.frames / elapsed_time

        # Mostrar los FPS en el frame
        cv.putText(frame, f"FPS: {fps:.2f}", (5, 22), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    def save_image(self, frame):
        """Guarda el cuadro actual en el folder especificado."""
        
        # Construir el nombre del archivo con el número de imagen
        filename = f"Coins_{self.image_count:03}.jpg"
        filepath = os.path.join(self.save_folder, filename)
        cv.imwrite(filepath, frame)
        print(f"Imagen guardada en: {filepath}")
        # Incrementar el contador de imagen para la próxima imagen
        self.image_count += 1

if __name__ == "__main__":
    folder_path = 'Folder/path'
    viewer = CameraViewer(0,show_fps=False, save_folder = folder_path)
    viewer.run()
