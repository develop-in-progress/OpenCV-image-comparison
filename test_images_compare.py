from compare_images import compare_images


first_image = "img/image_2020_12_17T09_57_35_397Z.png"
second_image = "img/image_2020_12_17T09_59_40_825Z.png"


class TestCompareImages:
    def test_equal_images(self):
        assert compare_images(first_image, first_image)

    def test_different_images(self):
        assert compare_images(first_image, second_image)