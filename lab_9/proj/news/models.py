from django.db import models


# Create your models here.

class Rubric(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    keywords = models.CharField(max_length=256)
    annotation = models.TextField()
    rubNum = models.ForeignKey(
        'Rubric',
        on_delete=models.CASCADE)

    def __str__(self):
        result = str(self.id) + " " + self.title
        return result

    # def import_from_csv(self):
    #     import pandas
    #     readerCSV = pandas.read_csv('text.csv', sep=';')
    #
    #     [Article.objects.create(title=titleText, keywords=readerCSV['keywords'][titleKey],
    #                         annotation=readerCSV['annotation'][titleKey],
    #                         rubNum=Rubric.objects.get(id=readerCSV['rubNum'][titleKey])) for titleKey, titleText in
    #     readerCSV['title'].items()]


class Hashtag(models.Model):
    name = models.CharField(max_length=256)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name
