#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCorpusBatchSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCorpusBatchSyncResponse, self).__init__()
        self._sync_batch_id = None

    @property
    def sync_batch_id(self):
        return self._sync_batch_id

    @sync_batch_id.setter
    def sync_batch_id(self, value):
        self._sync_batch_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCorpusBatchSyncResponse, self).parse_response_content(response_content)
        if 'sync_batch_id' in response:
            self.sync_batch_id = response['sync_batch_id']
