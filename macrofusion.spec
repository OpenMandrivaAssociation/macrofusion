Name:		macrofusion
Version:	0.7.2
Release:	2
Group:		Graphics
Summary:	GUI for HDR tool Enfuse
License:	GPLv3
URL:		http://sourceforge.net/projects/macrofusion
Source0:	http://sourceforge.net/projects/macrofusion/files/macrofusion-0.6/%{name}_%{version}.orig.tar.gz
BuildArch:	noarch
Requires:	python
Requires:	python-imaging
Requires:	Image-ExifTool
Requires:	hugin
Requires:	enfuse

%description
MacroFusion is a neat little GUI for great tool Enfuse (command line). It makes
easy fusion few photos to one with great DOF (Deep of Field) or DR (Dynamic
Range). It can be useful for every macro lovers or landscapers.

%prep
%setup -q

%build

%install
install -m 755 -D macrofusion.py %{buildroot}%{_bindir}/macrofusion
install -m 644 -D macrofusion.desktop %{buildroot}%{_datadir}/applications/macrofusion.desktop
install -d -m 755 %{buildroot}%{_datadir}/mfusion/ui
install -m 644 ui/* %{buildroot}%{_datadir}/mfusion/ui/
install -D -m 644 images/macrofusion.png %{buildroot}%{_datadir}/pixmaps/macrofusion.png
install -D -m 644 images/logoSplash.png %{buildroot}%{_datadir}/mfusion/images/logoSplash.png
for file in locale/*/LC_MESSAGES/*.mo
do
install -D -m 644 $file %{buildroot}%{_datadir}/$file
done

%find_lang MacroFusion

%files -f MacroFusion.lang
%{_bindir}/macrofusion
%{_datadir}/mfusion/
%{_datadir}/pixmaps/macrofusion.png
%{_datadir}/applications/macrofusion.desktop
%doc README CHANGELOG TODO
