import subprocess

tests = [

"tests/test_homepage.py",

"tests/test_search.py"

]

for test in tests:

    subprocess.run(["python", test])