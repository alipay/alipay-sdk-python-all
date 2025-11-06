#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCsfuServicehallSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCsfuServicehallSyncResponse, self).__init__()
        self._action = None
        self._interruptible = None
        self._output_content = None
        self._request_id = None
        self._transfer_target_code = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def interruptible(self):
        return self._interruptible

    @interruptible.setter
    def interruptible(self, value):
        self._interruptible = value
    @property
    def output_content(self):
        return self._output_content

    @output_content.setter
    def output_content(self, value):
        self._output_content = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def transfer_target_code(self):
        return self._transfer_target_code

    @transfer_target_code.setter
    def transfer_target_code(self, value):
        self._transfer_target_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCsfuServicehallSyncResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'interruptible' in response:
            self.interruptible = response['interruptible']
        if 'output_content' in response:
            self.output_content = response['output_content']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'transfer_target_code' in response:
            self.transfer_target_code = response['transfer_target_code']
