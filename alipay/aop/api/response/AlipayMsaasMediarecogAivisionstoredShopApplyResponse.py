#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAivisionstoredShopApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionstoredShopApplyResponse, self).__init__()
        self._category_name = None
        self._os_type = None
        self._os_version = None
        self._smile_version = None
        self._sn = None

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def smile_version(self):
        return self._smile_version

    @smile_version.setter
    def smile_version(self, value):
        self._smile_version = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionstoredShopApplyResponse, self).parse_response_content(response_content)
        if 'category_name' in response:
            self.category_name = response['category_name']
        if 'os_type' in response:
            self.os_type = response['os_type']
        if 'os_version' in response:
            self.os_version = response['os_version']
        if 'smile_version' in response:
            self.smile_version = response['smile_version']
        if 'sn' in response:
            self.sn = response['sn']
