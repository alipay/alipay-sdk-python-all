#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseCreateResponse, self).__init__()
        self._enterprise_id = None
        self._iot_group_id = None
        self._iot_logic_group_id = None
        self._sign_url = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def iot_group_id(self):
        return self._iot_group_id

    @iot_group_id.setter
    def iot_group_id(self, value):
        self._iot_group_id = value
    @property
    def iot_logic_group_id(self):
        return self._iot_logic_group_id

    @iot_logic_group_id.setter
    def iot_logic_group_id(self, value):
        self._iot_logic_group_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseCreateResponse, self).parse_response_content(response_content)
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'iot_group_id' in response:
            self.iot_group_id = response['iot_group_id']
        if 'iot_logic_group_id' in response:
            self.iot_logic_group_id = response['iot_logic_group_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
