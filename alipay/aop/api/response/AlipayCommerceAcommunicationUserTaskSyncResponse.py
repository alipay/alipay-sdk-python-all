#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationUserTaskSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationUserTaskSyncResponse, self).__init__()
        self._sync_success = None

    @property
    def sync_success(self):
        return self._sync_success

    @sync_success.setter
    def sync_success(self, value):
        self._sync_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationUserTaskSyncResponse, self).parse_response_content(response_content)
        if 'sync_success' in response:
            self.sync_success = response['sync_success']
