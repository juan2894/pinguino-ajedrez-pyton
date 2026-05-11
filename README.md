# Pingüino Médico 🐧🏥♟️

Pingüino Médico es un motor de ajedrez básico escrito en Python utilizando la biblioteca `python-chess`.

Este proyecto fue creado como respuesta a una solicitud para construir un programa de ajedrez simple pero funcional, capaz de jugar partidas en la terminal contra un usuario humano.

## 📋 Características

- **Juego por consola:** Interactúa con el usuario a través de la terminal usando notación SAN (ej. `e4`, `Nf3`, `Bxe5`).
- **Motor de toma de decisiones jerárquico:** Pingüino Médico decide sus movimientos basándose en las siguientes prioridades:
  1. **Jaque Mate:** Si existe un movimiento que resulta en jaque mate inmediato, lo ejecutará sin dudarlo.
  2. **Captura Estratégica:** Si no hay jaque mate disponible, evaluará todas las capturas legales posibles usando un sistema de puntuación que considera:
     - El valor de la pieza capturada (ej. una Reina vale más que un Peón).
     - La bonificación por la posición de destino (control del centro).
     - El riesgo de que la pieza atacante sea recapturada.
     - El control de la casilla (cuántos defensores propios y atacantes enemigos hay).
     - La proximidad a los Reyes.
  3. **Movimiento Aleatorio:** Si no hay capturas ventajosas ni jaque mate, realizará un movimiento legal completamente aleatorio.

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener **Python 3** instalado en tu sistema, así como la biblioteca `python-chess`.

1.  **Clona o descarga este repositorio.**
2.  **Instala la dependencia principal:**

    Puedes instalar `python-chess` usando `pip`:

    ```bash
    pip install chess
    ```

## 🚀 Cómo jugar

Para iniciar una partida contra Pingüino Médico, ejecuta el script principal en tu terminal:

```bash
python pinguino_medico.py
```

El juego comenzará. Tú jugarás con las piezas **blancas** y el motor (Pingüino Médico) jugará con las **negras**.

Cuando sea tu turno, deberás introducir tu jugada en **Notación Algebraica Estándar (SAN)**.
- *Ejemplos:* `e4`, `Nf3`, `O-O` (enroque corto), `Bxe5` (captura con alfil).

El tablero se imprimirá en la terminal después de cada movimiento, mostrando el estado actual de la partida.

## 🧠 Lógica Interna (Evaluación de Capturas)

La función `evaluate_capture` es el corazón de la toma de decisiones secundarias del motor. Asigna una puntuación a cada movimiento de captura basándose en:
- `PIECE_VALUES_CAPTURE`: El incentivo por capturar una pieza enemiga.
- `POSITIONAL_SCORES`: Bonificaciones por mover piezas hacia el centro del tablero.
- `PIECE_VALUES_RISK`: Penalizaciones si la pieza de Pingüino Médico queda expuesta a ser capturada en la nueva casilla.
- Control defensivo/ofensivo de la casilla de destino.

## 👨‍💻 Autor
Desarrollado según los requerimientos del usuario. ¡Disfruta jugando contra Pingüino Médico!
