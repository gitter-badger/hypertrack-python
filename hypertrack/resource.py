class HyperTrackObject(dict):

    def __init__(self, *args, **kwargs):
        super(HyperTrackObject, self).__init__(*args, **kwargs)


class APIResource(HyperTrackObject):
    pass


class CreatableResource(object):
    pass


class UpdatableResource(object):
    pass


class DeletableResource(object):
    pass


class ListableResouce(object):
    pass


class Customer(HyperTrackObject):
    pass


class Destination(HyperTrackObject):
    pass


class Fleet(HyperTrackObject):
    pass


class Driver(HyperTrackObject):
    pass


class Hub(HyperTrackObject):
    pass


class Task(HyperTrackObject):
    pass


class Trip(HyperTrackObject):
    pass


class GPSLog(HyperTrackObject):
    pass


class Event(HyperTrackObject):
    pass
