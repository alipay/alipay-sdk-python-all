#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class HuanxuUserHhhhhDeleteResponse(AlipayResponse):

    def __init__(self):
        super(HuanxuUserHhhhhDeleteResponse, self).__init__()
        self._aa = None
        self._app_name = None
        self._mini_app_id = None
        self._name = None

    @property
    def aa(self):
        return self._aa

    @aa.setter
    def aa(self, value):
        self._aa = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(HuanxuUserHhhhhDeleteResponse, self).parse_response_content(response_content)
        if 'aa' in response:
            self.aa = response['aa']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'name' in response:
            self.name = response['name']
