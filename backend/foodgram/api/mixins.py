from rest_framework import mixins, viewsets


class GetPostMixin(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """Mixin для наследования."""
    pass


class ListPostDel(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """Mixin для наследования."""
    pass


class ListPostDelPatch(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin):
    """Mixin для наследования."""
    pass
