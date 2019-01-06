# Dockerfile for providing buildozer
# Build with:
# docker build --tag=buildozer .
# In order to give the container access to your current working directory
# it must be mounted using the --volume option.
# Run with (e.g. `buildozer --version`):
# docker run --volume "$(pwd)":/home/user/hostcwd buildozer --version
# Or for interactive shell:
# docker run --volume "$(pwd)":/home/user/hostcwd --entrypoint /bin/bash -it --rm buildozer
FROM ubuntu:18.04

ENV USER="user"
ENV HOME_DIR="/home/${USER}"
ENV WORK_DIR="${HOME_DIR}/hostcwd" \
    PATH="${HOME_DIR}/.local/bin:${PATH}"

# configures locale
RUN apt update -qq > /dev/null && \
    apt install -qq --yes --no-install-recommends \
    locales && \
    locale-gen en_US.UTF-8 && \
    apt install -qq --yes mc openssh-client nano wget curl pkg-config autoconf automake libtool time
ENV LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

# installs system dependencies (required to setup all the tools)
RUN apt install -qq --yes --no-install-recommends \
    sudo python-pip python-setuptools file

# https://buildozer.readthedocs.io/en/latest/installation.html#android-on-ubuntu-18-04-64bit
RUN dpkg --add-architecture i386 && apt update -qq > /dev/null && \
	apt install -qq --yes --no-install-recommends \
	build-essential ccache git libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 \
	libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python2.7 \
	python2.7-dev openjdk-8-jdk unzip zlib1g-dev zlib1g:i386

# prepares non root env
RUN useradd --create-home --shell /bin/bash ${USER}
# with sudo access and no password
RUN usermod -append --groups sudo ${USER}
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER ${USER}
WORKDIR ${WORK_DIR}

# installs buildozer and dependencies
RUN pip install --user Cython==0.25.2 buildozer==0.34 sh
# calling buildozer adb command should trigger SDK/NDK first install and update
# but it requires a buildozer.spec file

ARG DOT_VERSION=0.1.0
ARG DOT_HASH=675b3ede7c44253ece2b6bd3c44b14750698aec783e438585b7646939b9e16e3
ARG DOT_PATH=https://github.com/homdx/pydelhi_mobile/releases/download
ARG DOT_FILE=dot-buildozer-py-home.tar.gz
ARG DOT_HASH2=4a4d8bdbd17642f355e5c58d87b2da57f7ec0e806c9de38fbc9a3a9186ebd1cb
ARG DOT_PATH2=https://github.com/homdx/pydelhi_mobile/releases/download
ARG DOT_FILE2=dot-buildozer-py.tar.gz


#USER ${USER}

RUN sudo mkdir app  && sudo chown user app \
  &&  set -ex \
  && cd ${HOME_DIR} && sudo time -p wget --quiet ${DOT_PATH}/${DOT_VERSION}/${DOT_FILE} \
  && echo "${DOT_HASH}  ${DOT_FILE}" | sha256sum -c \
  && sudo tar -xf ${DOT_FILE} && sudo rm ${DOT_FILE} \
  && time -p sudo chown user -R ${HOME_DIR}/.buildozer && time -p sudo chown user -R ${HOME_DIR}

#RUN cd /tmp/ && buildozer init && buildozer android adb -- version \
#    && cd ~/.buildozer/android/platform/&& rm -vf android-ndk*.tar* android-sdk*.tgz apache-ant*.tar.gz \
#    && cd -
# fixes source and target JDK version, refs https://github.com/kivy/buildozer/issues/625
RUN sed s/'name="java.source" value="1.5"'/'name="java.source" value="7"'/ -i ${HOME_DIR}/.buildozer/android/platform/android-sdk-20/tools/ant/build.xml
RUN sed s/'name="java.target" value="1.5"'/'name="java.target" value="7"'/ -i ${HOME_DIR}/.buildozer/android/platform/android-sdk-20/tools/ant/build.xml

#RUN wget https://www.crystax.net/download/crystax-ndk-10.3.1-linux-x86_64.tar.xz?interactive=true -O ~/.buildozer/crystax.tar.xz \
#  && cd ~/.buildozer/ \
#  && tar -xvf crystax.tar.xz && rm ~/.buildozer/crystax.tar.xz 

#USER root

#RUN chown user /home/user/ -R && chown user /home/user/hostcwd

USER ${USER}

COPY . app

RUN  sudo chown user -R app/ \
  && cd app \
  && time -p wget --quiet ${DOT_PATH}/${DOT_VERSION}/${DOT_FILE2} \
  && echo "${DOT_HASH2}  ${DOT_FILE2}" | sha256sum -c \
  && tar -xf ${DOT_FILE2} && rm ${DOT_FILE2} \
  && time -p buildozer android debug || /bin/true

RUN sudo cp /home/user/hostcwd/app/.buildozer/android/platform/build/dists/conference/bin/PyDelhiConf*debug.apk ${WORK_DIR}

CMD tail -f /var/log/faillog

#ENTRYPOINT ["buildozer"]
