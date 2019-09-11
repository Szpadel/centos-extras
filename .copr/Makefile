rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')
.PHONY: prepare srpm rpm

prepare:
	dnf -y install rpmdevtools rpm-build
	spectool -g -R $(spec)

srpm: prepare
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec) --target x86_64
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec) --target i686

rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" $(spec) --target x86_64
	rpmbuild -bb --define "_rpmdir $(outdir)" $(spec) --target i686
