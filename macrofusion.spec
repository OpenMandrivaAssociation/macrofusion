Name:		macrofusion
Version:	0.7.3
Release:	2
Group:		Graphics
Summary:	GUI for HDR tool Enfuse
License:	GPLv3
URL:		http://sourceforge.net/projects/macrofusion
Source0:	http://sourceforge.net/projects/macrofusion/files/%{name}-%{version}/%{name}_%{version}.orig.tar.gz
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


%changelog
* Sun Feb 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7.3-1
+ Revision: 777444
- update to 0.7.3
- drop separate Russian localisation files as they are merged upstream

* Mon Feb 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7.2-3
+ Revision: 771320
- add russian translation

* Tue Jan 31 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7.2-2
+ Revision: 770034
- fixed file installation paths

* Tue Jan 31 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7.2-1
+ Revision: 770024
- new version 0.7.2

* Tue Nov 15 2011 Andrey Smirnov <asmirnov@mandriva.org> 0.6-1
+ Revision: 730781
- imported package macrofusion

