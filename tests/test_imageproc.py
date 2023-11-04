import tempfile

from imageproc import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_generate_images():
    from imageproc.measure import generate_images

    images = list(generate_images(10, 256, 256, 3))
    assert len(list(images)) == 10


def test_save_images():
    from imageproc.measure import generate_images, save_images
    from pathlib import Path

    # make temporary directory
    with tempfile.TemporaryDirectory() as tmp_dirname:
        images = list(generate_images(10, 256, 256, 3))
        tmp_path = Path(tmp_dirname)
        save_images(images, tmp_path)
        assert tmp_path.exists()
        assert len(list(tmp_path.iterdir())) == 10
        assert len(list(tmp_path.glob("*.png"))) == 10
        assert len(list(tmp_path.glob("*.jpg"))) == 0
        save_images(images, tmp_path, extension="jpg")
        assert len(list(tmp_path.glob("*.jpg"))) == 10
