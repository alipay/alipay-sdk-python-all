#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingAiplayfieldbusPayorderCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingAiplayfieldbusPayorderCheckResponse, self).__init__()
        self._allow = None
        self._ext_text = None
        self._request_id = None

    @property
    def allow(self):
        return self._allow

    @allow.setter
    def allow(self, value):
        self._allow = value
    @property
    def ext_text(self):
        return self._ext_text

    @ext_text.setter
    def ext_text(self, value):
        self._ext_text = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingAiplayfieldbusPayorderCheckResponse, self).parse_response_content(response_content)
        if 'allow' in response:
            self.allow = response['allow']
        if 'ext_text' in response:
            self.ext_text = response['ext_text']
        if 'request_id' in response:
            self.request_id = response['request_id']
