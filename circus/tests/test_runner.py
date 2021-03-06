from circus.tests.support import TestCircus
import time


def Dummy(test_file):
    with open(test_file, 'w') as f:
        f.write('.')
        time.sleep(.1)
    return 1


class TestRunner(TestCircus):

    def test_dummy(self):
        test_file = self._run_circus('circus.tests.test_runner.Dummy')
        time.sleep(.5)

        # check that the file has been filled
        with open(test_file) as f:
            content = f.read()

        self.assertTrue('.' in content)
        self._stop_runners()
