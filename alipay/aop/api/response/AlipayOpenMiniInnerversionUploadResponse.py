#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionUploadResponse, self).__init__()
        self._build_info = None
        self._build_package_url = None
        self._build_status = None
        self._build_version = None
        self._need_rotation = None
        self._new_build_package_url = None
        self._package_id = None
        self._version_created = None

    @property
    def build_info(self):
        return self._build_info

    @build_info.setter
    def build_info(self, value):
        self._build_info = value
    @property
    def build_package_url(self):
        return self._build_package_url

    @build_package_url.setter
    def build_package_url(self, value):
        self._build_package_url = value
    @property
    def build_status(self):
        return self._build_status

    @build_status.setter
    def build_status(self, value):
        self._build_status = value
    @property
    def build_version(self):
        return self._build_version

    @build_version.setter
    def build_version(self, value):
        self._build_version = value
    @property
    def need_rotation(self):
        return self._need_rotation

    @need_rotation.setter
    def need_rotation(self, value):
        self._need_rotation = value
    @property
    def new_build_package_url(self):
        return self._new_build_package_url

    @new_build_package_url.setter
    def new_build_package_url(self, value):
        self._new_build_package_url = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value
    @property
    def version_created(self):
        return self._version_created

    @version_created.setter
    def version_created(self, value):
        self._version_created = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionUploadResponse, self).parse_response_content(response_content)
        if 'build_info' in response:
            self.build_info = response['build_info']
        if 'build_package_url' in response:
            self.build_package_url = response['build_package_url']
        if 'build_status' in response:
            self.build_status = response['build_status']
        if 'build_version' in response:
            self.build_version = response['build_version']
        if 'need_rotation' in response:
            self.need_rotation = response['need_rotation']
        if 'new_build_package_url' in response:
            self.new_build_package_url = response['new_build_package_url']
        if 'package_id' in response:
            self.package_id = response['package_id']
        if 'version_created' in response:
            self.version_created = response['version_created']
