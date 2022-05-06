#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspUserwithvidCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspUserwithvidCreateResponse, self).__init__()
        self._unique_id = None

    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspUserwithvidCreateResponse, self).parse_response_content(response_content)
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
