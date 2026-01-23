#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAnzhenerMessageSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAnzhenerMessageSyncResponse, self).__init__()
        self._send_sync_message = None

    @property
    def send_sync_message(self):
        return self._send_sync_message

    @send_sync_message.setter
    def send_sync_message(self, value):
        self._send_sync_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAnzhenerMessageSyncResponse, self).parse_response_content(response_content)
        if 'send_sync_message' in response:
            self.send_sync_message = response['send_sync_message']
