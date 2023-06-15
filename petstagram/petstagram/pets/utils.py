from petstagram.pets.models import Pet


def get_by_petname_and_username(pet_slug, username):
    return Pet.objects.filter(slug=pet_slug, user__username=username).get()


def is_owner(request, obj):
    return request.user == obj.user


# class OwnedRequired:
#     def get(self, request, *args, **kwargs):
#         result = super().get(request, *args, **kwargs)
#         if request.user == self.object.user:
#             return result
#         else:
#             return ...