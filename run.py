import pytest

if __name__ == '__main__':
    pytest.main(['-s','-v','--alluredir','./target/allure-results','--clean-alluredir'])
