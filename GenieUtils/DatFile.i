%module DatFile

%include "stdint.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_pair.i"

%{
#include "var/genieutils/include/genie/Types.h"
#include "var/genieutils/include/genie/dat/Graphic.h"
#include "var/genieutils/include/genie/dat/Unit.h"
#include "var/genieutils/include/genie/dat/DatFile.h"

using namespace genie;
%}

%include "var/genieutils/include/genie/Types.h";
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

%include "var/genieutils/include/genie/dat/ResourceUsage.h"
%include "var/genieutils/include/genie/dat/Unit.h"
%include "var/genieutils/include/genie/dat/Civ.h"
%include "var/genieutils/include/genie/dat/Research.h"
%include "var/genieutils/include/genie/dat/UnitLine.h"

%template(CivVector) std::vector<genie::Civ>;
%template(UnitVector) std::vector<genie::Unit>;
%template(GraphicVector) std::vector<genie::Graphic>;
%template(TechVector) std::vector<genie::Tech>;
%template(UnitLineVector) std::vector<genie::UnitLine>;
%template(ResearchResourceCost) genie::ResourceUsage<int16_t, int16_t, int8_t>;
%template(ResearchResourceCostVector) std::vector<genie::ResourceUsage<int16_t, int16_t, int8_t>>;

%template(Int16Pair) std::pair<int16_t, int16_t>;

%include "var/genieutils/include/genie/Types.h"
%include "var/genieutils/include/genie/file/IFile.h"
%include "var/genieutils/include/genie/dat/DatFile.h"
