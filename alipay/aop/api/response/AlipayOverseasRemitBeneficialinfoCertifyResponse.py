#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasRemitBeneficialinfoCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasRemitBeneficialinfoCertifyResponse, self).__init__()
        self._extend_info = None
        self._is_pass = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def is_pass(self):
        return self._is_pass

    @is_pass.setter
    def is_pass(self, value):
        self._is_pass = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasRemitBeneficialinfoCertifyResponse, self).parse_response_content(response_content)
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'is_pass' in response:
            self.is_pass = response['is_pass']
