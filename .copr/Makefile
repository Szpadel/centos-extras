srpm:
	rpmbuild -bs $(spec) --define '_sourcedir $(CURDIR)' --define '_specdir $(CURDIR)' --define '_srcrpmdir $(outdir)' --target x86_64
	rpmbuild -bs $(spec) --define '_sourcedir $(CURDIR)' --define '_specdir $(CURDIR)' --define '_srcrpmdir $(outdir) --target i686
