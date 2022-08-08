#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerCansearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerCansearchQueryResponse, self).__init__()
        self._can_search = None

    @property
    def can_search(self):
        return self._can_search

    @can_search.setter
    def can_search(self, value):
        self._can_search = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerCansearchQueryResponse, self).parse_response_content(response_content)
        if 'can_search' in response:
            self.can_search = response['can_search']
