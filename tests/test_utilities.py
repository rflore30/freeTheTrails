import freethetrails.utilities as utl


def test_trail_init():
    """Test to see that Trail is initialized properly"""
    attributes = (
        ('Trail1', 5.1, 4.3),
        ('Trail2', 6.7, 3.1)
    )

    for attribute in attributes:
        actual = utl.Trail(*attribute)
        assert actual.name == attribute[0]
        assert actual.length == attribute[1]
        assert actual.rating == attribute[2]


def test_trail_str():
    """Test to see that str(Trail) has all needed info"""
    length = 5
    rating = 2
    name = 'my_trail'
    my_trail = utl.Trail(length, rating, name)

    assert str(length) in str(my_trail)
    assert str(rating) in str(my_trail)
    assert name in str(my_trail)
