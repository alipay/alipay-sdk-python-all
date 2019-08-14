#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodAccountQueryResponse, self).__init__()
        self._name = None
        self._pid = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodAccountQueryResponse, self).parse_response_content(response_content)
        if 'name' in response:
            self.name = response['name']
        if 'pid' in response:
            self.pid = response['pid']
