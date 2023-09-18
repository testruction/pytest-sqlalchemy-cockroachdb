ARG BASE_IMAGE_TAG="3.11-slim"

FROM docker.io/amd64/python:${BASE_IMAGE_TAG}
ARG IMAGE_VERSION
ARG TZ='America/Montreal'
ENV TZ="${TZ}"
ENV APP_VERSION="${IMAGE_VERSION}"
ENV OCI_USER='python'
ENV OCI_USER_ID='1001'

# https://github.com/opencontainers/image-spec/blob/main/annotations.md
LABEL org.opencontainers.image.vendor="Testruction" \
      org.opencontainers.image.authors='Florian JUDITH <florian.judith.b@gmail.com>' \
      org.opencontainers.image.version=${IMAGE_VERSION} \
	  org.opencontainers.image.title="Dataset Loader Demo" \
	  org.opencontainers.image.description="Dataset Loader for Web demo" \
      org.opencontainers.image.base.name="docker.io/amd64/python:${BASE_IMAGE_TAG}" \
      org.opencontainers.image.source="https://github.com/testruction/pytest-sqlalchemy-cockroachdb"

USER root

# Create the internal user
RUN groupadd --gid="${OCI_USER_ID}" "${OCI_USER}" \
    && useradd --uid="${OCI_USER_ID}" --gid=${OCI_USER_ID} --system "${OCI_USER}"

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get autoremove -y --purge \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

# Copy app source code
COPY ./src /usr/local/app/
COPY ./MANIFEST.in /usr/local/app/
COPY ./pyproject.toml /usr/local/app/
COPY ./README.md /usr/local/app/
COPY ./setup.cfg /usr/local/app/
COPY ./VERSION /usr/local/app/
WORKDIR /usr/local/app/

# Python Build
RUN python3 -m pip install --upgrade pip \
    && pip install -e .[tests,dev] \
    && pip uninstall -y webdemo-dataset

# Startup admission control
COPY ./entrypoint.sh /entrypoint.sh
RUN chown -R ${OCI_USER}:${OCI_USER} \
      /entrypoint.sh \
      /usr/local/app/ \
    && chmod -R a+x \
      /entrypoint.sh \
      /usr/local/app/

# Activation de l'utilisateur intégré
USER ${OCI_USER}

WORKDIR /usr/local/app/src
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["python3", "-m", "fakenamesservice.data_loader"]]
