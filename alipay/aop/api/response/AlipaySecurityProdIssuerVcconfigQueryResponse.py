#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdIssuerVcconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdIssuerVcconfigQueryResponse, self).__init__()
        self._attribute_schema = None
        self._security_level = None
        self._support_revoke = None
        self._support_select = None

    @property
    def attribute_schema(self):
        return self._attribute_schema

    @attribute_schema.setter
    def attribute_schema(self, value):
        self._attribute_schema = value
    @property
    def security_level(self):
        return self._security_level

    @security_level.setter
    def security_level(self, value):
        self._security_level = value
    @property
    def support_revoke(self):
        return self._support_revoke

    @support_revoke.setter
    def support_revoke(self, value):
        self._support_revoke = value
    @property
    def support_select(self):
        return self._support_select

    @support_select.setter
    def support_select(self, value):
        self._support_select = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdIssuerVcconfigQueryResponse, self).parse_response_content(response_content)
        if 'attribute_schema' in response:
            self.attribute_schema = response['attribute_schema']
        if 'security_level' in response:
            self.security_level = response['security_level']
        if 'support_revoke' in response:
            self.support_revoke = response['support_revoke']
        if 'support_select' in response:
            self.support_select = response['support_select']
