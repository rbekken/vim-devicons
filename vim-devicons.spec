Name:           vim-devicons
Summary:        Adds file type icons to Vim plugins

Version:        0.11.0
Release:        1%{?dist}

License:        MIT
URL:            https://github.com/ryanoasis/vim-devicons

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  vim-filesystem

Requires:       vim-enhanced


%description
Supports plugins such as NERDTree, vim-airline, CtrlP, powerline, denite,
unite, lightline.vim, vim-startify, vimfiler, vim-buffet and flagship.

Features:

- Adds filetype glyphs (icons) to various vim plugins.
- Customizable and extendable glyphs settings.
- Supports a wide range of file type extensions.
- Supports popular full filenames, like .gitignore, node_modules, .vimrc, and
  many more.
- Supports byte order marker (BOM).
- Works with patched fonts, especially Nerd Fonts.


%prep
%autosetup

%install
mkdir -p                                                %{buildroot}%{vimfiles_root}
cp -r {autoload,nerdtree_plugin,plugin,pythonx,rplugin} %{buildroot}%{vimfiles_root}


%files
%license LICENSE
%doc README.md CHANGELOG.md DEVELOPER.md CONTRIBUTING.md doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/nerdtree_plugin/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/pythonx/
%{vimfiles_root}/rplugin/


%changelog
* Sun Aug 31 2025 Roy Bekken <roy.bekken@gmail.com> - 0.11.0-1
- Initial RPM
