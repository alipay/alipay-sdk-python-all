#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderBroadcastCoilBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderBroadcastCoilBindResponse, self).__init__()
        self._bind_result = None
        self._route_url = None
        self._tag_id = None

    @property
    def bind_result(self):
        return self._bind_result

    @bind_result.setter
    def bind_result(self, value):
        self._bind_result = value
    @property
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        self._route_url = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderBroadcastCoilBindResponse, self).parse_response_content(response_content)
        if 'bind_result' in response:
            self.bind_result = response['bind_result']
        if 'route_url' in response:
            self.route_url = response['route_url']
        if 'tag_id' in response:
            self.tag_id = response['tag_id']
