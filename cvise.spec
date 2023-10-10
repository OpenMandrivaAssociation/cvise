#define date 20230415
%global optflags %{optflags} -Wno-error=unknown-warning-option -Wno-error=unused-but-set-variable

Name: cvise
Version: 2.8.0
Release: %{?date:0.%{date}.}1
%if 0%{?date:1}
Source0: https://github.com/marxin/cvise/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
%else
Source0: https://github.com/marxin/cvise/archive/refs/tags/v%{version}.tar.gz
%endif
# Patches 0 to 5 are LLVM 17 support from master branch
Patch0: https://github.com/marxin/cvise/commit/20cac24b794987f09321201130452f2102e26194.patch
Patch1: https://github.com/marxin/cvise/commit/47b20cd98513e686145e52aa7f8dc081204ad6ea.patch
Patch2: https://github.com/marxin/cvise/commit/9c713b0b95b84968b5e9ef46c20d88c1ade0ab35.patch
Patch3: https://github.com/marxin/cvise/commit/62a7ed03263344cd5d761b80d4af646af6b23815.patch
Patch4: https://github.com/marxin/cvise/commit/ab37cba079049e3c920357c3c25e2deb476b6c32.patch
Patch5: https://github.com/marxin/cvise/commit/c0e2623434a7736e4c4864a822a4a5cf9c8746c1.patch
Summary: Tool for creating reduced test cases for compiler bugs
URL: https://github.com/marxin/cvise
License: MIT
Group: Development/Tools
BuildRequires: python
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: flex
BuildRequires: unifdef
BuildRequires: cmake(LLVM)
BuildRequires: cmake(Clang)
BuildRequires: cmake(MLIR)
BuildRequires: python%{py_ver}dist(pebble)
BuildRequires: python%{py_ver}dist(chardet)
BuildRequires: python%{py_ver}dist(psutil)
BuildRequires: python%{py_ver}dist(pytest)
BuildRequires: llvm-static-devel
Recommends: colordiff

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient LLVM-based C/C++
reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that has a property
of interest (such as triggering a compiler bug) and automatically produces a
much smaller C/C++ or OpenCL program that has the same property. It is intended
for use by people who discover and report bugs in compilers and other tools that
process C/C++ or OpenCL code.

The project also contains a simple wrapper cvise-delta which simulates the same
behavior as original delta tool (but in super-parallel way).

%prep
%autosetup -p1 %{?date:-n %{name}-master}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/cvise
%{_bindir}/cvise-delta
%{_libexecdir}/cvise
%{_datadir}/cvise
