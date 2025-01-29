import subprocess

def run_test(command, expected_output):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    assert output == expected_output, f"Expected: {expected_output}, Got: {output}"

def test_addition():
    run_test("./your_program.sh add 2 3", "5")

def test_subtraction():
    run_test("./your_program.sh subtract 5 2", "3")

def test_multiplication():
    run_test("./your_program.sh multiply 4 3", "12")

def test_division():
    run_test("./your_program.sh divide 6 3", "2.0")

def test_division_by_zero():
    run_test("./your_program.sh divide 6 0", "Erreur : Division par zéro.")
