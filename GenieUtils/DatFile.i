%module DatFile

%include "stdint.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_pair.i"

%{
#include "var/genieutils/include/genie/dat/Graphic.h"
#include "var/genieutils/include/genie/dat/Unit.h"
#include "var/genieutils/include/genie/dat/DatFile.h"

using namespace genie;
%}


%include "var/genieutils/include/genie/file/ISerializable.h"
%include "var/genieutils/include/genie/dat/Graphic.h"

%include "var/genieutils/include/genie/dat/unit/AttackOrArmor.h"
%include "var/genieutils/include/genie/dat/unit/Bird.h"
%include "var/genieutils/include/genie/dat/unit/Building.h"
%include "var/genieutils/include/genie/dat/unit/Creatable.h"
%include "var/genieutils/include/genie/dat/unit/DamageGraphic.h"
%include "var/genieutils/include/genie/dat/unit/DeadFish.h"
%include "var/genieutils/include/genie/dat/unit/Projectile.h"
%include "var/genieutils/include/genie/dat/unit/Type50.h"

%include "var/genieutils/include/genie/dat/Unit.h"
%include "var/genieutils/include/genie/dat/Civ.h"


namespace std {
    %template(CivVector) vector<genie::Civ>;
    %template(UnitVector) vector<genie::Unit>;
    %template(GraphicVector) vector<genie::Graphic>;

    %template(Int16Pair) pair<int16_t, int16_t>;
}

%include "var/genieutils/include/genie/Types.h"
%include "var/genieutils/include/genie/file/IFile.h"
%include "var/genieutils/include/genie/dat/DatFile.h"
