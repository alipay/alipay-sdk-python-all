#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceIdentityInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceIdentityInitializeResponse, self).__init__()
        self._extend_field = None
        self._verify_id = None

    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceIdentityInitializeResponse, self).parse_response_content(response_content)
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
