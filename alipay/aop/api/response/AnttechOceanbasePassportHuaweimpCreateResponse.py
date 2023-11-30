#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbasePassportHuaweimpCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassportHuaweimpCreateResponse, self).__init__()
        self._passport_id = None

    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassportHuaweimpCreateResponse, self).parse_response_content(response_content)
        if 'passport_id' in response:
            self.passport_id = response['passport_id']
