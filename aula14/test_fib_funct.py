from subprocess import PIPE

def test_no_args():
    proc = Popen("python3 fib_funct.py ",stdout=PIPE,shell=True)
    return_code = proc.wait()
    output = proc.stdout.read().decode('utf-8')
    assert output == "Usage: python3 fib_funct.py number\n"
    assert return_code == 1