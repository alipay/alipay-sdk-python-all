#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtPunchoutProductSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtPunchoutProductSyncResponse, self).__init__()
        self._ret_value = None
        self._sync_error_msg = None
        self._sync_flag = None

    @property
    def ret_value(self):
        return self._ret_value

    @ret_value.setter
    def ret_value(self, value):
        if isinstance(value, list):
            self._ret_value = list()
            for i in value:
                self._ret_value.append(i)
    @property
    def sync_error_msg(self):
        return self._sync_error_msg

    @sync_error_msg.setter
    def sync_error_msg(self, value):
        self._sync_error_msg = value
    @property
    def sync_flag(self):
        return self._sync_flag

    @sync_flag.setter
    def sync_flag(self, value):
        self._sync_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtPunchoutProductSyncResponse, self).parse_response_content(response_content)
        if 'ret_value' in response:
            self.ret_value = response['ret_value']
        if 'sync_error_msg' in response:
            self.sync_error_msg = response['sync_error_msg']
        if 'sync_flag' in response:
            self.sync_flag = response['sync_flag']
