#
# spec file for package yast2-rdp
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           yast2-rdp
Version:        3.1.3
Release:        0
License:        GPL-2.0
Group:          System/YaST
Summary:        Setup Remote Desktop Protocol service for remote administration
URL:            https://www.suse.com
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  perl-XML-Writer update-desktop-files yast2 yast2-testsuite yast2-network
BuildRequires:  yast2-devtools
Requires:       yast2 yast2-ruby-bindings

%description
Configure RDP (remote desktop protocol) daemon to allow remote system administration.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%dir %{yast_yncludedir}/rdp
%{yast_yncludedir}/rdp/*
%{yast_clientdir}/rdp.rb
%{yast_clientdir}/rdp_*.rb
%{yast_moduledir}/RDP.*
%{yast_desktopdir}/rdp.desktop
%doc %{yast_docdir}

%changelog
