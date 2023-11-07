from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment


class CommentTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Create a post
        self.post = Post.objects.create(
            title='Test Post', content='Test Content', owner=self.user)
        # Create a comment for the post
        self.comment = Comment.objects.create(
            content='A test comment', owner=self.user, post=self.post)

    def test_get_comments(self):
        # Ensure we can retrieve a list of comments for a post
        url = reverse('comment-list')
        response = self.client.get(url, {'post': self.post.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make sure the response is paginated and the 'results' key contains a list
        self.assertIn('results', response.data,
                  "Response data should include a 'results' key for paginated lists.")
        self.assertIsInstance(
           response.data['results'], list, "'results' should be a list.")

       # Check if the returned comments in 'results' are only for the specified post
        comments_for_post = [
          comment for comment in response.data['results'] if comment['post'] == self.post.pk]
        self.assertEqual(len(comments_for_post), 1,
                     "There should be only one comment for the specified post.")

    def test_create_comment(self):
        # Ensure we can create a new comment for a post
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment-list')
        data = {'content': 'Creating a new comment', 'post': self.post.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comment_detail(self):
        # Ensure we can retrieve a comment's detail
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        # Ensure we can update a comment
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        data = {'content': 'Updated comment', 'post': self.post.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        # Ensure we can delete a comment
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
