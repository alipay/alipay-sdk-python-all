#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportIndustryDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryDataSyncResponse, self).__init__()
        self._sync_response = None

    @property
    def sync_response(self):
        return self._sync_response

    @sync_response.setter
    def sync_response(self, value):
        self._sync_response = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryDataSyncResponse, self).parse_response_content(response_content)
        if 'sync_response' in response:
            self.sync_response = response['sync_response']
