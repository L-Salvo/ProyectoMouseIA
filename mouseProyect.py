import cv2
import mediapipe as mp
import pyautogui as pag

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Seleccionar indice de la camara
cap = cv2.VideoCapture(0)

# Obtener el tamaño de la pantalla
screen_width, screen_height = pag.size()


with mp_hands.Hands(
    static_image_mode=False,  # Falso porque vamos a utilizar un video
    max_num_hands=1,
    min_detection_confidence=0.9) as hands:
    
    while True:
        ret, frame = cap.read() 
        if not ret:
            break
        
        # Cambiar el tamaño del frame a 1920x1080
        frame_resized = cv2.resize(frame, (screen_width, screen_height))
        frame_resized = cv2.flip(frame_resized, 1)
        
        height, width, _ = frame_resized.shape  # Obtener dimensiones del fotograma
        frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB) 
        
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:  # Si se detectó una mano, hacer lo siguiente:
            for hand_landmarks in results.multi_hand_landmarks:
                x1 = int(hand_landmarks.landmark[9].x * screen_width)
                y1 = int(hand_landmarks.landmark[9].y * screen_height)
                cv2.circle(frame_resized, (x1, y1), 3, (0,0,255), 3)
                
                pag.moveTo(x1, y1)
                # Mover el mouse a la posición detectada
                #pag.moveTo(x1, y1)
                
        
        # Mostrar el frame
        #cv2.imshow("Cámara del Celular", frame_resized)
        
        # Salir si se presiona 'ESC'
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

        
        
        
    
        
    
