#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpOpporFeedbackModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpOpporFeedbackModifyResponse, self).__init__()
        self._msg = None
        self._success = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpOpporFeedbackModifyResponse, self).parse_response_content(response_content)
        if 'msg' in response:
            self.msg = response['msg']
        if 'success' in response:
            self.success = response['success']
