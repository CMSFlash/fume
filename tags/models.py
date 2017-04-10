from django.db import models
from member.models import Member
from games.models import Game

class TagManager(models.Manager):

    def get_tags_of_game(self, game, order='Arbitrary'):
        tag_items = TagItem.objects.filter(game=game)
        tags = set()
        for tag_item in tag_items:
            tags.add(tag_item.tag)
        tags = list(tags)
        if (order == 'Lexicographical'):
            tags.sort(key=lambda tag: tag.label)
        return tags

class Tag(models.Model):

    label = models.TextField(max_length=100)
    objects = TagManager()

    @classmethod
    def create(cls, label):
        return cls(label=label)

class TagItem(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_items')
    tagger = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='tag_items')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tag_items')

    @classmethod
    def create(cls, tag, tagger, game):
        return cls(tag=tag, tagger=tagger, game=game)