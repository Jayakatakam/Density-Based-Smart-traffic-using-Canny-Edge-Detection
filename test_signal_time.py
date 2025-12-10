from signal_controller import get_signal_time

def test_signal():
    assert get_signal_time(10000) == 60
