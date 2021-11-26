#!/bin/bash
 
function replace_company()
{
    # $1 original name
    # $2 new name
    # $3 original compay name
    # $4 new company name
 
    cat $1 | sed -e "s/$3/$4/g" > $2
}
 
if [ $# -ne 3 ]; then
    echo "Usage: $0 <version> <project_name> <company_name>" > /dev/stderr
    exit 1
fi

if [ -d "../hardware/$VERSION" ]; then
	echo "+++ Version exists, please enter unique version!"
	exit 1
fi
 
ORIG_COMPANY="Josh Johnson"
 
VERSION=$1
NAME=$2
COMPANY=$3
 
mkdir ../hardware
cp -R template ../hardware/$VERSION
for suffix in -cache.lib .pro; do
    mv ../hardware/$VERSION/template${suffix} ../hardware/$VERSION/${NAME}${suffix}
done
 
replace_company ../hardware/$VERSION/template.kicad_pcb ../hardware/$VERSION/$NAME.kicad_pcb "$ORIG_COMPANY" "$COMPANY"
rm ../hardware/$VERSION/template.kicad_pcb
replace_company ../hardware/$VERSION/template.sch ../hardware/$VERSION/$NAME.sch "$ORIG_COMPANY" "$COMPANY"
rm ../hardware/$VERSION/template.sch

sed -i "s/VER_NO/$VERSION/" ../hardware/$VERSION/$NAME.*
sed -i "s/DESIGN_TITLE/$NAME/" ../hardware/$VERSION/$NAME.*
 
echo "+++ DONE"