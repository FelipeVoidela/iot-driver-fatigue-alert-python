#  **Sistema de Alerta de Sonolência para Motoristas** 🔐

## Descrição

O **Sistema de Alerta de Sonolência para Motoristas** é uma aplicação desenvolvida para **prevenir acidentes** causados por sonolência e distração no trânsito. O sistema utiliza a **detecção de piscadas** e a **postura da cabeça** para identificar sinais de **fadiga** em motoristas. Quando detecta sonolência, o sistema envia **alertas visuais** e **sonoros** através de LEDs coloridos e um buzzer para alertar o motorista, ajudando a evitar acidentes.

---

##  **Tecnologias**

- **OpenCV**: Captura de vídeo e exibição em tempo real.
- **MediaPipe**: Usado para detectar pontos faciais (malha facial) e a postura da cabeça.
- **Arduino**: Controla LEDs e o buzzer para alertas físicos.

---

##  **Como Funciona**

O sistema detecta **piscadas** dos motoristas através da análise da **Taxa de Aspect Ratio do Olho (EAR)**, utilizando a biblioteca MediaPipe. Quando o motorista pisca repetidamente ou mantém os olhos fechados por muito tempo, o sistema identifica sinais de sonolência. A **postura da cabeça** também é monitorada para garantir que o motorista esteja atento à estrada.

###  **Fases de Alerta:**

- **LED Verde**: O motorista está alerta (sem sinais de sonolência).
- **LED Amarelo**: O motorista está começando a mostrar sinais de sonolência.
- **LED Vermelho + Buzzer**: Sonolência detectada, alerta urgente para o motorista.

---

##  **Aplicações Reais**

Este sistema pode ser utilizado em diversos contextos, como:

- **Motoristas de caminhão**
- **Motoristas de ônibus**
- **Motoristas de carros de longo percurso**

Esses motoristas frequentemente enfrentam longos períodos de direção, e o sistema pode ajudar a **prevenir acidentes** causados por **fadiga**.

---

##  **Como Rodar**

### Requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `opencv-python`
  - `mediapipe`
- **Arduino**: Para controlar os LEDs e o buzzer.

### Instalação de Dependências (Python)

Para instalar as bibliotecas necessárias, basta executar o seguinte comando:

```bash
pip install opencv-python mediapipe
