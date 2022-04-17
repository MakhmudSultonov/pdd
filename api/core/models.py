from django.db import models
from django.utils.timezone import now

class Data(models.Model):
    pred = models.CharField(max_length=120)
    pred_idx = models.CharField(max_length=120)
    probs = models.CharField(max_length=120)
    picture = models.FileField()
    created_at = models.DateTimeField(default=now)

    def __str_(self):
        return "data for {}".format(self.pred_idx)
