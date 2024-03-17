from main import process_numbers

def test_process_numbers():
    assert process_numbers([1, 2, 5, 6, 8, -8, -10, 20]) == 504

