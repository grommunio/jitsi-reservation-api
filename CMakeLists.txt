cmake_minimum_required(VERSION 3.14)
project(jitsi-reservation-api VERSION 1.0 LANGUAGES NONE)

include(GNUInstallDirs)

find_package(PkgConfig REQUIRED)

set(INSTALLDIR ${CMAKE_INSTALL_FULL_DATADIR}/jitsi-reservation-api)
pkg_get_variable(TMPFILESDIR systemd tmpfilesdir)
pkg_get_variable(UNITDIR systemd systemdsystemunitdir)

install(DIRECTORY endpoints orm DESTINATION ${INSTALLDIR})
install(PROGRAMS main.py DESTINATION ${INSTALLDIR})
install(FILES data/api-config.ini config.yaml DESTINATION ${INSTALLDIR})

install(FILES data/jitsi-reservation-api.service data/jitsi-reservation-api.socket DESTINATION ${UNITDIR})

