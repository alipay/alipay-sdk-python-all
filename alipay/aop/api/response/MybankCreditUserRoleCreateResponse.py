#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserRoleCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserRoleCreateResponse, self).__init__()
        self._ip_id = None
        self._ip_role_id = None

    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserRoleCreateResponse, self).parse_response_content(response_content)
        if 'ip_id' in response:
            self.ip_id = response['ip_id']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
