from rest_framework import mixins, viewsets


class ListDeleteViewSet(mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    pass
