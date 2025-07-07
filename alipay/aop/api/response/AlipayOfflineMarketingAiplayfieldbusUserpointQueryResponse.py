#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingAiplayfieldbusUserpointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingAiplayfieldbusUserpointQueryResponse, self).__init__()
        self._point = None
        self._request_id = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingAiplayfieldbusUserpointQueryResponse, self).parse_response_content(response_content)
        if 'point' in response:
            self.point = response['point']
        if 'request_id' in response:
            self.request_id = response['request_id']
