#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneKidsCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneKidsCloseResponse, self).__init__()
        self._close_success = None

    @property
    def close_success(self):
        return self._close_success

    @close_success.setter
    def close_success(self, value):
        self._close_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneKidsCloseResponse, self).parse_response_content(response_content)
        if 'close_success' in response:
            self.close_success = response['close_success']
