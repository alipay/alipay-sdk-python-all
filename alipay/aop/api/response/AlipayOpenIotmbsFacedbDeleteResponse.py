#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsFacedbDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsFacedbDeleteResponse, self).__init__()
        self._success = None

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsFacedbDeleteResponse, self).parse_response_content(response_content)
        if 'success' in response:
            self.success = response['success']
