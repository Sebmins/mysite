from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse
from quiz.forms import QuestionForm
from quiz.models import Quiz, QuizQuestion
from selenium import webdriver
from quiz.models import Quiz,QuizQuestion
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

# Test all static urls
class URLTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_create(self):
        response = self.client.get(reverse('quiz:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/create.html')

    def test_two_entries(self):
        Quiz.objects.create(title='1-title', author='1-author')
        Quiz.objects.create(title='2-title', author='2-author')
        response = self.client.get(reverse('quiz:index'))
        self.assertContains(response, '1-title')
        self.assertContains(response, '2-title')
        self.assertNotContains(response, '2-author')
        # self.assertContains(response, 'add')


# Test creating objects
class ModelTests(TestCase):
    @classmethod
    def setUp(self):
        self.quiz_instance = Quiz.objects.create(title='Test title', author='Test author')
        self.question_instance = QuizQuestion.objects.create(quiz=Quiz.objects.get(id=1),
                                                             question_text='test question',
                                                             correct=1,
                                                             option1='option 1',
                                                             option2='option 2',
                                                             option3='option 3',
                                                             option4='option 4', )

    def test_quiz_data(self):
        quiz = Quiz.objects.get(id=1)
        title_label = quiz.title
        self.assertEqual(title_label, 'Test title')

    def test_question_data(self):
        question = QuizQuestion.objects.get(id=1)
        self.assertEqual(question.question_text, 'test question')
        self.assertEqual(question.correct, 1)
        self.assertEqual(question.option1, 'option 1')

    # def test_quiz(self):
    #     request = self.client.post(
    #         reverse('quiz:questionnaire', kwargs={'quiz_id': self.question_instance.id}))
    #     response = self.client.get(reverse('quiz:questionnaire', args=(id)))
    #     self.assertEqual(request.status_code, 200)
    #     self.assertTemplateUsed(request, 'quiz/questionnaire.html')


# Test form validation
class FormTest(TestCase):
    def test_create_form(self):
        form = QuestionForm(data={'title': 'Science',
                                  'author': 'Seb Waring',
                                  'question_text': 'What is the fourth state of matter',
                                  'correct': 3,
                                  'option1': 'Gas',
                                  'option2': 'Liquid',
                                  'option3': 'Plasma',
                                  'option4': 'Solid', })
        self.assertTrue(form.is_valid())

    # Provide a string instead of an integer and should fail
    def test_create_falseform(self):
        form = QuestionForm(data={'title': 'Science',
                                  'author': 'Seb Waring',
                                  'question_text': 'What is the fourth state of matter',
                                  'correct': "5",
                                  'option1': 'Gas',
                                  'option2': 'Liquid',
                                  'option3': 'Plasma',
                                  'option4': 'Solid', })
        self.assertFalse(form.is_valid())


class FunctionalTests(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('quiz/chromedriver')

    def tearDown(self):
        self.browser.close()


    def test_index_page_displayed(self):
        self.browser.get(self.live_server_url)
        # time.sleep(20)

        alert = self.browser.find_elements_by_tag_name('li')
        self.assertEqual(alert[0].find_element_by_tag_name('a').text, 'quiz')
        self.assertEqual(alert[1].find_element_by_tag_name('a').text, 'polls')

    def test_create_display(self):
        self.browser.get(self.live_server_url)

        add_url = self.live_server_url + reverse('quiz:index')
        create_url = self.live_server_url + reverse('quiz:create')
        self.browser.find_element_by_tag_name('a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, add_url)
        self.browser.find_element_by_class_name('create_quiz').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, create_url)
        self.browser.find_element_by_id('id_title').send_keys("Test Quiz")
        self.browser.find_element_by_id('id_author').send_keys("Test Author")
        self.browser.find_element_by_id('id_quizquestion_set-0-question_text').send_keys("Test Question")
        self.browser.find_element_by_id('id_quizquestion_set-0-correct').send_keys("1")
        self.browser.find_element_by_id('id_quizquestion_set-0-option1').send_keys("Test Option1")
        self.browser.find_element_by_id('id_quizquestion_set-0-option2').send_keys("Test Option2")
        self.browser.find_element_by_id('id_quizquestion_set-0-option3').send_keys("Test Option3")
        self.browser.find_element_by_id('id_quizquestion_set-0-option4').send_keys("Test Option4")
        self.browser.find_element_by_id('submitBtn').click()
        self.assertEqual(self.browser.current_url, add_url)
        indexList = self.browser.find_elements_by_tag_name('a')
        self.assertEqual(indexList[0].text, 'Test Quiz')
        indexList[0].click()
        time.sleep(1)