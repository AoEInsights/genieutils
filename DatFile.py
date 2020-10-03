# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _DatFile
else:
    import _DatFile

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _DatFile.delete_SwigPyIterator

    def value(self):
        return _DatFile.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _DatFile.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _DatFile.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _DatFile.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _DatFile.SwigPyIterator_equal(self, x)

    def copy(self):
        return _DatFile.SwigPyIterator_copy(self)

    def next(self):
        return _DatFile.SwigPyIterator_next(self)

    def __next__(self):
        return _DatFile.SwigPyIterator___next__(self)

    def previous(self):
        return _DatFile.SwigPyIterator_previous(self)

    def advance(self, n):
        return _DatFile.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _DatFile.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _DatFile.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _DatFile.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _DatFile.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _DatFile.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _DatFile.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _DatFile:
_DatFile.SwigPyIterator_swigregister(SwigPyIterator)

class ISerializable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _DatFile.delete_ISerializable

    def setInitialReadPosition(self, pos):
        return _DatFile.ISerializable_setInitialReadPosition(self, pos)

    def getInitialReadPosition(self):
        return _DatFile.ISerializable_getInitialReadPosition(self)

    def readObject(self, istr):
        return _DatFile.ISerializable_readObject(self, istr)

    def writeObject(self, ostr):
        return _DatFile.ISerializable_writeObject(self, ostr)

    def objectSize(self):
        return _DatFile.ISerializable_objectSize(self)

    def serializeSubObject(self, root):
        return _DatFile.ISerializable_serializeSubObject(self, root)

    def setGameVersion(self, gv):
        return _DatFile.ISerializable_setGameVersion(self, gv)

    def getGameVersion(self):
        return _DatFile.ISerializable_getGameVersion(self)
    dat_internal_ver = property(_DatFile.ISerializable_dat_internal_ver_get, _DatFile.ISerializable_dat_internal_ver_set)
    scn_ver = property(_DatFile.ISerializable_scn_ver_get, _DatFile.ISerializable_scn_ver_set)
    scn_plr_data_ver = property(_DatFile.ISerializable_scn_plr_data_ver_get, _DatFile.ISerializable_scn_plr_data_ver_set)
    scn_internal_ver = property(_DatFile.ISerializable_scn_internal_ver_get, _DatFile.ISerializable_scn_internal_ver_set)
    scn_trigger_ver = property(_DatFile.ISerializable_scn_trigger_ver_get, _DatFile.ISerializable_scn_trigger_ver_set)

# Register ISerializable in _DatFile:
_DatFile.ISerializable_swigregister(ISerializable)
cvar = _DatFile.cvar

