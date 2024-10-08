#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoQueuePushSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoQueuePushSyncResponse, self).__init__()
        self._queue_sync = None

    @property
    def queue_sync(self):
        return self._queue_sync

    @queue_sync.setter
    def queue_sync(self, value):
        self._queue_sync = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoQueuePushSyncResponse, self).parse_response_content(response_content)
        if 'queue_sync' in response:
            self.queue_sync = response['queue_sync']
