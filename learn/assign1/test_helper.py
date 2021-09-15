import assign1

def test_helper():
    assert "World!" == assign1.helper("World"), "did not get the expected excitement"

def test_helper_no_args():
    assert "!" == assign1.helper(), "you need to handle when no arguments are passed"
