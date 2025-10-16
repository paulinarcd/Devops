from main import
from unittest.mock import patch

@patch("maim.request.get")
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"temperature": 22}

    result = get_weather()
    assert result == 22