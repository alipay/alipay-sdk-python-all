#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncWallstreetCompareflowTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncWallstreetCompareflowTransferResponse, self).__init__()
        self._system_success = None

    @property
    def system_success(self):
        return self._system_success

    @system_success.setter
    def system_success(self, value):
        self._system_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncWallstreetCompareflowTransferResponse, self).parse_response_content(response_content)
        if 'system_success' in response:
            self.system_success = response['system_success']
