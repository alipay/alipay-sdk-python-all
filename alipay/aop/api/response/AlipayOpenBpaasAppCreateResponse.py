#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenBpaasAppCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBpaasAppCreateResponse, self).__init__()
        self._app_name = None
        self._app_platform = None
        self._app_type = None
        self._bpaas_app_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_platform(self):
        return self._app_platform

    @app_platform.setter
    def app_platform(self, value):
        self._app_platform = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def bpaas_app_id(self):
        return self._bpaas_app_id

    @bpaas_app_id.setter
    def bpaas_app_id(self, value):
        self._bpaas_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenBpaasAppCreateResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_platform' in response:
            self.app_platform = response['app_platform']
        if 'app_type' in response:
            self.app_type = response['app_type']
        if 'bpaas_app_id' in response:
            self.bpaas_app_id = response['bpaas_app_id']
