from compare_images import compare_images, image_search_in_image
import pytest

first_image = "img/image_2020_12_17T09_57_35_397Z.png"
second_image = "img/image_2020_12_17T09_59_40_825Z.png"
searched_image = "img/image_must_be_in_first_img.png"


class TestCompareImages:
    def test_equal_images(self):
        assert compare_images(first_image, first_image), "Images shoud be same"

    @pytest.mark.xfail(strict=True)
    def test_different_images(self):
        assert compare_images(first_image, second_image), "Images shoud not be same"


class TestImageInAnotherImage:
    def test_image_is_on_another_image(self):
        assert image_search_in_image(first_image, searched_image), "Searched image shoud be in base image"

    @pytest.mark.xfail(strict=True)
    def test_image_is_not_on_another_image(self):
        assert image_search_in_image(second_image, searched_image), "Searched image shoud not be in base image"