Summary:	Kinetic protocol description
Summary(pl.UTF-8):	Opis protokołu Kinetic
Name:		kinetic-protocol
Version:	3.0.5
Release:	2
License:	GPL v2+
Group:		Development/Libraries
Source0:	https://github.com/Seagate/kinetic-protocol/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6129e69b6d105f62f219f2748c9b0d86
URL:		https://github.com/Seagate/kinetic-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kinetic is a key-value storage system. A Kinetic Device (e.g. a
Kinetic Drive or a traditional server running the Java Reference
Implementation) stores key-value objects. Kinetic Client applications
can communicate with a Kinetic Device by sending messages over a
network using TCP. Each individual message is called a "Kinetic
Protocol Data Unit" (Kinetic PDU) and represents an individual request
or response. For example, a Kinetic Client may send a message
requesting the value associated with a particular key to a Kinetic
Device. The device would respond with a message containing the value.

%description -l pl.UTF-8
Kinetic to system przechowywania danych klucz-wartość. Urządzenie
Kinetic (np. Kinetic Drive lub tradycyjny serwer z uruchomioną
implementacją wzorcową w Javie) przechowuje obiekty klucz-wartość.
Aplikacje klienckie Kinetic mogą komunikować się z urządzeniem Kinetic
poprzez wysyłanie komunikatów po sieci przy użyciu TCP. Każdy
komunikat jest nazywany "jednostką danych protokołu Kinetic" (Kinetic
PDU - Kinetic Protocol Data Unit) i reprezentuje pojedyncze żądanie
lub odpowiedź. Na przykład: klient Kinetic może wysłać do urządzenia
Kinetic komunikat z żądaniem wartości powiązanej z pewnym kluczem;
urządzenie odpowie komunikatem zawierającym tę wartość.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -p kinetic.proto $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/%{name}
