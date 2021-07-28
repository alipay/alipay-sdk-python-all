#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvOcrVatinvoiceIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvOcrVatinvoiceIdentifyResponse, self).__init__()
        self._algo_msg = None
        self._algo_ret = None
        self._message = None
        self._result = None
        self._ret = None

    @property
    def algo_msg(self):
        return self._algo_msg

    @algo_msg.setter
    def algo_msg(self, value):
        self._algo_msg = value
    @property
    def algo_ret(self):
        return self._algo_ret

    @algo_ret.setter
    def algo_ret(self, value):
        self._algo_ret = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def ret(self):
        return self._ret

    @ret.setter
    def ret(self, value):
        self._ret = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvOcrVatinvoiceIdentifyResponse, self).parse_response_content(response_content)
        if 'algo_msg' in response:
            self.algo_msg = response['algo_msg']
        if 'algo_ret' in response:
            self.algo_ret = response['algo_ret']
        if 'message' in response:
            self.message = response['message']
        if 'result' in response:
            self.result = response['result']
        if 'ret' in response:
            self.ret = response['ret']
