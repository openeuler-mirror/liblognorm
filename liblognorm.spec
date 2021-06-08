Name:             liblognorm
Version:          2.0.3
Release:          8
Summary:          A tool to normalize log data
License:          LGPLv2+
URL:              http://www.liblognorm.com
Source0:          http://www.liblognorm.com/files/download/%{name}-%{version}.tar.gz

BuildRequires:    chrpath libfastjson-devel libestr-devel pcre-devel gcc

%description
Briefly described, liblognorm is a tool to normalize log data.

If you have traffic logs from three different firewalls,liblognorm will
be able to "normalize" the events into generic ones. Among others,it will
extract source and destination ip addresses and ports and make them
available via well-defined fields.As the end resulta common log
analysis application will be able to work on that common set and so
this backend will be independent from the actual firewalls feeding it.

Even better,once we have a well-understood interim format,it is also
easy to convert that into any other vendor specific format,so that you
can use that vendor's analysis tool.

%package     devel
Summary:     Development tools for programs using liblognorm library
Requires:    %{name} = %{version}-%{release} json-c-devel libestr-devel

%description devel
This package provides the development tools for programs using liblognorm library.

%package        help
Summary:        Help document for the netpbm package
BuildRequires:  python-sphinx
Provides:       liblognorm-doc = %{version}-%{release}
Obsoletes:      liblognorm-doc < %{version}-%{release}

%description    help
Help document for the liblognorm package.

%package     utils
Summary:     A utility for normalizing log files
Requires:    %{name} = %{version}-%{release}

%description utils
This package can be known as a lognormalizer utility for normalizing
log files.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --enable-regexp --enable-docs --docdir=%{_docdir}/liblognorm/html \
           --includedir=%{_includedir}/%{name}/

%install
%make_install V=1 INSTALL="install -p"
%delete_la_and_a
chrpath -d %{buildroot}%{_bindir}/lognormalizer
chrpath -d %{buildroot}%{_libdir}/liblognorm.so

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog README COPYING
%exclude %{_docdir}/liblognorm/html
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
%exclude %{_docdir}/liblognorm/html/{objects.inv,.buildinfo}

%files utils
%{_bindir}/lognormalizer

%files help
%doc %{_docdir}/liblognorm/html

%changelog
* Tue Jun 08 2021 wulei <wulei80@huawei.com> - 2.0.3-8
- fixes failed: error: no acceptable C compiler found in $PATH

* Fri Dec 20 2019 wangzhishun <wangzhishun1@huawei.com> - 2.0.3-7
- Package init