UT_EyeCandy = _DatFile.UT_EyeCandy
UT_Trees = _DatFile.UT_Trees
UT_Flag = _DatFile.UT_Flag
UT_25 = _DatFile.UT_25
UT_Dead_Fish = _DatFile.UT_Dead_Fish
UT_Bird = _DatFile.UT_Bird
UT_Combatant = _DatFile.UT_Combatant
UT_Projectile = _DatFile.UT_Projectile
UT_Creatable = _DatFile.UT_Creatable
UT_Building = _DatFile.UT_Building
UT_AoeTrees = _DatFile.UT_AoeTrees
class Unit(ISerializable):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _DatFile.Unit_swiginit(self, _DatFile.new_Unit())
    __swig_destroy__ = _DatFile.delete_Unit

    def setGameVersion(self, gv):
        return _DatFile.Unit_setGameVersion(self, gv)
    Type = property(_DatFile.Unit_Type_get, _DatFile.Unit_Type_set)
    ID = property(_DatFile.Unit_ID_get, _DatFile.Unit_ID_set)
    LanguageDLLName = property(_DatFile.Unit_LanguageDLLName_get, _DatFile.Unit_LanguageDLLName_set)
    LanguageDLLCreation = property(_DatFile.Unit_LanguageDLLCreation_get, _DatFile.Unit_LanguageDLLCreation_set)
    Class = property(_DatFile.Unit_Class_get, _DatFile.Unit_Class_set)
    StandingGraphic = property(_DatFile.Unit_StandingGraphic_get, _DatFile.Unit_StandingGraphic_set)
    DyingGraphic = property(_DatFile.Unit_DyingGraphic_get, _DatFile.Unit_DyingGraphic_set)
    UndeadGraphic = property(_DatFile.Unit_UndeadGraphic_get, _DatFile.Unit_UndeadGraphic_set)
    UndeadMode = property(_DatFile.Unit_UndeadMode_get, _DatFile.Unit_UndeadMode_set)
    HitPoints = property(_DatFile.Unit_HitPoints_get, _DatFile.Unit_HitPoints_set)
    LineOfSight = property(_DatFile.Unit_LineOfSight_get, _DatFile.Unit_LineOfSight_set)
    GarrisonCapacity = property(_DatFile.Unit_GarrisonCapacity_get, _DatFile.Unit_GarrisonCapacity_set)
    CollisionSize = property(_DatFile.Unit_CollisionSize_get, _DatFile.Unit_CollisionSize_set)
    TrainSound = property(_DatFile.Unit_TrainSound_get, _DatFile.Unit_TrainSound_set)
    DamageSound = property(_DatFile.Unit_DamageSound_get, _DatFile.Unit_DamageSound_set)
    WwiseTrainSoundID = property(_DatFile.Unit_WwiseTrainSoundID_get, _DatFile.Unit_WwiseTrainSoundID_set)
    WwiseDamageSoundID = property(_DatFile.Unit_WwiseDamageSoundID_get, _DatFile.Unit_WwiseDamageSoundID_set)
    DeadUnitID = property(_DatFile.Unit_DeadUnitID_get, _DatFile.Unit_DeadUnitID_set)
    BloodUnitID = property(_DatFile.Unit_BloodUnitID_get, _DatFile.Unit_BloodUnitID_set)
    SortNumber = property(_DatFile.Unit_SortNumber_get, _DatFile.Unit_SortNumber_set)
    CanBeBuiltOn = property(_DatFile.Unit_CanBeBuiltOn_get, _DatFile.Unit_CanBeBuiltOn_set)
    IconID = property(_DatFile.Unit_IconID_get, _DatFile.Unit_IconID_set)
    HideInEditor = property(_DatFile.Unit_HideInEditor_get, _DatFile.Unit_HideInEditor_set)
    OldPortraitPict = property(_DatFile.Unit_OldPortraitPict_get, _DatFile.Unit_OldPortraitPict_set)
    Enabled = property(_DatFile.Unit_Enabled_get, _DatFile.Unit_Enabled_set)
    Disabled = property(_DatFile.Unit_Disabled_get, _DatFile.Unit_Disabled_set)
    PlacementSideTerrain = property(_DatFile.Unit_PlacementSideTerrain_get, _DatFile.Unit_PlacementSideTerrain_set)
    PlacementTerrain = property(_DatFile.Unit_PlacementTerrain_get, _DatFile.Unit_PlacementTerrain_set)
    ClearanceSize = property(_DatFile.Unit_ClearanceSize_get, _DatFile.Unit_ClearanceSize_set)
    HillMode = property(_DatFile.Unit_HillMode_get, _DatFile.Unit_HillMode_set)
    FogVisibility = property(_DatFile.Unit_FogVisibility_get, _DatFile.Unit_FogVisibility_set)
    TerrainRestriction = property(_DatFile.Unit_TerrainRestriction_get, _DatFile.Unit_TerrainRestriction_set)
    FlyMode = property(_DatFile.Unit_FlyMode_get, _DatFile.Unit_FlyMode_set)
    ResourceCapacity = property(_DatFile.Unit_ResourceCapacity_get, _DatFile.Unit_ResourceCapacity_set)
    ResourceDecay = property(_DatFile.Unit_ResourceDecay_get, _DatFile.Unit_ResourceDecay_set)
    BlastDefenseLevel = property(_DatFile.Unit_BlastDefenseLevel_get, _DatFile.Unit_BlastDefenseLevel_set)
    CombatLevel = property(_DatFile.Unit_CombatLevel_get, _DatFile.Unit_CombatLevel_set)
    InteractionMode = property(_DatFile.Unit_InteractionMode_get, _DatFile.Unit_InteractionMode_set)
    MinimapMode = property(_DatFile.Unit_MinimapMode_get, _DatFile.Unit_MinimapMode_set)
    InterfaceKind = property(_DatFile.Unit_InterfaceKind_get, _DatFile.Unit_InterfaceKind_set)
    MultipleAttributeMode = property(_DatFile.Unit_MultipleAttributeMode_get, _DatFile.Unit_MultipleAttributeMode_set)
    MinimapColor = property(_DatFile.Unit_MinimapColor_get, _DatFile.Unit_MinimapColor_set)
    LanguageDLLHelp = property(_DatFile.Unit_LanguageDLLHelp_get, _DatFile.Unit_LanguageDLLHelp_set)
    LanguageDLLHotKeyText = property(_DatFile.Unit_LanguageDLLHotKeyText_get, _DatFile.Unit_LanguageDLLHotKeyText_set)
    HotKey = property(_DatFile.Unit_HotKey_get, _DatFile.Unit_HotKey_set)
    Recyclable = property(_DatFile.Unit_Recyclable_get, _DatFile.Unit_Recyclable_set)
    EnableAutoGather = property(_DatFile.Unit_EnableAutoGather_get, _DatFile.Unit_EnableAutoGather_set)
    CreateDoppelgangerOnDeath = property(_DatFile.Unit_CreateDoppelgangerOnDeath_get, _DatFile.Unit_CreateDoppelgangerOnDeath_set)
    ResourceGatherGroup = property(_DatFile.Unit_ResourceGatherGroup_get, _DatFile.Unit_ResourceGatherGroup_set)
    OcclusionMode = property(_DatFile.Unit_OcclusionMode_get, _DatFile.Unit_OcclusionMode_set)
    ObstructionType = property(_DatFile.Unit_ObstructionType_get, _DatFile.Unit_ObstructionType_set)
    ObstructionClass = property(_DatFile.Unit_ObstructionClass_get, _DatFile.Unit_ObstructionClass_set)
    Trait = property(_DatFile.Unit_Trait_get, _DatFile.Unit_Trait_set)
    Civilization = property(_DatFile.Unit_Civilization_get, _DatFile.Unit_Civilization_set)
    Nothing = property(_DatFile.Unit_Nothing_get, _DatFile.Unit_Nothing_set)
    SelectionEffect = property(_DatFile.Unit_SelectionEffect_get, _DatFile.Unit_SelectionEffect_set)
    EditorSelectionColour = property(_DatFile.Unit_EditorSelectionColour_get, _DatFile.Unit_EditorSelectionColour_set)
    OutlineSize = property(_DatFile.Unit_OutlineSize_get, _DatFile.Unit_OutlineSize_set)
    ResourceStorages = property(_DatFile.Unit_ResourceStorages_get, _DatFile.Unit_ResourceStorages_set)
    DamageGraphics = property(_DatFile.Unit_DamageGraphics_get, _DatFile.Unit_DamageGraphics_set)
    SelectionSound = property(_DatFile.Unit_SelectionSound_get, _DatFile.Unit_SelectionSound_set)
    DyingSound = property(_DatFile.Unit_DyingSound_get, _DatFile.Unit_DyingSound_set)
    WwiseSelectionSoundID = property(_DatFile.Unit_WwiseSelectionSoundID_get, _DatFile.Unit_WwiseSelectionSoundID_set)
    WwiseDyingSoundID = property(_DatFile.Unit_WwiseDyingSoundID_get, _DatFile.Unit_WwiseDyingSoundID_set)
    OldAttackReaction = property(_DatFile.Unit_OldAttackReaction_get, _DatFile.Unit_OldAttackReaction_set)
    ConvertTerrain = property(_DatFile.Unit_ConvertTerrain_get, _DatFile.Unit_ConvertTerrain_set)
    Name = property(_DatFile.Unit_Name_get, _DatFile.Unit_Name_set)
    Name2 = property(_DatFile.Unit_Name2_get, _DatFile.Unit_Name2_set)
    Unitline = property(_DatFile.Unit_Unitline_get, _DatFile.Unit_Unitline_set)
    MinTechLevel = property(_DatFile.Unit_MinTechLevel_get, _DatFile.Unit_MinTechLevel_set)
    CopyID = property(_DatFile.Unit_CopyID_get, _DatFile.Unit_CopyID_set)
    BaseID = property(_DatFile.Unit_BaseID_get, _DatFile.Unit_BaseID_set)
    TelemetryID = property(_DatFile.Unit_TelemetryID_get, _DatFile.Unit_TelemetryID_set)
    Speed = property(_DatFile.Unit_Speed_get, _DatFile.Unit_Speed_set)
    DeadFish = property(_DatFile.Unit_DeadFish_get, _DatFile.Unit_DeadFish_set)
    Bird = property(_DatFile.Unit_Bird_get, _DatFile.Unit_Bird_set)
    Type50 = property(_DatFile.Unit_Type50_get, _DatFile.Unit_Type50_set)
    Projectile = property(_DatFile.Unit_Projectile_get, _DatFile.Unit_Projectile_set)
    Creatable = property(_DatFile.Unit_Creatable_get, _DatFile.Unit_Creatable_set)
    Building = property(_DatFile.Unit_Building_get, _DatFile.Unit_Building_set)

