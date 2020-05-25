from maps import maps


def test_get_location():
    assert maps.get_location('tour eiffel') == {'lat': 49.2712154,
                                                'lng': 2.4833139}