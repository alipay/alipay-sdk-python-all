#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspBusinessNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspBusinessNotifyResponse, self).__init__()
        self._biz_success = None
        self._fail_reason = None
        self._msg_success = None

    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def msg_success(self):
        return self._msg_success

    @msg_success.setter
    def msg_success(self, value):
        self._msg_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspBusinessNotifyResponse, self).parse_response_content(response_content)
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'msg_success' in response:
            self.msg_success = response['msg_success']
