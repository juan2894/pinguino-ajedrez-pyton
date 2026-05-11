# -*- coding: utf-8 -*-

"""
==============================================================================
                            PINGÜINO AJEDRECISTA (MOTOR DE AJEDREZ)
==============================================================================
Descripción:
Este programa es "Pingüino Ajedrecista", un motor de ajedrez básico que utiliza la
biblioteca 'python-chess'. Pingüino Ajedrecista decide su próxima jugada basándose en
una jerarquía de reglas predefinidas:
1.  Si puede dar jaque mate, lo hace.
2.  Si no, busca la mejor captura posible según un sistema de puntuación.
3.  Si no hay capturas, realiza un movimiento legal aleatorio.

Autor: Desarrollado bajo la solicitud del usuario para el proyecto Pingüino Ajedrecista.
Fecha: 2025-09-16
Uso: Ejecutar el script en una terminal. El programa permitirá al usuario 
     (jugando con las blancas) introducir jugadas en notación SAN (ej. e4, Nf3).
     Pingüino Ajedrecista responderá con su jugada para las negras.
==============================================================================
"""

import chess
import random
import math

# ==============================================================================
# DEFINICIÓN DE VARIABLES Y CONSTANTES DE EVALUACIÓN
# ==============================================================================

# --- Valores base de las piezas del oponente para incentivar la captura ---
# Estos valores se usan para puntuar la pieza que se va a comer.
PIECE_VALUES_CAPTURE = {
    chess.PAWN: 100,
    chess.KNIGHT: 300,
    chess.BISHOP: 300,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 3900  # Valor teórico, ya que el rey no puede ser capturado.
}

# --- Valores de riesgo de nuestras propias piezas ---
# Estos valores se restan si la pieza que usamos para capturar puede ser 
# recapturada por el oponente.
PIECE_VALUES_RISK = {
    chess.PAWN: 130,
    chess.KNIGHT: 390,
    chess.BISHOP: 390,
    chess.ROOK: 650,
    chess.QUEEN: 1170,
    chess.KING: 5070
}

# --- Bonificaciones por la posición de la casilla a atacar ---
# Se utiliza un diccionario para mapear el índice de la casilla a su valor.
POSITIONAL_SCORES = {}

# Casillas centrales (valor +12)
for square in ['d4', 'e4', 'd5', 'e5']:
    POSITIONAL_SCORES[chess.parse_square(square)] = 12

# Anillo interior (valor +6)
for square in ['c3', 'd3', 'e3', 'f3', 'c4', 'f4', 'c5', 'f5', 'c6', 'd6', 'e6', 'f6']:
    POSITIONAL_SCORES[chess.parse_square(square)] = 6

