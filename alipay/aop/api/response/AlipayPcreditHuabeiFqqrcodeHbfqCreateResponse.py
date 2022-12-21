#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiFqqrcodeHbfqCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiFqqrcodeHbfqCreateResponse, self).__init__()
        self._apply = None
        self._process_id = None

    @property
    def apply(self):
        return self._apply

    @apply.setter
    def apply(self, value):
        self._apply = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiFqqrcodeHbfqCreateResponse, self).parse_response_content(response_content)
        if 'apply' in response:
            self.apply = response['apply']
        if 'process_id' in response:
            self.process_id = response['process_id']
