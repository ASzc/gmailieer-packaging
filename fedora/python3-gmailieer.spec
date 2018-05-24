%global srcname gmailieer

Name:           python3-%{srcname}
Version:        0.8
Release:        1%{?dist}
Summary:        Fast email-fetching and two-way tag synchronization between notmuch and GMail

License:        GPLv3+
URL:            https://github.com/gauteh/%{srcname}
Source0:        https://github.com/gauteh/%{srcname}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-tqdm python3-google-api-client python3-oauth2client python3-notmuch notmuch-devel

Requires: python3-tqdm python3-google-api-client python3-oauth2client python3-notmuch

%description
This program can pull email and labels (and changes to labels) from your GMail
account and store them locally in a maildir with the labels synchronized with a
notmuch database. The changes to tags in the notmuch database may be pushed
back remotely to your GMail account.

Gmailieer will not and can not:

    - Add or delete messages on your remote account (except syncing the trash
      or spam label to messages, and those messages will eventually be deleted)
    - Modify messages other than their labels

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license COPYING.GPL-3.0+
%doc README.md LICENSE.md
%{python3_sitelib}/*
%{_bindir}/gmi

%changelog
* Wed May 23 2018 Alex Szczuczko <aszczucz@redhat.com> - 0.8-1
- Update to source version 0.8
* Wed Apr 04 2018 Alex Szczuczko <aszczucz@redhat.com> - 0.6-1
- Update to source version 0.6
* Mon Nov 20 2017 Alex Szczuczko <aszczucz@redhat.com> - 0.4-1
- Initial package
