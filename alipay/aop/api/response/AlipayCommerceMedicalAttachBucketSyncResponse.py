#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAttachBucketSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAttachBucketSyncResponse, self).__init__()
        self._sync_flag = None

    @property
    def sync_flag(self):
        return self._sync_flag

    @sync_flag.setter
    def sync_flag(self, value):
        self._sync_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAttachBucketSyncResponse, self).parse_response_content(response_content)
        if 'sync_flag' in response:
            self.sync_flag = response['sync_flag']
