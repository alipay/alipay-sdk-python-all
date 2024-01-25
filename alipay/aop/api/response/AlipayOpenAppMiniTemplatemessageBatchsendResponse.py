#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppMiniTemplatemessageBatchsendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMiniTemplatemessageBatchsendResponse, self).__init__()
        self._batch_msg_id = None

    @property
    def batch_msg_id(self):
        return self._batch_msg_id

    @batch_msg_id.setter
    def batch_msg_id(self, value):
        self._batch_msg_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMiniTemplatemessageBatchsendResponse, self).parse_response_content(response_content)
        if 'batch_msg_id' in response:
            self.batch_msg_id = response['batch_msg_id']
