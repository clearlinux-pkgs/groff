#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1A60EACE707FDA5 (wl@gnu.org)
#
Name     : groff
Version  : 1.22.2
Release  : 15
URL      : https://ftp.gnu.org/gnu/groff/groff-1.22.2.tar.gz
Source0  : https://ftp.gnu.org/gnu/groff/groff-1.22.2.tar.gz
Source99 : https://ftp.gnu.org/gnu/groff/groff-1.22.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+ MIT
Requires: groff-bin
Requires: groff-doc
Requires: groff-data
BuildRequires : bison
BuildRequires : texinfo
Patch1: usr-bin-sed.patch
Patch2: timestamp.patch

%description
This is the GNU `groff' document formatting system.  The version
number is given in the file VERSION.

%package bin
Summary: bin components for the groff package.
Group: Binaries
Requires: groff-data

%description bin
bin components for the groff package.


%package data
Summary: data components for the groff package.
Group: Data

%description data
data components for the groff package.


%package doc
Summary: doc components for the groff package.
Group: Documentation

%description doc
doc components for the groff package.


%prep
%setup -q -n groff-1.22.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493230969
%configure --disable-static
make V=1

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1493230969
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/groff/groffer/func.pl
/usr/lib64/groff/groffer/man.pl
/usr/lib64/groff/groffer/perl_test.pl
/usr/lib64/groff/groffer/split_env.sh
/usr/lib64/groff/groffer/version.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/addftinfo
/usr/bin/afmtodit
/usr/bin/chem
/usr/bin/eqn
/usr/bin/eqn2graph
/usr/bin/gdiffmk
/usr/bin/grap2graph
/usr/bin/grn
/usr/bin/grodvi
/usr/bin/groff
/usr/bin/groffer
/usr/bin/grog
/usr/bin/grolbp
/usr/bin/grolj4
/usr/bin/gropdf
/usr/bin/grops
/usr/bin/grotty
/usr/bin/hpftodit
/usr/bin/indxbib
/usr/bin/lkbib
/usr/bin/lookbib
/usr/bin/mmroff
/usr/bin/neqn
/usr/bin/nroff
/usr/bin/pdfmom
/usr/bin/pdfroff
/usr/bin/pfbtops
/usr/bin/pic
/usr/bin/pic2graph
/usr/bin/post-grohtml
/usr/bin/pre-grohtml
/usr/bin/preconv
/usr/bin/refer
/usr/bin/roff2dvi
/usr/bin/roff2html
/usr/bin/roff2pdf
/usr/bin/roff2ps
/usr/bin/roff2text
/usr/bin/roff2x
/usr/bin/soelim
/usr/bin/tbl
/usr/bin/tfmtodit
/usr/bin/troff

%files data
%defattr(-,root,root,-)
/usr/share/groff/1.22.2/eign
/usr/share/groff/1.22.2/font/devascii/B
/usr/share/groff/1.22.2/font/devascii/BI
/usr/share/groff/1.22.2/font/devascii/DESC
/usr/share/groff/1.22.2/font/devascii/I
/usr/share/groff/1.22.2/font/devascii/R
/usr/share/groff/1.22.2/font/devdvi/CW
/usr/share/groff/1.22.2/font/devdvi/CWEC
/usr/share/groff/1.22.2/font/devdvi/CWI
/usr/share/groff/1.22.2/font/devdvi/CWIEC
/usr/share/groff/1.22.2/font/devdvi/CWITC
/usr/share/groff/1.22.2/font/devdvi/CWTC
/usr/share/groff/1.22.2/font/devdvi/DESC
/usr/share/groff/1.22.2/font/devdvi/EX
/usr/share/groff/1.22.2/font/devdvi/HB
/usr/share/groff/1.22.2/font/devdvi/HBEC
/usr/share/groff/1.22.2/font/devdvi/HBI
/usr/share/groff/1.22.2/font/devdvi/HBIEC
/usr/share/groff/1.22.2/font/devdvi/HBITC
/usr/share/groff/1.22.2/font/devdvi/HBTC
/usr/share/groff/1.22.2/font/devdvi/HI
/usr/share/groff/1.22.2/font/devdvi/HIEC
/usr/share/groff/1.22.2/font/devdvi/HITC
/usr/share/groff/1.22.2/font/devdvi/HR
/usr/share/groff/1.22.2/font/devdvi/HREC
/usr/share/groff/1.22.2/font/devdvi/HRTC
/usr/share/groff/1.22.2/font/devdvi/MI
/usr/share/groff/1.22.2/font/devdvi/S
/usr/share/groff/1.22.2/font/devdvi/SA
/usr/share/groff/1.22.2/font/devdvi/SB
/usr/share/groff/1.22.2/font/devdvi/SC
/usr/share/groff/1.22.2/font/devdvi/TB
/usr/share/groff/1.22.2/font/devdvi/TBEC
/usr/share/groff/1.22.2/font/devdvi/TBI
/usr/share/groff/1.22.2/font/devdvi/TBIEC
/usr/share/groff/1.22.2/font/devdvi/TBITC
/usr/share/groff/1.22.2/font/devdvi/TBTC
/usr/share/groff/1.22.2/font/devdvi/TI
/usr/share/groff/1.22.2/font/devdvi/TIEC
/usr/share/groff/1.22.2/font/devdvi/TITC
/usr/share/groff/1.22.2/font/devdvi/TR
/usr/share/groff/1.22.2/font/devdvi/TREC
/usr/share/groff/1.22.2/font/devdvi/TRTC
/usr/share/groff/1.22.2/font/devdvi/generate/CompileFonts
/usr/share/groff/1.22.2/font/devdvi/generate/Makefile
/usr/share/groff/1.22.2/font/devdvi/generate/ec.map
/usr/share/groff/1.22.2/font/devdvi/generate/msam.map
/usr/share/groff/1.22.2/font/devdvi/generate/msbm.map
/usr/share/groff/1.22.2/font/devdvi/generate/tc.map
/usr/share/groff/1.22.2/font/devdvi/generate/texb.map
/usr/share/groff/1.22.2/font/devdvi/generate/texex.map
/usr/share/groff/1.22.2/font/devdvi/generate/texi.map
/usr/share/groff/1.22.2/font/devdvi/generate/texmi.map
/usr/share/groff/1.22.2/font/devdvi/generate/texr.map
/usr/share/groff/1.22.2/font/devdvi/generate/texsy.map
/usr/share/groff/1.22.2/font/devdvi/generate/textex.map
/usr/share/groff/1.22.2/font/devdvi/generate/textt.map
/usr/share/groff/1.22.2/font/devhtml/B
/usr/share/groff/1.22.2/font/devhtml/BI
/usr/share/groff/1.22.2/font/devhtml/CB
/usr/share/groff/1.22.2/font/devhtml/CBI
/usr/share/groff/1.22.2/font/devhtml/CI
/usr/share/groff/1.22.2/font/devhtml/CR
/usr/share/groff/1.22.2/font/devhtml/DESC
/usr/share/groff/1.22.2/font/devhtml/I
/usr/share/groff/1.22.2/font/devhtml/R
/usr/share/groff/1.22.2/font/devhtml/S
/usr/share/groff/1.22.2/font/devlatin1/B
/usr/share/groff/1.22.2/font/devlatin1/BI
/usr/share/groff/1.22.2/font/devlatin1/DESC
/usr/share/groff/1.22.2/font/devlatin1/I
/usr/share/groff/1.22.2/font/devlatin1/R
/usr/share/groff/1.22.2/font/devlbp/CB
/usr/share/groff/1.22.2/font/devlbp/CI
/usr/share/groff/1.22.2/font/devlbp/CR
/usr/share/groff/1.22.2/font/devlbp/DESC
/usr/share/groff/1.22.2/font/devlbp/EB
/usr/share/groff/1.22.2/font/devlbp/EI
/usr/share/groff/1.22.2/font/devlbp/ER
/usr/share/groff/1.22.2/font/devlbp/HB
/usr/share/groff/1.22.2/font/devlbp/HBI
/usr/share/groff/1.22.2/font/devlbp/HI
/usr/share/groff/1.22.2/font/devlbp/HNB
/usr/share/groff/1.22.2/font/devlbp/HNBI
/usr/share/groff/1.22.2/font/devlbp/HNI
/usr/share/groff/1.22.2/font/devlbp/HNR
/usr/share/groff/1.22.2/font/devlbp/HR
/usr/share/groff/1.22.2/font/devlbp/TB
/usr/share/groff/1.22.2/font/devlbp/TBI
/usr/share/groff/1.22.2/font/devlbp/TI
/usr/share/groff/1.22.2/font/devlbp/TR
/usr/share/groff/1.22.2/font/devlj4/AB
/usr/share/groff/1.22.2/font/devlj4/ABI
/usr/share/groff/1.22.2/font/devlj4/AI
/usr/share/groff/1.22.2/font/devlj4/ALBB
/usr/share/groff/1.22.2/font/devlj4/ALBR
/usr/share/groff/1.22.2/font/devlj4/AOB
/usr/share/groff/1.22.2/font/devlj4/AOI
/usr/share/groff/1.22.2/font/devlj4/AOR
/usr/share/groff/1.22.2/font/devlj4/AR
/usr/share/groff/1.22.2/font/devlj4/CB
/usr/share/groff/1.22.2/font/devlj4/CBI
/usr/share/groff/1.22.2/font/devlj4/CI
/usr/share/groff/1.22.2/font/devlj4/CLARENDON
/usr/share/groff/1.22.2/font/devlj4/CORONET
/usr/share/groff/1.22.2/font/devlj4/CR
/usr/share/groff/1.22.2/font/devlj4/DESC
/usr/share/groff/1.22.2/font/devlj4/GB
/usr/share/groff/1.22.2/font/devlj4/GBI
/usr/share/groff/1.22.2/font/devlj4/GI
/usr/share/groff/1.22.2/font/devlj4/GR
/usr/share/groff/1.22.2/font/devlj4/LGB
/usr/share/groff/1.22.2/font/devlj4/LGI
/usr/share/groff/1.22.2/font/devlj4/LGR
/usr/share/groff/1.22.2/font/devlj4/MARIGOLD
/usr/share/groff/1.22.2/font/devlj4/OB
/usr/share/groff/1.22.2/font/devlj4/OBI
/usr/share/groff/1.22.2/font/devlj4/OI
/usr/share/groff/1.22.2/font/devlj4/OR
/usr/share/groff/1.22.2/font/devlj4/S
/usr/share/groff/1.22.2/font/devlj4/SYMBOL
/usr/share/groff/1.22.2/font/devlj4/TB
/usr/share/groff/1.22.2/font/devlj4/TBI
/usr/share/groff/1.22.2/font/devlj4/TI
/usr/share/groff/1.22.2/font/devlj4/TNRB
/usr/share/groff/1.22.2/font/devlj4/TNRBI
/usr/share/groff/1.22.2/font/devlj4/TNRI
/usr/share/groff/1.22.2/font/devlj4/TNRR
/usr/share/groff/1.22.2/font/devlj4/TR
/usr/share/groff/1.22.2/font/devlj4/UB
/usr/share/groff/1.22.2/font/devlj4/UBI
/usr/share/groff/1.22.2/font/devlj4/UCB
/usr/share/groff/1.22.2/font/devlj4/UCBI
/usr/share/groff/1.22.2/font/devlj4/UCI
/usr/share/groff/1.22.2/font/devlj4/UCR
/usr/share/groff/1.22.2/font/devlj4/UI
/usr/share/groff/1.22.2/font/devlj4/UR
/usr/share/groff/1.22.2/font/devlj4/WINGDINGS
/usr/share/groff/1.22.2/font/devlj4/generate/Makefile
/usr/share/groff/1.22.2/font/devlj4/generate/special.awk
/usr/share/groff/1.22.2/font/devlj4/generate/special.map
/usr/share/groff/1.22.2/font/devlj4/generate/symbol.map
/usr/share/groff/1.22.2/font/devlj4/generate/text.map
/usr/share/groff/1.22.2/font/devlj4/generate/wingdings.map
/usr/share/groff/1.22.2/font/devpdf/CB
/usr/share/groff/1.22.2/font/devpdf/CBI
/usr/share/groff/1.22.2/font/devpdf/CI
/usr/share/groff/1.22.2/font/devpdf/CR
/usr/share/groff/1.22.2/font/devpdf/DESC
/usr/share/groff/1.22.2/font/devpdf/EURO
/usr/share/groff/1.22.2/font/devpdf/Foundry
/usr/share/groff/1.22.2/font/devpdf/HB
/usr/share/groff/1.22.2/font/devpdf/HBI
/usr/share/groff/1.22.2/font/devpdf/HI
/usr/share/groff/1.22.2/font/devpdf/HR
/usr/share/groff/1.22.2/font/devpdf/S
/usr/share/groff/1.22.2/font/devpdf/TB
/usr/share/groff/1.22.2/font/devpdf/TBI
/usr/share/groff/1.22.2/font/devpdf/TI
/usr/share/groff/1.22.2/font/devpdf/TR
/usr/share/groff/1.22.2/font/devpdf/ZD
/usr/share/groff/1.22.2/font/devpdf/download
/usr/share/groff/1.22.2/font/devpdf/enc/text.enc
/usr/share/groff/1.22.2/font/devpdf/map/dingbats.map
/usr/share/groff/1.22.2/font/devpdf/map/symbolchars
/usr/share/groff/1.22.2/font/devpdf/map/symbolmap
/usr/share/groff/1.22.2/font/devpdf/map/textmap
/usr/share/groff/1.22.2/font/devps/AB
/usr/share/groff/1.22.2/font/devps/ABI
/usr/share/groff/1.22.2/font/devps/AI
/usr/share/groff/1.22.2/font/devps/AR
/usr/share/groff/1.22.2/font/devps/BMB
/usr/share/groff/1.22.2/font/devps/BMBI
/usr/share/groff/1.22.2/font/devps/BMI
/usr/share/groff/1.22.2/font/devps/BMR
/usr/share/groff/1.22.2/font/devps/CB
/usr/share/groff/1.22.2/font/devps/CBI
/usr/share/groff/1.22.2/font/devps/CI
/usr/share/groff/1.22.2/font/devps/CR
/usr/share/groff/1.22.2/font/devps/DESC
/usr/share/groff/1.22.2/font/devps/EURO
/usr/share/groff/1.22.2/font/devps/HB
/usr/share/groff/1.22.2/font/devps/HBI
/usr/share/groff/1.22.2/font/devps/HI
/usr/share/groff/1.22.2/font/devps/HNB
/usr/share/groff/1.22.2/font/devps/HNBI
/usr/share/groff/1.22.2/font/devps/HNI
/usr/share/groff/1.22.2/font/devps/HNR
/usr/share/groff/1.22.2/font/devps/HR
/usr/share/groff/1.22.2/font/devps/NB
/usr/share/groff/1.22.2/font/devps/NBI
/usr/share/groff/1.22.2/font/devps/NI
/usr/share/groff/1.22.2/font/devps/NR
/usr/share/groff/1.22.2/font/devps/PB
/usr/share/groff/1.22.2/font/devps/PBI
/usr/share/groff/1.22.2/font/devps/PI
/usr/share/groff/1.22.2/font/devps/PR
/usr/share/groff/1.22.2/font/devps/S
/usr/share/groff/1.22.2/font/devps/SS
/usr/share/groff/1.22.2/font/devps/TB
/usr/share/groff/1.22.2/font/devps/TBI
/usr/share/groff/1.22.2/font/devps/TI
/usr/share/groff/1.22.2/font/devps/TR
/usr/share/groff/1.22.2/font/devps/ZCMI
/usr/share/groff/1.22.2/font/devps/ZD
/usr/share/groff/1.22.2/font/devps/ZDR
/usr/share/groff/1.22.2/font/devps/download
/usr/share/groff/1.22.2/font/devps/freeeuro.afm
/usr/share/groff/1.22.2/font/devps/freeeuro.pfa
/usr/share/groff/1.22.2/font/devps/generate/Makefile
/usr/share/groff/1.22.2/font/devps/generate/afmname
/usr/share/groff/1.22.2/font/devps/generate/dingbats.map
/usr/share/groff/1.22.2/font/devps/generate/dingbats.rmap
/usr/share/groff/1.22.2/font/devps/generate/lgreekmap
/usr/share/groff/1.22.2/font/devps/generate/symbol.sed
/usr/share/groff/1.22.2/font/devps/generate/symbolchars
/usr/share/groff/1.22.2/font/devps/generate/symbolsl.afm
/usr/share/groff/1.22.2/font/devps/generate/textmap
/usr/share/groff/1.22.2/font/devps/prologue
/usr/share/groff/1.22.2/font/devps/symbolsl.pfa
/usr/share/groff/1.22.2/font/devps/text.enc
/usr/share/groff/1.22.2/font/devps/zapfdr.pfa
/usr/share/groff/1.22.2/font/devutf8/B
/usr/share/groff/1.22.2/font/devutf8/BI
/usr/share/groff/1.22.2/font/devutf8/DESC
/usr/share/groff/1.22.2/font/devutf8/I
/usr/share/groff/1.22.2/font/devutf8/R
/usr/share/groff/1.22.2/oldfont/devps/CB
/usr/share/groff/1.22.2/oldfont/devps/CBI
/usr/share/groff/1.22.2/oldfont/devps/CI
/usr/share/groff/1.22.2/oldfont/devps/CR
/usr/share/groff/1.22.2/oldfont/devps/HB
/usr/share/groff/1.22.2/oldfont/devps/HBI
/usr/share/groff/1.22.2/oldfont/devps/HI
/usr/share/groff/1.22.2/oldfont/devps/HNB
/usr/share/groff/1.22.2/oldfont/devps/HNBI
/usr/share/groff/1.22.2/oldfont/devps/HNI
/usr/share/groff/1.22.2/oldfont/devps/HNR
/usr/share/groff/1.22.2/oldfont/devps/HR
/usr/share/groff/1.22.2/oldfont/devps/NB
/usr/share/groff/1.22.2/oldfont/devps/NBI
/usr/share/groff/1.22.2/oldfont/devps/NI
/usr/share/groff/1.22.2/oldfont/devps/NR
/usr/share/groff/1.22.2/oldfont/devps/PB
/usr/share/groff/1.22.2/oldfont/devps/PBI
/usr/share/groff/1.22.2/oldfont/devps/PI
/usr/share/groff/1.22.2/oldfont/devps/PR
/usr/share/groff/1.22.2/oldfont/devps/S
/usr/share/groff/1.22.2/oldfont/devps/SS
/usr/share/groff/1.22.2/oldfont/devps/TB
/usr/share/groff/1.22.2/oldfont/devps/TBI
/usr/share/groff/1.22.2/oldfont/devps/TI
/usr/share/groff/1.22.2/oldfont/devps/TR
/usr/share/groff/1.22.2/oldfont/devps/symbol.afm
/usr/share/groff/1.22.2/oldfont/devps/symbolsl.afm
/usr/share/groff/1.22.2/oldfont/devps/zapfdr.afm
/usr/share/groff/1.22.2/oldfont/devps/zapfdr.ps
/usr/share/groff/1.22.2/pic/chem.pic
/usr/share/groff/1.22.2/tmac/62bit.tmac
/usr/share/groff/1.22.2/tmac/X.tmac
/usr/share/groff/1.22.2/tmac/Xps.tmac
/usr/share/groff/1.22.2/tmac/a4.tmac
/usr/share/groff/1.22.2/tmac/an-ext.tmac
/usr/share/groff/1.22.2/tmac/an-old.tmac
/usr/share/groff/1.22.2/tmac/an.tmac
/usr/share/groff/1.22.2/tmac/andoc.tmac
/usr/share/groff/1.22.2/tmac/composite.tmac
/usr/share/groff/1.22.2/tmac/cp1047.tmac
/usr/share/groff/1.22.2/tmac/cs.tmac
/usr/share/groff/1.22.2/tmac/de.tmac
/usr/share/groff/1.22.2/tmac/den.tmac
/usr/share/groff/1.22.2/tmac/devtag.tmac
/usr/share/groff/1.22.2/tmac/doc-old.tmac
/usr/share/groff/1.22.2/tmac/doc.tmac
/usr/share/groff/1.22.2/tmac/dvi.tmac
/usr/share/groff/1.22.2/tmac/e.tmac
/usr/share/groff/1.22.2/tmac/ec.tmac
/usr/share/groff/1.22.2/tmac/eqnrc
/usr/share/groff/1.22.2/tmac/europs.tmac
/usr/share/groff/1.22.2/tmac/fallbacks.tmac
/usr/share/groff/1.22.2/tmac/fr.tmac
/usr/share/groff/1.22.2/tmac/hdmisc.tmac
/usr/share/groff/1.22.2/tmac/hdtbl.tmac
/usr/share/groff/1.22.2/tmac/html-end.tmac
/usr/share/groff/1.22.2/tmac/html.tmac
/usr/share/groff/1.22.2/tmac/hyphen.cs
/usr/share/groff/1.22.2/tmac/hyphen.den
/usr/share/groff/1.22.2/tmac/hyphen.det
/usr/share/groff/1.22.2/tmac/hyphen.fr
/usr/share/groff/1.22.2/tmac/hyphen.sv
/usr/share/groff/1.22.2/tmac/hyphen.us
/usr/share/groff/1.22.2/tmac/hyphenex.cs
/usr/share/groff/1.22.2/tmac/hyphenex.det
/usr/share/groff/1.22.2/tmac/hyphenex.us
/usr/share/groff/1.22.2/tmac/ja.tmac
/usr/share/groff/1.22.2/tmac/latin1.tmac
/usr/share/groff/1.22.2/tmac/latin2.tmac
/usr/share/groff/1.22.2/tmac/latin5.tmac
/usr/share/groff/1.22.2/tmac/latin9.tmac
/usr/share/groff/1.22.2/tmac/lbp.tmac
/usr/share/groff/1.22.2/tmac/lj4.tmac
/usr/share/groff/1.22.2/tmac/m.tmac
/usr/share/groff/1.22.2/tmac/man.tmac
/usr/share/groff/1.22.2/tmac/mandoc.tmac
/usr/share/groff/1.22.2/tmac/mdoc.tmac
/usr/share/groff/1.22.2/tmac/mdoc/doc-common
/usr/share/groff/1.22.2/tmac/mdoc/doc-ditroff
/usr/share/groff/1.22.2/tmac/mdoc/doc-nroff
/usr/share/groff/1.22.2/tmac/mdoc/doc-syms
/usr/share/groff/1.22.2/tmac/me.tmac
/usr/share/groff/1.22.2/tmac/mm.tmac
/usr/share/groff/1.22.2/tmac/mm/0.MT
/usr/share/groff/1.22.2/tmac/mm/4.MT
/usr/share/groff/1.22.2/tmac/mm/5.MT
/usr/share/groff/1.22.2/tmac/mm/locale
/usr/share/groff/1.22.2/tmac/mm/ms.cov
/usr/share/groff/1.22.2/tmac/mm/se_locale
/usr/share/groff/1.22.2/tmac/mm/se_ms.cov
/usr/share/groff/1.22.2/tmac/mmse.tmac
/usr/share/groff/1.22.2/tmac/mom.tmac
/usr/share/groff/1.22.2/tmac/ms.tmac
/usr/share/groff/1.22.2/tmac/mse.tmac
/usr/share/groff/1.22.2/tmac/om.tmac
/usr/share/groff/1.22.2/tmac/papersize.tmac
/usr/share/groff/1.22.2/tmac/pdf.tmac
/usr/share/groff/1.22.2/tmac/pdfmark.tmac
/usr/share/groff/1.22.2/tmac/pic.tmac
/usr/share/groff/1.22.2/tmac/ps.tmac
/usr/share/groff/1.22.2/tmac/psatk.tmac
/usr/share/groff/1.22.2/tmac/psold.tmac
/usr/share/groff/1.22.2/tmac/pspic.tmac
/usr/share/groff/1.22.2/tmac/refer-me.tmac
/usr/share/groff/1.22.2/tmac/refer-mm.tmac
/usr/share/groff/1.22.2/tmac/refer-ms.tmac
/usr/share/groff/1.22.2/tmac/refer.tmac
/usr/share/groff/1.22.2/tmac/s.tmac
/usr/share/groff/1.22.2/tmac/safer.tmac
/usr/share/groff/1.22.2/tmac/spdf.tmac
/usr/share/groff/1.22.2/tmac/sv.tmac
/usr/share/groff/1.22.2/tmac/trace.tmac
/usr/share/groff/1.22.2/tmac/trans.tmac
/usr/share/groff/1.22.2/tmac/troffrc
/usr/share/groff/1.22.2/tmac/troffrc-end
/usr/share/groff/1.22.2/tmac/tty-char.tmac
/usr/share/groff/1.22.2/tmac/tty.tmac
/usr/share/groff/1.22.2/tmac/unicode.tmac
/usr/share/groff/1.22.2/tmac/www.tmac
/usr/share/groff/current
/usr/share/groff/site-tmac/man.local
/usr/share/groff/site-tmac/mdoc.local

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/groff/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
