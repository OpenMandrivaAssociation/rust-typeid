# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate typeid

Name:           rust-typeid
Version:        1.0.0
Release:        1
Summary:        Const TypeId and non-'static TypeId
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typeid
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.61

%global _description %{expand:
Const TypeId and non-'static TypeId.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(typeid) = 1.0.0
Requires:       cargo
Requires:       rust >= 1.61

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(typeid/default) = 1.0.0
Requires:       cargo
Requires:       crate(typeid) = 1.0.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