# Register Unit in _DatFile:
_DatFile.Unit_swigregister(Unit)

class Civ(ISerializable):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _DatFile.Civ_swiginit(self, _DatFile.new_Civ())
    __swig_destroy__ = _DatFile.delete_Civ

    def setGameVersion(self, gv):
        return _DatFile.Civ_setGameVersion(self, gv)
    PlayerType = property(_DatFile.Civ_PlayerType_get, _DatFile.Civ_PlayerType_set)

    @staticmethod
    def getNameSize():
        return _DatFile.Civ_getNameSize()
    Name = property(_DatFile.Civ_Name_get, _DatFile.Civ_Name_set)
    Name2 = property(_DatFile.Civ_Name2_get, _DatFile.Civ_Name2_set)
    TechTreeID = property(_DatFile.Civ_TechTreeID_get, _DatFile.Civ_TechTreeID_set)
    TeamBonusID = property(_DatFile.Civ_TeamBonusID_get, _DatFile.Civ_TeamBonusID_set)
    Resources = property(_DatFile.Civ_Resources_get, _DatFile.Civ_Resources_set)
    IconSet = property(_DatFile.Civ_IconSet_get, _DatFile.Civ_IconSet_set)
    UnitPointers = property(_DatFile.Civ_UnitPointers_get, _DatFile.Civ_UnitPointers_set)
    Units = property(_DatFile.Civ_Units_get, _DatFile.Civ_Units_set)
    UniqueUnitsTechs = property(_DatFile.Civ_UniqueUnitsTechs_get, _DatFile.Civ_UniqueUnitsTechs_set)

