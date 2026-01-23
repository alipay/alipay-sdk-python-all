#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRentSignSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentSignSyncResponse, self).__init__()
        self._sync_status = None

    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentSignSyncResponse, self).parse_response_content(response_content)
        if 'sync_status' in response:
            self.sync_status = response['sync_status']
