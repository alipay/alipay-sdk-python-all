#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdAlipaySecurityProdTestResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAlipaySecurityProdTestResponse, self).__init__()
        self._admin = None

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, value):
        self._admin = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAlipaySecurityProdTestResponse, self).parse_response_content(response_content)
        if 'admin' in response:
            self.admin = response['admin']