# Register Civ in _DatFile:
_DatFile.Civ_swigregister(Civ)

def Civ_getNameSize():
    return _DatFile.Civ_getNameSize()

class CivVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DatFile.CivVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DatFile.CivVector___nonzero__(self)

    def __bool__(self):
        return _DatFile.CivVector___bool__(self)

    def __len__(self):
        return _DatFile.CivVector___len__(self)

    def __getslice__(self, i, j):
        return _DatFile.CivVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DatFile.CivVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DatFile.CivVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DatFile.CivVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DatFile.CivVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DatFile.CivVector___setitem__(self, *args)

    def pop(self):
        return _DatFile.CivVector_pop(self)

    def append(self, x):
        return _DatFile.CivVector_append(self, x)

    def empty(self):
        return _DatFile.CivVector_empty(self)

    def size(self):
        return _DatFile.CivVector_size(self)

    def swap(self, v):
        return _DatFile.CivVector_swap(self, v)

    def begin(self):
        return _DatFile.CivVector_begin(self)

    def end(self):
        return _DatFile.CivVector_end(self)

    def rbegin(self):
        return _DatFile.CivVector_rbegin(self)

    def rend(self):
        return _DatFile.CivVector_rend(self)

    def clear(self):
        return _DatFile.CivVector_clear(self)

    def get_allocator(self):
        return _DatFile.CivVector_get_allocator(self)

    def pop_back(self):
        return _DatFile.CivVector_pop_back(self)

    def erase(self, *args):
        return _DatFile.CivVector_erase(self, *args)

    def __init__(self, *args):
        _DatFile.CivVector_swiginit(self, _DatFile.new_CivVector(*args))

    def push_back(self, x):
        return _DatFile.CivVector_push_back(self, x)

    def front(self):
        return _DatFile.CivVector_front(self)

    def back(self):
        return _DatFile.CivVector_back(self)

    def assign(self, n, x):
        return _DatFile.CivVector_assign(self, n, x)

    def resize(self, *args):
        return _DatFile.CivVector_resize(self, *args)

    def insert(self, *args):
        return _DatFile.CivVector_insert(self, *args)

    def reserve(self, n):
        return _DatFile.CivVector_reserve(self, n)

    def capacity(self):
        return _DatFile.CivVector_capacity(self)
    __swig_destroy__ = _DatFile.delete_CivVector

