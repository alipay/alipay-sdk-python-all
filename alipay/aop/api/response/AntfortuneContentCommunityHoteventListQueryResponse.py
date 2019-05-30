#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneContentCommunityHoteventListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunityHoteventListQueryResponse, self).__init__()
        self._hot_event_product = None
        self._trace_id = None

    @property
    def hot_event_product(self):
        return self._hot_event_product

    @hot_event_product.setter
    def hot_event_product(self, value):
        self._hot_event_product = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunityHoteventListQueryResponse, self).parse_response_content(response_content)
        if 'hot_event_product' in response:
            self.hot_event_product = response['hot_event_product']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
