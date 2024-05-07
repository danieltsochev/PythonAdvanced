from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.tester = SocialMedia('jonny', 'YouTube', 2, 'travel')

    def test_correct__init__(self):
        self.assertEqual('jonny', self.tester._username)
        self.assertEqual('YouTube', self.tester._platform)
        self.assertEqual(2, self.tester.followers)
        self.assertEqual('travel', self.tester._content_type)
        self.assertEqual([], self.tester._posts)

    def test_followers_negative_value_error(self):
        expect = "Followers cannot be negative."
        with self.assertRaises(ValueError) as ve:
            self.tester.followers = -1
        self.assertEqual(expect, str(ve.exception))

    def test_setting_wrong_platform_value_error(self):
        expect = "Platform should be one of ['Instagram', 'YouTube', 'Twitter']"
        with self.assertRaises(ValueError) as ve:
            self.tester._validate_and_set_platform('Telegram')
        self.assertEqual(expect, str(ve.exception))

    def test_correct_function_validate_and_set_platform(self):
        expect = 'Instagram'
        self.tester._validate_and_set_platform('Instagram')
        self.assertEqual(expect, self.tester.platform)

    def test_create_pos_function_and_return(self):
        expect_post = [{'content': 'music', 'likes': 0, 'comments': []}]
        expect_return = "New travel post created by jonny on YouTube."
        self.assertEqual(expect_return, self.tester.create_post('music'))
        self.assertEqual(expect_post, self.tester._posts)

    def test_like_post_when_index_out_of_range(self):
        expect = "Invalid post index."
        self.tester.create_post('movie')
        self.assertEqual(expect, self.tester.like_post(-1))
        self.assertEqual(expect,  self.tester.like_post(1))
        self.assertEqual(expect, self.tester.like_post(2))

    def test_like_post_when_max_likes_reached(self):
        expect = "Post has reached the maximum number of likes."
        self.tester._posts = [{'content': 'travel', 'likes': 10, 'comments': []}]
        self.assertEqual(expect, self.tester.like_post(0))

    def test_like_post_check_functionality(self):
        expect_return = "Post liked by jonny."
        expect_likes_raise = [{'content': 'travel', 'likes': 8, 'comments': []}]
        self.tester._posts = [{'content': 'travel', 'likes': 7, 'comments': []}]
        self.assertEqual(expect_return, self.tester.like_post(0))
        self.assertEqual(expect_likes_raise, self.tester._posts)

    def test_comment_on_post_when_length_smaller_than_ten(self):
        expect = "Comment should be more than 10 characters."
        self.tester._posts = [{'content': 'travel', 'likes': 7, 'comments': []}]
        self.assertEqual(expect, self.tester.comment_on_post(0, 'no'))

    def test_comment_on_post_when_length_greater_than_ten(self):
        expect_return = "Comment added by jonny on the post."
        self.tester._posts = [{'content': 'travel', 'likes': 7, 'comments': []}]
        self.assertEqual(expect_return, self.tester.comment_on_post(0, 'this is so nice and fresh'))


if __name__ == '__main__':
    main()