# Register CivVector in _DatFile:
_DatFile.CivVector_swigregister(CivVector)

class UnitVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DatFile.UnitVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DatFile.UnitVector___nonzero__(self)

    def __bool__(self):
        return _DatFile.UnitVector___bool__(self)

    def __len__(self):
        return _DatFile.UnitVector___len__(self)

    def __getslice__(self, i, j):
        return _DatFile.UnitVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DatFile.UnitVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DatFile.UnitVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DatFile.UnitVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DatFile.UnitVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DatFile.UnitVector___setitem__(self, *args)

    def pop(self):
        return _DatFile.UnitVector_pop(self)

    def append(self, x):
        return _DatFile.UnitVector_append(self, x)

    def empty(self):
        return _DatFile.UnitVector_empty(self)

    def size(self):
        return _DatFile.UnitVector_size(self)

    def swap(self, v):
        return _DatFile.UnitVector_swap(self, v)

    def begin(self):
        return _DatFile.UnitVector_begin(self)

    def end(self):
        return _DatFile.UnitVector_end(self)

    def rbegin(self):
        return _DatFile.UnitVector_rbegin(self)

    def rend(self):
        return _DatFile.UnitVector_rend(self)

    def clear(self):
        return _DatFile.UnitVector_clear(self)

    def get_allocator(self):
        return _DatFile.UnitVector_get_allocator(self)

    def pop_back(self):
        return _DatFile.UnitVector_pop_back(self)

    def erase(self, *args):
        return _DatFile.UnitVector_erase(self, *args)

    def __init__(self, *args):
        _DatFile.UnitVector_swiginit(self, _DatFile.new_UnitVector(*args))

    def push_back(self, x):
        return _DatFile.UnitVector_push_back(self, x)

    def front(self):
        return _DatFile.UnitVector_front(self)

    def back(self):
        return _DatFile.UnitVector_back(self)

    def assign(self, n, x):
        return _DatFile.UnitVector_assign(self, n, x)

    def resize(self, *args):
        return _DatFile.UnitVector_resize(self, *args)

    def insert(self, *args):
        return _DatFile.UnitVector_insert(self, *args)

    def reserve(self, n):
        return _DatFile.UnitVector_reserve(self, n)

    def capacity(self):
        return _DatFile.UnitVector_capacity(self)
    __swig_destroy__ = _DatFile.delete_UnitVector

