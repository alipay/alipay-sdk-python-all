#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneUserQueryResponse, self).__init__()
        self._open_status = None

    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneUserQueryResponse, self).parse_response_content(response_content)
        if 'open_status' in response:
            self.open_status = response['open_status']
