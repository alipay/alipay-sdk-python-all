#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaxBillContent import TaxBillContent


class AlipayIserviceCognitiveInvoicesInferenceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveInvoicesInferenceQueryResponse, self).__init__()
        self._algo_version = None
        self._content = None
        self._err_msg = None
        self._ret = None

    @property
    def algo_version(self):
        return self._algo_version

    @algo_version.setter
    def algo_version(self, value):
        self._algo_version = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, TaxBillContent):
            self._content = value
        else:
            self._content = TaxBillContent.from_alipay_dict(value)
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def ret(self):
        return self._ret

    @ret.setter
    def ret(self, value):
        self._ret = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveInvoicesInferenceQueryResponse, self).parse_response_content(response_content)
        if 'algo_version' in response:
            self.algo_version = response['algo_version']
        if 'content' in response:
            self.content = response['content']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'ret' in response:
            self.ret = response['ret']
