#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineSmddOcrImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddOcrImageUploadResponse, self).__init__()
        self._afts_url = None

    @property
    def afts_url(self):
        return self._afts_url

    @afts_url.setter
    def afts_url(self, value):
        self._afts_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddOcrImageUploadResponse, self).parse_response_content(response_content)
        if 'afts_url' in response:
            self.afts_url = response['afts_url']
