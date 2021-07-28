#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionUploadstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionUploadstatusQueryResponse, self).__init__()
        self._build_info = None
        self._build_package_url = None
        self._build_status = None
        self._log_url = None
        self._need_rotation = None
        self._new_build_package_url = None
        self._new_result_url = None
        self._result_url = None
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
    def log_url(self):
        return self._log_url

    @log_url.setter
    def log_url(self, value):
        self._log_url = value
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
    def new_result_url(self):
        return self._new_result_url

    @new_result_url.setter
    def new_result_url(self, value):
        self._new_result_url = value
    @property
    def result_url(self):
        return self._result_url

    @result_url.setter
    def result_url(self, value):
        self._result_url = value
    @property
    def version_created(self):
        return self._version_created

    @version_created.setter
    def version_created(self, value):
        self._version_created = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionUploadstatusQueryResponse, self).parse_response_content(response_content)
        if 'build_info' in response:
            self.build_info = response['build_info']
        if 'build_package_url' in response:
            self.build_package_url = response['build_package_url']
        if 'build_status' in response:
            self.build_status = response['build_status']
        if 'log_url' in response:
            self.log_url = response['log_url']
        if 'need_rotation' in response:
            self.need_rotation = response['need_rotation']
        if 'new_build_package_url' in response:
            self.new_build_package_url = response['new_build_package_url']
        if 'new_result_url' in response:
            self.new_result_url = response['new_result_url']
        if 'result_url' in response:
            self.result_url = response['result_url']
        if 'version_created' in response:
            self.version_created = response['version_created']
