Name:		block-led-trigger
Version:	0.1
Release:	1%{?dist}
Summary:	Block device activity LED trigger
License:	GPLv2

BuildArch:	noarch
Source:		block-led-trigger.tar

BuildRequires:		systemd 
Requires:		kernel-devel
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Block device activity LED trigger

%prep
%setup -n block-led-trigger

%build

%install
mkdir -p %{buildroot}%{_prefix}/share/block-led-trigger
cp -v block-led-trigger Makefile block_led_trigger.c %{buildroot}%{_prefix}/share/block-led-trigger/

mkdir -p %{buildroot}%{_unitdir}
cp -v block-led-trigger.service %{buildroot}%{_unitdir}

%clean
rm -rf %{buildroot}

%post
%systemd_post block-led-trigger.service

%preun
%systemd_preun block-led-trigger.service

%postun
%systemd_postun_with_restart block-led-trigger.service

%files
%defattr(-,root,root,-)
%{_prefix}/share/block-led-trigger
%{_unitdir}/block-led-trigger.service

%changelog
* Wed Aug 5 2015 Fabio D'Urso <fabiodurso@hotmail.com> 0.1-1
- Initial version.
