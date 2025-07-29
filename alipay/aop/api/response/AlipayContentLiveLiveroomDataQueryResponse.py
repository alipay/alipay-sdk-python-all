#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLiveLiveroomDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveLiveroomDataQueryResponse, self).__init__()
        self._count_uv = None
        self._online_uv = None
        self._praise_count = None

    @property
    def count_uv(self):
        return self._count_uv

    @count_uv.setter
    def count_uv(self, value):
        self._count_uv = value
    @property
    def online_uv(self):
        return self._online_uv

    @online_uv.setter
    def online_uv(self, value):
        self._online_uv = value
    @property
    def praise_count(self):
        return self._praise_count

    @praise_count.setter
    def praise_count(self, value):
        self._praise_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveLiveroomDataQueryResponse, self).parse_response_content(response_content)
        if 'count_uv' in response:
            self.count_uv = response['count_uv']
        if 'online_uv' in response:
            self.online_uv = response['online_uv']
        if 'praise_count' in response:
            self.praise_count = response['praise_count']
