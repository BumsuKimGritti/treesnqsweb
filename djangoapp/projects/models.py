from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class NewProject(models.Model):
    title = models.CharField(max_length=64)
    newproject_text = models.CharField(max_length=512)
    newproject_detail = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    # TODO: Depending on user profile, "Default", "Member", "NonProfit"
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse_lazy('add-to-cart', args=[self.id])

    def get_remove_from_cart_url(self):
        return reverse_lazy('remove-from-cart', args=[self.id])
