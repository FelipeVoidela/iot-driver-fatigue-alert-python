import cv2                          # OpenCV: captura de vídeo e exibição
import mediapipe as mp             # MediaPipe: detecção de pontos faciais
# import serial                      # Comunicação com Arduino via porta serial
import time                        # Usado para dar tempo de inicializar o Arduino

# Inicia conexão com o Arduino (ajuste a porta conforme necessário)
# arduino = serial.Serial('COM4', 9600, timeout=1)
# time.sleep(2)  # Aguarda o Arduino iniciar

# Inicializa o detector de malha facial
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(max_num_faces=1)
mp_draw = mp.solutions.drawing_utils

# 0 Usa a webcam
cap = cv2.VideoCapture(0) 

# Variáveis de controle
frames_fechado = 0
status = "Aguardando..."
cor_status = (255, 255, 255) 

# Limiar com histerese:
LIMIAR_FECHAR = 0.38    # Se EAR cair abaixo disso, olho considerado fechado
LIMIAR_ABRIR = 0.42     # Se EAR subir acima disso, olho considerado aberto
LIMIAR_COCHILO = 30     # Número de frames com olho fechado = cochilo

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Espelha o vídeo
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = face_mesh.process(rgb)

    if resultados.multi_face_landmarks:
        pontos = resultados.multi_face_landmarks[0].landmark

        # Desenha a malha facial
        mp_draw.draw_landmarks(
            frame,
            resultados.multi_face_landmarks[0],
            mp_face.FACEMESH_TESSELATION,
            landmark_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
            connection_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1)
        )

        # Cálculo do EAR com 6 pontos do olho direito (lado esquerdo da imagem)
        h = abs(pontos[33].x - pontos[133].x)
        v1 = abs(pontos[159].y - pontos[145].y)
        v2 = abs(pontos[158].y - pontos[153].y)
        ear = (v1 + v2) / (2.0 * h)

        

        # Detecção face
        if ear <= LIMIAR_FECHAR:
            frames_fechado += 1

            if frames_fechado == 3:
                status = "Piscando"
                cor_status = (0, 255, 255) 
                print(status)
                # arduino.write(b'Y')

            elif frames_fechado >= LIMIAR_COCHILO:
                status = "COCHILO DETECTADO!"
                cor_status = (0, 0, 255)  
                print(status)
                # arduino.write(b'R')

        elif ear > LIMIAR_ABRIR:
            frames_fechado = 0
            status = "Aguardando piscada"
            cor_status = (0, 255, 0)  
            print(status)
            # arduino.write(b'G')

        # Exibe o texto acima do status atual
        cv2.putText(frame, "Status:", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Exibe o status na tela com a cor correspondente
        cv2.putText(frame, status, (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, cor_status, 2)

    # Exibe o vídeo
    cv2.imshow("Detector de Sonolência", frame)

    # Encerra com a tecla 'q' ou esc
    if cv2.waitKey(30) & 0xFF in [ord('q'), 27]:
        break

# Finaliza tudo
cap.release()
# arduino.close()
cv2.destroyAllWindows()
