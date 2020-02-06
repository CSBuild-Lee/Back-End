# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# import uuid

# # Create your models here.
# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default=0)
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     def initialize(self):
#         if self.currentRoom == 0:
#             self.currentRoom = Room.objects.first().id
#             self.save()
#     def room(self):
#         try:
#             return Room.objects.get(id=self.currentRoom)
#         except Room.DoesNotExist:
#             self.initialize()
#             return self.room()

# @receiver(post_save, sender=User)
# def create_user_player(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user=instance)
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_player(sender, instance, **kwargs):
#     instance.player.save()