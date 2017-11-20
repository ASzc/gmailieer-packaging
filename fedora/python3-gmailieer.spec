%global srcname gmailieer
%global sum Fast email-fetching and two-way tag synchronization between notmuch and GMail

Name:           python3-%{srcname}
Version:        0.4
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            https://github.com/gauteh/%{srcname}
Source0:        https://github.com/gauteh/%{srcname}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

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

