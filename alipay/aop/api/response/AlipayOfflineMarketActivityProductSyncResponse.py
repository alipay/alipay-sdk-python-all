#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketActivityProductSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketActivityProductSyncResponse, self).__init__()
        self._failed_activity_batch_ids = None

    @property
    def failed_activity_batch_ids(self):
        return self._failed_activity_batch_ids

    @failed_activity_batch_ids.setter
    def failed_activity_batch_ids(self, value):
        if isinstance(value, list):
            self._failed_activity_batch_ids = list()
            for i in value:
                self._failed_activity_batch_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketActivityProductSyncResponse, self).parse_response_content(response_content)
        if 'failed_activity_batch_ids' in response:
            self.failed_activity_batch_ids = response['failed_activity_batch_ids']
