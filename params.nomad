# количество аргументов функционала
DIMENSION 24


# команда, запускающая блакбокс и
# вычисляющая значение функционала
BB_EXE "$python3 eval.py"


# формат ввода блакбокса:
# три вещественных числа и одно целое
BB_INPUT_TYPE ( R R R R R R R R R R R R R R R R R R R R R R R R)


# формат вывода блакбокса:
# только значение функционала (OBJ)
# может содержать также функции-условия
# (для задач условной оптимизации)
BB_OUTPUT_TYPE OBJ

# начальное приближение
X0 ( 0 0.49 0 1 0 0.7 0 1 0.7 -0.49 0 1 1.33 1.52 1.96 1 1 0 1 0 0 0 0 0)


# границы изменения параметров
LOWER_BOUND ( -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 -10 0 0 0 0 0 0 0 0 0 )
UPPER_BOUND ( 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 )

# максимальное количество запуска блакбокса
MAX_BB_EVAL 15000

# временная директория
TMP_DIR /tmp