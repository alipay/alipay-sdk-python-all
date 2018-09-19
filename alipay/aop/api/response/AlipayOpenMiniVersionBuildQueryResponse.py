#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniVersionBuildQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionBuildQueryResponse, self).__init__()
        self._build_status = None
        self._create_status = None
        self._need_rotation = None
        self._version_created = None

    @property
    def build_status(self):
        return self._build_status

    @build_status.setter
    def build_status(self, value):
        self._build_status = value
    @property
    def create_status(self):
        return self._create_status

    @create_status.setter
    def create_status(self, value):
        self._create_status = value
    @property
    def need_rotation(self):
        return self._need_rotation

    @need_rotation.setter
    def need_rotation(self, value):
        self._need_rotation = value
    @property
    def version_created(self):
        return self._version_created

    @version_created.setter
    def version_created(self, value):
        self._version_created = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionBuildQueryResponse, self).parse_response_content(response_content)
        if 'build_status' in response:
            self.build_status = response['build_status']
        if 'create_status' in response:
            self.create_status = response['create_status']
        if 'need_rotation' in response:
            self.need_rotation = response['need_rotation']
        if 'version_created' in response:
            self.version_created = response['version_created']