# Register UnitVector in _DatFile:
_DatFile.UnitVector_swigregister(UnitVector)

GV_None = _DatFile.GV_None
GV_TEST = _DatFile.GV_TEST
GV_MIK = _DatFile.GV_MIK
GV_DAVE = _DatFile.GV_DAVE
GV_MATT = _DatFile.GV_MATT
GV_AoEB = _DatFile.GV_AoEB
GV_AoE = _DatFile.GV_AoE
GV_RoR = _DatFile.GV_RoR
GV_Tapsa = _DatFile.GV_Tapsa
GV_T2 = _DatFile.GV_T2
GV_T3 = _DatFile.GV_T3
GV_T4 = _DatFile.GV_T4
GV_T5 = _DatFile.GV_T5
GV_T6 = _DatFile.GV_T6
GV_T7 = _DatFile.GV_T7
GV_T8 = _DatFile.GV_T8
GV_AoKE3 = _DatFile.GV_AoKE3
GV_AoKA = _DatFile.GV_AoKA
GV_AoKB = _DatFile.GV_AoKB
GV_AoK = _DatFile.GV_AoK
GV_TC = _DatFile.GV_TC
GV_Cysion = _DatFile.GV_Cysion
GV_C2 = _DatFile.GV_C2
GV_C3 = _DatFile.GV_C3
GV_C4 = _DatFile.GV_C4
GV_CK = _DatFile.GV_CK
GV_C5 = _DatFile.GV_C5
GV_C6 = _DatFile.GV_C6
GV_C7 = _DatFile.GV_C7
GV_C8 = _DatFile.GV_C8
GV_C9 = _DatFile.GV_C9
GV_C10 = _DatFile.GV_C10
GV_C11 = _DatFile.GV_C11
GV_C12 = _DatFile.GV_C12
GV_C13 = _DatFile.GV_C13
GV_C14 = _DatFile.GV_C14
GV_C15 = _DatFile.GV_C15
GV_SWGB = _DatFile.GV_SWGB
GV_CC = _DatFile.GV_CC
class XYZF(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_DatFile.XYZF_x_get, _DatFile.XYZF_x_set)
    y = property(_DatFile.XYZF_y_get, _DatFile.XYZF_y_set)
    z = property(_DatFile.XYZF_z_get, _DatFile.XYZF_z_set)

    def __init__(self):
        _DatFile.XYZF_swiginit(self, _DatFile.new_XYZF())
    __swig_destroy__ = _DatFile.delete_XYZF

# Register XYZF in _DatFile:
_DatFile.XYZF_swigregister(XYZF)

class IFile(ISerializable):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _DatFile.delete_IFile

    def freelock(self):
        return _DatFile.IFile_freelock(self)

    def setFileName(self, fileName):
        return _DatFile.IFile_setFileName(self, fileName)

    def getFileName(self):
        return _DatFile.IFile_getFileName(self)

    def load(self, *args):
        return _DatFile.IFile_load(self, *args)

    def save(self):
        return _DatFile.IFile_save(self)

    def saveAs(self, fileName):
        return _DatFile.IFile_saveAs(self, fileName)

# Register IFile in _DatFile:
_DatFile.IFile_swigregister(IFile)

