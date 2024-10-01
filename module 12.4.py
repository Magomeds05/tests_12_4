from with_exception import Runner, Tournament
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests2.log',
                    encoding='utf-8', format="%(levelname)s ! %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            x = Runner('Mark', -5)
            for i in range(10):
               x.walk()
            self.assertEqual(x.distance, 50, f'{x.name} должен пройти 50 метров, а прошел {x.distance}')
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.error(f'Неверная скорость для{Runner}', exc_info=exc)


    def test_run(self):
        try:
            y = Runner(40)
            for i in range(10):
               y.run()
            self.assertEqual(y.distance, 100, f'{y.name} должен пробежать 100 метров, а пробежал {y.distance}')
            logging.info(f'"test_run" выполнен успешно')
        except TypeError as exc:
            logging.error(f'Неверный тип данных для объекта {Runner}', exc_info=exc)


