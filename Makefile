VERSION ?= 1.0.1
CACHE ?= --no-cache=1
FULLVERSION ?= 1.0.1
archs ?= amd64 i386 arm64v8 arm32v6

.PHONY: all build publish latest
all: build publish latest
qemu-arm-static:
	cp /usr/bin/qemu-arm-static .
qemu-aarch64-static:
	cp /usr/bin/qemu-aarch64-static .
build: qemu-arm-static qemu-aarch64-static
	$(foreach arch,$(archs), \
		cat Dockerfile | sed "s/FROM python:alpine/FROM ${arch}\/python:alpine/g" > .Dockerfile; \
		docker build -t jaymoulin/google-musicmanager-dedup-api:${VERSION}-$(arch) -t ghcr.io/jaymoulin/google-musicmanager-dedup-api:${VERSION}-$(arch) -f .Dockerfile --build-arg VERSION=${VERSION} ${CACHE} .;\
	)
publish:
	docker push jaymoulin/google-musicmanager-dedup-api -a
	docker push ghcr.io/jaymoulin/google-musicmanager-dedup-api -a
	cat manifest.yml | sed "s/\$$VERSION/${VERSION}/g" > manifest.yaml
	cat manifest.yaml | sed "s/\$$FULLVERSION/${FULLVERSION}/g" > manifest2.yaml
	mv manifest2.yaml manifest.yaml
	manifest-tool push from-spec manifest.yaml
	cat manifest.yaml | sed "s/jaymoukin/ghcr.io\/jaymoulin/g" > manifest2.yaml
	mv manifest2.yaml manifest.yaml
	manifest-tool push from-spec manifest.yaml
latest:
	FULLVERSION=latest VERSION=${VERSION} make publish

