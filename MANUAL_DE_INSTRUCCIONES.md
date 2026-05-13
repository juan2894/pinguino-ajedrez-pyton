# Manual de Instrucciones: Pingüino Ajedrecista 🐧♟️

¡Bienvenido al manual de usuario oficial de **Pingüino Ajedrecista**! Esta guía te enseñará todo lo necesario para instalar el juego, entender sus comandos y comenzar a jugar contra tu nuevo rival de inteligencia artificial (básica) en la terminal de tu computadora.

---

## Índice
1. [¿Qué es Pingüino Ajedrecista?](#1-qué-es-pingüino-ajedrecista)
2. [Instalación y Requisitos](#2-instalación-y-requisitos)
3. [Cómo Ejecutar el Juego](#3-cómo-ejecutar-el-juego)
4. [¿Cómo muevo las piezas? (Notación SAN)](#4-cómo-muevo-las-piezas-notación-san)
5. [Comandos Especiales y Atajos](#5-comandos-especiales-y-atajos)
6. [Resolución de Problemas Comunes](#6-resolución-de-problemas-comunes)

---

## 1. ¿Qué es Pingüino Ajedrecista?

Es un programa de ajedrez escrito en Python que se juega completamente desde la consola (terminal). Tú siempre juegas con las piezas **blancas** y el Pingüino Ajedrecista controla las piezas **negras**.

El Pingüino toma sus decisiones basándose en una jerarquía simple:
- Si puede dar jaque mate, lo hace.
- Si no, busca la captura de pieza que más puntos le otorgue.
- Si no puede capturar nada con ventaja, moverá una pieza de manera aleatoria.

## 2. Instalación y Requisitos

Para poder jugar, necesitas que tu computadora cumpla con dos requisitos muy sencillos.

**Paso 1: Instalar Python**
Debes tener instalado Python 3 en tu computadora. Si no lo tienes, puedes descargarlo de forma gratuita desde [python.org](https://www.python.org/downloads/).

**Paso 2: Instalar la biblioteca del tablero**
El juego requiere un paquete de código llamado `python-chess`. Para instalarlo, abre tu terminal (Símbolo del Sistema en Windows, Terminal en macOS/Linux) y escribe el siguiente comando:

```bash
pip install chess
```
*(Presiona Enter y espera a que termine la descarga).*

## 3. Cómo Ejecutar el Juego

Una vez que tengas Python y `chess` instalados:

1. Abre tu terminal.
2. Navega hasta la carpeta donde descargaste o guardaste el archivo `pinguino_ajedrecista.py`.
3. Escribe el siguiente comando y presiona Enter:

```bash
python pinguino_ajedrecista.py
```

El juego te dará la bienvenida y te mostrará el tablero inicial.

## 4. ¿Cómo muevo las piezas? (Notación SAN)

El juego utiliza el sistema oficial del ajedrez llamado **Notación Algebraica Estándar (SAN)**. A diferencia de jugar con un ratón, aquí debes escribir la coordenada a la que deseas mover.

### Las reglas básicas de escritura:
- **Peones:** Solo escribes la casilla a la que van. (Ej: `e4`, `d5`).
- **Otras piezas:** Llevan una letra mayúscula en inglés seguida de la casilla.
  - **N** = Caballo (kNight)
  - **B** = Alfil (Bishop)
  - **R** = Torre (Rook)
  - **Q** = Reina (Queen)
  - **K** = Rey (King)
- **Capturas:** Se indica con una `x`. (Ej: `Bxe5` = El Alfil captura lo que haya en e5). Si un peón captura, pones la letra de su columna de origen (Ej: `exd5`).
- **Enroques:** Se escriben con la letra O mayúscula.
  - `O-O` para enroque corto.
  - `O-O-O` para enroque largo.
- **Jaque / Mate:** `+` para Jaque, `#` para Jaque Mate (el programa a menudo los detecta automáticamente).

### Ejemplos prácticos:
- Mover el peón del rey dos casillas: Escribe `e4`
- Mover el caballo a f3: Escribe `Nf3`

## 5. Comandos Especiales y Atajos

Si cometes un error o quieres dejar de jugar, no tienes que mover una pieza, puedes escribir las siguientes palabras durante tu turno:

- `deshacer`: Deshace tu último movimiento y el movimiento de respuesta del Pingüino. El tablero regresará a como estaba antes de tu última decisión.
- `salir` o `quit`: Cierra el programa inmediatamente de forma amigable.

**Atajos de teclado rápidos:**
También puedes presionar `Ctrl + C` o `Ctrl + D` en tu teclado para interrumpir el juego y salir de manera instantánea en cualquier momento.

## 6. Resolución de Problemas Comunes

**"El juego dice: ¡Jugada o comando inválido!"**
Esto significa que lo que escribiste no es un movimiento legal o lo escribiste mal.
*Solución:* Revisa la ortografía (recuerda que la letra de la pieza va en mayúscula y la casilla en minúscula, ej. `Nf3`, no `nf3` ni `NF3`). Además, asegúrate de que esa pieza realmente pueda moverse a esa casilla según las reglas del ajedrez.

**"Me sale el error: ModuleNotFoundError: No module named 'chess'"**
*Solución:* Olvidaste instalar la biblioteca. Abre tu consola y escribe `pip install chess` antes de intentar jugar de nuevo.

**"No sé qué jugada hacer"**
¡Tranquilo! Puedes usar el comando `deshacer` para probar diferentes estrategias. El pingüino es benevolente.

---
¡Eso es todo! Prepárate, toma tus piezas blancas y ¡disfruta tu partida contra el Pingüino Ajedrecista!
