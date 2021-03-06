import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import PollChoice
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def poll_choice_factory(db, poll_factory):
    class PollChoiceFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = PollChoice

        poll = factory.SubFactory(poll_factory)
        text = faker.sentence(nb_words=200)

    return PollChoiceFactory


@pytest.fixture
def sample_poll_choice(poll_choice_factory):
    '''
    sample usage:
    > poll_choice1 = sample_poll_choice()
    > poll_choice2 = sample_poll_choice()
    > PollChoice.objects.all().count() # returns 2
    '''
    def factory_worker(**custom_fields):
        defaults = {
            "text": factory.LazyAttribute(lambda x: faker.sentence(nb_words=200)),
        }
        defaults = extend(defaults, custom_fields)
        return poll_choice_factory(**defaults)

    return factory_worker

