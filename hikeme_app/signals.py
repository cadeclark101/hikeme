from django.dispatch import receiver
from hikeme_app.models import Person
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import pre_save

@receiver(pre_save, sender=Person)
def update_user(sender, instance: Person, **kwargs):
    if not instance.auth_user.id:
        # new user is created
        return

    # existing user is updated
    old_instance = sender.objects.get(id=instance.auth_user.id)
    if old_instance.current_trail != instance.current_trail:
        # execute this only if the user status has changed
        user_data = Person(instance).data
        channel_layer = get_channel_layer()
        user_group_name = "active_users"
        async_to_sync(channel_layer.group_send)(
            user_group_name, {"type": "send_user", "data": user_data}
        )