# Anillo exterior (valor +3)
for square in ['b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'b3', 'g3', 'b4', 'g4', 
               'b5', 'g5', 'b6', 'g6', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7']:
    POSITIONAL_SCORES[chess.parse_square(square)] = 3


# ==============================================================================
# FUNCIONES DEL MOTOR
# ==============================================================================

def evaluate_capture(board, move):
    """
    Calcula la puntuación de una jugada de captura según las reglas definidas.
    
    Args:
        board (chess.Board): El estado actual del tablero.
        move (chess.Move): El movimiento de captura a evaluar.
        
    Returns:
        int: La puntuación calculada para la captura.
    """
    score = 0
    
    # 1. Identificar la pieza atacante y la pieza capturada
    attacking_piece = board.piece_at(move.from_square)
    captured_piece = board.piece_at(move.to_square)
    
    # Caso especial: Captura al paso (en passant)
    if captured_piece is None and board.is_en_passant(move):
        captured_piece = chess.Piece(chess.PAWN, not board.turn)

    if attacking_piece is None or captured_piece is None:
        return -math.inf # Movimiento inválido o no es captura

    # 2. Sumar el valor base de la pieza capturada
    score += PIECE_VALUES_CAPTURE.get(captured_piece.piece_type, 0)
    
    # 3. Sumar la bonificación por posición de la casilla de destino
    score += POSITIONAL_SCORES.get(move.to_square, 0)
    
    # 4. Evaluar el riesgo: Si la pieza atacante puede ser recapturada
    # Creamos un tablero temporal para ver el estado *después* de la jugada
    temp_board = board.copy()
    temp_board.push(move)
    
    # Si la casilla donde ahora está nuestra pieza es atacada por el oponente,
    # restamos el valor de riesgo de nuestra pieza.
    if temp_board.is_attacked_by(not board.turn, move.to_square):
        score -= PIECE_VALUES_RISK.get(attacking_piece.piece_type, 0)

    # 5. Evaluar control de la casilla (defensores y atacantes)
    # Contamos cuántas piezas nuestras defienden la casilla ANTES del movimiento
    own_defenders = len(board.attackers(board.turn, move.to_square))
    score += own_defenders * 24

    # Contamos cuántas piezas del oponente atacan la casilla ANTES del movimiento
    opponent_attackers = len(board.attackers(not board.turn, move.to_square))
    score -= opponent_attackers * 25
    
    # 6. Bonificación por proximidad de los reyes
    opponent_king_square = board.king(not board.turn)
    own_king_square = board.king(board.turn)
    
    if chess.square_distance(opponent_king_square, move.to_square) == 1:
        score += 3
        
    if chess.square_distance(own_king_square, move.to_square) == 1:
        score += 3
        
    return score


def find_best_move(board):
    """
    Encuentra la mejor jugada para el turno actual basándose en la jerarquía 
    de decisiones del motor.
    
    Args:
        board (chess.Board): El estado actual del tablero.
        
    Returns:
        chess.Move: El mejor movimiento encontrado.
    """
    legal_moves = list(board.legal_moves)
    
    # --- PRIORIDAD 1: Buscar un jaque mate ---
    for move in legal_moves:
        # Hacemos el movimiento en un tablero temporal para no alterar el original
        temp_board = board.copy()
        temp_board.push(move)
        if temp_board.is_checkmate():
            print("Pingüino Ajedrecista: ¡Encontré un jaque mate!")
            return move

    # --- PRIORIDAD 2: (No implementada explícitamente, ver nota) ---
    # La lógica de "disminuir la probabilidad de jaque mate" del oponente
    # requeriría una búsqueda más profunda (minimax). Este motor prioriza
    # la agresión a través de capturas valiosas, lo que indirectamente puede
    # desbaratar los planes del oponente.

    # --- PRIORIDAD 3: Buscar la mejor captura ---
    best_capture = None
    max_score = -math.inf  # Inicializamos con un valor muy bajo

    capture_moves = [move for move in legal_moves if board.is_capture(move)]
    
    if capture_moves:
        for move in capture_moves:
            score = evaluate_capture(board, move)
            if score > max_score:
                max_score = score
                best_capture = move
        
        if best_capture:
            print(f"Pingüino Ajedrecista: Mejor captura encontrada: {board.san(best_capture)} con puntaje: {max_score}")
            return best_capture

    # --- SI NO HAY PRIORIDADES, JUGADA ALEATORIA ---
    # Si no se encontró un mate ni una captura, se elige un movimiento legal al azar.
    print("Pingüino Ajedrecista: No hay mates ni capturas. Realizando un movimiento aleatorio.")
    return random.choice(legal_moves)


# ==============================================================================
# FUNCIÓN PRINCIPAL Y BUCLE DEL JUEGO
# ==============================================================================

if __name__ == "__main__":
    # Creamos un objeto Board que representa el tablero de ajedrez
    board = chess.Board()
    
    print("=========================================")
    print("   Bienvenido a Pingüino Ajedrecista (Ajedrez)")
    print("=========================================")
    print("Tú juegas con las piezas blancas.")
    print("Introduce tus jugadas en notación SAN (ej. e4, Nf3, Bxe5).")
    print(board)
    
    import sys

    # Bucle principal del juego
    try:
        while not board.is_game_over():
            if board.turn == chess.WHITE:  # Turno del jugador
                try:
                    # Pedir jugada al usuario
                    move_san = input("Tu jugada (blancas): ").strip()

                    # Comandos de utilidad
                    if move_san.lower() in ['salir', 'quit']:
                        print("\nSaliendo del juego. ¡Hasta pronto!")
                        sys.exit(0)
                    elif move_san.lower() == 'deshacer':
                        if len(board.move_stack) >= 2:
                            board.pop() # Deshace el movimiento del motor (negras)
                            board.pop() # Deshace tu movimiento (blancas)
                            print("\nSe han deshecho los dos últimos movimientos.")
                            print("\n" + str(board))
                            print("-----------------------------------------")
                        else:
                            print("\nNo hay suficientes movimientos para deshacer.")
                        continue

                    # El método `parse_san` convierte la notación a un objeto Move
                    move = board.parse_san(move_san)
                    # Ejecuta el movimiento en el tablero
                    board.push(move)
                except ValueError:
                    print("¡Jugada o comando inválido! Inténtalo de nuevo.")
                    continue
            else:  # Turno del motor (negras)
                print("\nTurno de Pingüino Ajedrecista (negras)...")
                # El motor busca su mejor jugada
                engine_move = find_best_move(board)
                print(f"Pingüino Ajedrecista juega: {board.san(engine_move)}")
                # Ejecuta la jugada del motor
                board.push(engine_move)

            # Imprimir el tablero después de cada jugada
            print("\n" + str(board))
            print("-----------------------------------------")

        # Mensaje de fin de partida
        print("\n¡Fin del juego!")
        print("Resultado: " + board.result())

    except (KeyboardInterrupt, EOFError):
        print("\n\nJuego interrumpido. ¡Hasta pronto!")
        sys.exit(0)
