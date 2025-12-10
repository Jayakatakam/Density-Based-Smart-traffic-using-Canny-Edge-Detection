def get_signal_time(density):
    if density > 9000:
        return 60
    elif density > 6000:
        return 45
    elif density > 3000:
        return 30
    else:
        return 15
