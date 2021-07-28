#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniDeploypackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDeploypackageQueryResponse, self).__init__()
        self._pack_json = None

    @property
    def pack_json(self):
        return self._pack_json

    @pack_json.setter
    def pack_json(self, value):
        self._pack_json = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDeploypackageQueryResponse, self).parse_response_content(response_content)
        if 'pack_json' in response:
            self.pack_json = response['pack_json']
