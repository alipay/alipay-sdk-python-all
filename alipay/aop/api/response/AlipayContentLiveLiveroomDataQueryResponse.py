#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLiveLiveroomDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveLiveroomDataQueryResponse, self).__init__()
        self._count_uv = None

    @property
    def count_uv(self):
        return self._count_uv

    @count_uv.setter
    def count_uv(self, value):
        self._count_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveLiveroomDataQueryResponse, self).parse_response_content(response_content)
        if 'count_uv' in response:
            self.count_uv = response['count_uv']
