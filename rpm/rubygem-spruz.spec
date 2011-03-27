#
# spec file for package rubygem-spruz (Version 0.2.2)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild
Name:           rubygem-spruz
Version:        0.2.5
Release:        0
%define mod_name spruz
#
Group:          Development/Languages/Ruby
License:        MIT
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
#
Url:            http://flori.github.com/spruz
Source:         %{mod_name}-%{version}.gem
#
Summary:        Useful stuff
%description
All the stuff that isn't good/big enough for a real library.

%package doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
Requires:       %{name} = %{version}

%description doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.



%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/enum
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/


%changelog
