#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailvoiceConfigSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailvoiceConfigSyncResponse, self).__init__()
        self._sync_task_id = None

    @property
    def sync_task_id(self):
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, value):
        self._sync_task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailvoiceConfigSyncResponse, self).parse_response_content(response_content)
        if 'sync_task_id' in response:
            self.sync_task_id = response['sync_task_id']
