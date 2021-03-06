#!/bin/bash
#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
#
# Script for running ydk CI on docker via travis-ci.org
#
# ------------------------------------------------------------------

RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

function print_msg {
    echo -e "${MSG_COLOR}*** $(date) *** dependencies_osx.sh | $@ ${NOCOLOR}"
}

function run_cmd {
    local cmd=$@
    print_msg "Running: $cmd"
    $@
    local status=$?
    if [ $status -ne 0 ]; then
        MSG_COLOR=$RED
        print_msg "Exiting '$@' with status=$status"
        exit $status
    fi
    return $status
}

function install_dependencies {
    print_msg "install_dependencies"

    brew install curl doxygen wget xml2
#                 pcre  \
#                 lcov

#    brew install libssh
#    brew link libssh
}

function install_confd {
    print_msg "install_confd"

    wget https://github.com/CiscoDevNet/ydk-gen/files/562559/confd-basic-6.2.darwin.x86_64.zip
    unzip confd-basic-6.2.darwin.x86_64.zip
    ./confd-basic-6.2.darwin.x86_64.installer.bin ../confd
}

function download_moco {
    print_msg "Downloading moco"
    cd test
    wget https://repo1.maven.org/maven2/com/github/dreamhead/moco-runner/0.11.0/moco-runner-0.11.0-standalone.jar
    cd -
}

function check_python_installation {
  print_msg "Checking python and pip installation"
  python3 -V
  status=$?
  if [ $status -ne 0 ]; then
    print_msg "Installing python3"
    brew upgrade python
  fi
  pip3 -V
  status=$?
  if [ $status -ne 0 ]; then
    print_msg "Installing pip3"
    run_cmd curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    run_cmd sudo -H python3 get-pip.py
  fi
  sudo pip3 install virtualenv
}

########################## EXECUTION STARTS HERE #############################

install_dependencies
install_confd
download_moco

check_python_installation
