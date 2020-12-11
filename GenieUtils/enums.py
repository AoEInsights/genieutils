import enum


class UnknownValueMixin(enum.Enum):
    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


class DefaultIntValueMixin():
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, int):
            return cls._create_pseudo_member_(value)
        return None  # will raise the ValueError in Enum.__new__

    @classmethod
    def _create_pseudo_member_(cls, value):
        pseudo_member = cls._value2member_map_.get(value, None)
        if pseudo_member is None:
            new_member = int.__new__(cls, value)
            # I expect a name attribute to hold a string, hence str(value)
            # However, new_member._name_ = value works, too
            new_member._name_ = str(value)
            new_member._value_ = value
            pseudo_member = cls._value2member_map_.setdefault(value, new_member)
        return pseudo_member


class UnitType(UnknownValueMixin, enum.IntEnum):
    EYE_CANDY = 10
    TREE_AOK = 15
    ANIMATED = 20
    DOPPELGANGER = 25
    MOVING = 30
    ACTOR = 40
    SUPERCLASS = 50
    PROJECTILE = 60
    COMBATANT = 70
    BUILDING = 80
    TREE_AOE = 90

    UNKNOWN = -1


class ResourceType(DefaultIntValueMixin, enum.IntEnum):
    FOOD = 0
    WOOD = 1
    STONE = 2
    GOLD = 3
