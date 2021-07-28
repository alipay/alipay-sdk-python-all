#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecuritySssssssQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecuritySssssssQueryResponse, self).__init__()
        self._adfad = None

    @property
    def adfad(self):
        return self._adfad

    @adfad.setter
    def adfad(self, value):
        self._adfad = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecuritySssssssQueryResponse, self).parse_response_content(response_content)
        if 'adfad' in response:
            self.adfad = response['adfad']
