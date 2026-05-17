.PHONY: setup-upstream rebase-upstream

UPSTREAM_URL := https://github.com/chatmail/relay.git

# Add or update the upstream remote to chatmail/relay.
setup-upstream:
	@if git remote get-url upstream >/dev/null 2>&1; then \
		git remote set-url upstream $(UPSTREAM_URL); \
	else \
		git remote add upstream $(UPSTREAM_URL); \
	fi
	git remote -v | grep upstream

# Sync main with chatmail/relay upstream, keeping qxp commits on top.
rebase-upstream:
	git fetch upstream
	git rebase upstream/main main
	git push --force-with-lease origin main
