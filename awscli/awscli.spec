%global pkg awscli
%global binary aws
Name:           %{pkg}
Version:        1.16.253
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS

License:        Apache License 2.0
URL:            http://aws.amazon.com/cli/
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}

%description
aws-cli This package provides a unified command line interface to Amazon Web
Services.The aws-cli package works on Python versions:* 2.6.5 and greater *
2.7.x and greater * 3.3.x and greater * 3.4.x and greater * 3.5.x and greater *
3.6.x and greater * 3.7.x and greater.. attention:: We recommend that all
customers regularly monitor the Amazon Web Services Security Bulletins website_
for any...

%prep

%build
%{__python3} -m venv --copies venv
source ./venv/bin/activate
pip install %{pkg}==%{version}
pip uninstall -y pip setuptools
virtualenv --relocatable venv
deactivate
rm venv/bin/activate* venv/bin/Activate*
rm venv/bin/python venv/bin/python3

%install
mkdir -p %{buildroot}%{_datadir}/%{pkg}
cp -r venv/* %{buildroot}%{_datadir}/%{pkg}/

%posttrans
alternatives --install %{_bindir}/%{binary} %{binary} %{_datadir}/%{pkg}/bin/%{binary} %{version}
ln -s %{_bindir}/python %{_datadir}/%{pkg}/bin/python
ln -s %{_bindir}/python3 %{_datadir}/%{pkg}/bin/python3

%files
%ghost %{_bindir}/%{binary}
%ghost %{_datadir}/%{pkg}/bin/python
%ghost %{_datadir}/%{pkg}/bin/python3
%{_datadir}/%{pkg}/

%changelog
* Mon Oct 07 2019 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 1.16.253-1
- Initial package.
