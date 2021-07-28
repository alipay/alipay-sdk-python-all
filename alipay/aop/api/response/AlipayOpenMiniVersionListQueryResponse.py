#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppVersionInfo import AppVersionInfo


class AlipayOpenMiniVersionListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionListQueryResponse, self).__init__()
        self._app_version_infos = None
        self._app_versions = None

    @property
    def app_version_infos(self):
        return self._app_version_infos

    @app_version_infos.setter
    def app_version_infos(self, value):
        if isinstance(value, list):
            self._app_version_infos = list()
            for i in value:
                if isinstance(i, AppVersionInfo):
                    self._app_version_infos.append(i)
                else:
                    self._app_version_infos.append(AppVersionInfo.from_alipay_dict(i))
    @property
    def app_versions(self):
        return self._app_versions

    @app_versions.setter
    def app_versions(self, value):
        if isinstance(value, list):
            self._app_versions = list()
            for i in value:
                self._app_versions.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionListQueryResponse, self).parse_response_content(response_content)
        if 'app_version_infos' in response:
            self.app_version_infos = response['app_version_infos']
        if 'app_versions' in response:
            self.app_versions = response['app_versions']
