# Mouse Circle Mover

Script en Python que mueve el mouse en un movimiento circular continuo alrededor de la posición actual del cursor.

## Requisitos

- Python 3.x
- Windows (utiliza `ctypes` para acceder a la API de Windows)

No se requieren dependencias externas.

## Uso

Simplemente ejecuta el script:

```bash
python main.py
```

El mouse comenzará a moverse en un círculo alrededor de la posición donde se encuentre el cursor. Para detener el script, presiona `Ctrl+C`.

## Configuración

Las siguientes variables en [main.py](main.py) permiten modificar el comportamiento del movimiento:

| Variable | Línea | Descripción | Valor por defecto |
|----------|-------|-------------|-------------------|
| `radio` | 7 | Radio del círculo en píxeles | 20 |
| `time_step` | 8 | Tiempo de espera entre cada paso del movimiento (segundos) | 0.003 |
| `interval` | 9 | Tiempo de espera entre cada círculo completado (segundos) | 20 |

### Ejemplos de personalización

**Círculo más grande:**
```python
radio = 100  # Radio de 100 píxeles
```

**Movimiento más lento:**
```python
time_step = 0.01  # Más tiempo entre movimientos
```

**Más tiempo entre ciclos:**
```python
interval = 60  # 1 minuto entre cada círculo
```

## Cómo funciona

1. Obtiene la posición actual del mouse usando `GetCursorPos`
2. Calcula puntos en un círculo usando funciones trigonométricas (`cos` y `sin`)
3. Mueve el mouse a cada punto usando `SetCursorPos`
4. Repite el proceso indefinidamente con el intervalo configurado

## Licencia

MIT