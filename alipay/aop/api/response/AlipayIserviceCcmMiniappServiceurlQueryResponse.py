#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmMiniappServiceurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmMiniappServiceurlQueryResponse, self).__init__()
        self._service_url = None

    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmMiniappServiceurlQueryResponse, self).parse_response_content(response_content)
        if 'service_url' in response:
            self.service_url = response['service_url']
