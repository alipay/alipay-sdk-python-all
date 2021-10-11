#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeCollectrightQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeCollectrightQueryResponse, self).__init__()
        self._can_collect = None

    @property
    def can_collect(self):
        return self._can_collect

    @can_collect.setter
    def can_collect(self, value):
        self._can_collect = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeCollectrightQueryResponse, self).parse_response_content(response_content)
        if 'can_collect' in response:
            self.can_collect = response['can_collect']
