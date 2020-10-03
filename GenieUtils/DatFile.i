%module DatFile

%include "stdint.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_pair.i"

%{
#include "var/genieutils/include/genie/dat/Graphic.h"
#include "var/genieutils/include/genie/dat/Unit.h"
#include "var/genieutils/include/genie/dat/Civ.h"
#include "var/genieutils/include/genie/dat/DatFile.h"

using namespace genie;
%}


%include "var/genieutils/include/genie/file/ISerializable.h"
%include "var/genieutils/include/genie/dat/Graphic.h"
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
