# Set up python environment for autotests
1. Make sure you have python installed on your machine by typing in console "python --version" 
   (python 3.12 was used for test development)
2. Activate VirtualEnv 
   >source venv/bin/activate
3. Install requirements.txt
   >pip install -r requirements.txt
4. Install PyTest as default runner(instruction for PyCharm IDE )
- PyCharm - Preferences - Tools - Python integrated tools - default test runner: pytest

# Run tests
- To run all tests execute next script:
  >pytest
- To run specific tests execute next script:
  >pytest tests/test_login.py::TestLogin::test_incorrect_creds