#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderVerifyphotoNpassporterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderVerifyphotoNpassporterQueryResponse, self).__init__()
        self._photo_url = None

    @property
    def photo_url(self):
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        self._photo_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderVerifyphotoNpassporterQueryResponse, self).parse_response_content(response_content)
        if 'photo_url' in response:
            self.photo_url = response['photo_url']