class DatFile(IFile):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _DatFile.DatFile_swiginit(self, _DatFile.new_DatFile())
    __swig_destroy__ = _DatFile.delete_DatFile

    def setGameVersion(self, gv):
        return _DatFile.DatFile_setGameVersion(self, gv)

    def extractRaw(self, inFile, outFile):
        return _DatFile.DatFile_extractRaw(self, inFile, outFile)

    def setVerboseMode(self, verbose):
        return _DatFile.DatFile_setVerboseMode(self, verbose)
    FILE_VERSION_SIZE = _DatFile.DatFile_FILE_VERSION_SIZE
    FileVersion = property(_DatFile.DatFile_FileVersion_get, _DatFile.DatFile_FileVersion_set)
    FloatPtrTerrainTables = property(_DatFile.DatFile_FloatPtrTerrainTables_get, _DatFile.DatFile_FloatPtrTerrainTables_set)
    TerrainPassGraphicPointers = property(_DatFile.DatFile_TerrainPassGraphicPointers_get, _DatFile.DatFile_TerrainPassGraphicPointers_set)
    TerrainRestrictions = property(_DatFile.DatFile_TerrainRestrictions_get, _DatFile.DatFile_TerrainRestrictions_set)
    PlayerColours = property(_DatFile.DatFile_PlayerColours_get, _DatFile.DatFile_PlayerColours_set)
    Sounds = property(_DatFile.DatFile_Sounds_get, _DatFile.DatFile_Sounds_set)
    GraphicPointers = property(_DatFile.DatFile_GraphicPointers_get, _DatFile.DatFile_GraphicPointers_set)
    Graphics = property(_DatFile.DatFile_Graphics_get, _DatFile.DatFile_Graphics_set)
    TerrainBlock = property(_DatFile.DatFile_TerrainBlock_get, _DatFile.DatFile_TerrainBlock_set)
    RandomMaps = property(_DatFile.DatFile_RandomMaps_get, _DatFile.DatFile_RandomMaps_set)
    Effects = property(_DatFile.DatFile_Effects_get, _DatFile.DatFile_Effects_set)
    UnitHeaders = property(_DatFile.DatFile_UnitHeaders_get, _DatFile.DatFile_UnitHeaders_set)
    Civs = property(_DatFile.DatFile_Civs_get, _DatFile.DatFile_Civs_set)
    Techs = property(_DatFile.DatFile_Techs_get, _DatFile.DatFile_Techs_set)
    UnitLines = property(_DatFile.DatFile_UnitLines_get, _DatFile.DatFile_UnitLines_set)
    TechTree = property(_DatFile.DatFile_TechTree_get, _DatFile.DatFile_TechTree_set)
    TimeSlice = property(_DatFile.DatFile_TimeSlice_get, _DatFile.DatFile_TimeSlice_set)
    UnitKillRate = property(_DatFile.DatFile_UnitKillRate_get, _DatFile.DatFile_UnitKillRate_set)
    UnitKillTotal = property(_DatFile.DatFile_UnitKillTotal_get, _DatFile.DatFile_UnitKillTotal_set)
    UnitHitPointRate = property(_DatFile.DatFile_UnitHitPointRate_get, _DatFile.DatFile_UnitHitPointRate_set)
    UnitHitPointTotal = property(_DatFile.DatFile_UnitHitPointTotal_get, _DatFile.DatFile_UnitHitPointTotal_set)
    RazingKillRate = property(_DatFile.DatFile_RazingKillRate_get, _DatFile.DatFile_RazingKillRate_set)
    RazingKillTotal = property(_DatFile.DatFile_RazingKillTotal_get, _DatFile.DatFile_RazingKillTotal_set)
    TerrainsUsed1 = property(_DatFile.DatFile_TerrainsUsed1_get, _DatFile.DatFile_TerrainsUsed1_set)
    SUnknown2 = property(_DatFile.DatFile_SUnknown2_get, _DatFile.DatFile_SUnknown2_set)
    SUnknown3 = property(_DatFile.DatFile_SUnknown3_get, _DatFile.DatFile_SUnknown3_set)
    SUnknown4 = property(_DatFile.DatFile_SUnknown4_get, _DatFile.DatFile_SUnknown4_set)
    SUnknown5 = property(_DatFile.DatFile_SUnknown5_get, _DatFile.DatFile_SUnknown5_set)
    SUnknown7 = property(_DatFile.DatFile_SUnknown7_get, _DatFile.DatFile_SUnknown7_set)
    SUnknown8 = property(_DatFile.DatFile_SUnknown8_get, _DatFile.DatFile_SUnknown8_set)

# Register DatFile in _DatFile:
_DatFile.DatFile_swigregister(DatFile)



