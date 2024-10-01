import rt_with_exceptions
from tests_12_3 import RunnerTest
import runner
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                    encoding='utf-8', format="%(levelname)s ! %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            x = runner.Runner('Mark')
            logging.info(f'{test_walk} выполнен успешно')
            for i in range(10):
               x.walk()
            self.assertEqual(x.distance, 50, f'{x.name} должен пройти 50 метров, а прошел {x.distance}')
        except:
            logging.error(f'Неверная скорость для{Runner}')


    def test_run(self):
        y = runner.Runner('Ugor')
        for i in range(10):
            y.run()
        self.assertEqual(y.distance, 100, f'{y.name} должен пробежать 100 метров, а пробежал {y.distance}')


