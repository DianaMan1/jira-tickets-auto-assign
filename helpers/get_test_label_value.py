def __get_test_label_value():
    with open('.config/.debug/test_label_value') as file:
        value = file.read()
        file.close()
        return value
    
TEST_LABEL_VALUE = __get_test_label_value()
