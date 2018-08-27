#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankFinanceYulibaoCapitalRansomResponse(AlipayResponse):

    def __init__(self):
        super(MybankFinanceYulibaoCapitalRansomResponse, self).__init__()
        self._inner_biz_no = None
        self._remark = None
        self._trans_result = None

    @property
    def inner_biz_no(self):
        return self._inner_biz_no

    @inner_biz_no.setter
    def inner_biz_no(self, value):
        self._inner_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def trans_result(self):
        return self._trans_result

    @trans_result.setter
    def trans_result(self, value):
        self._trans_result = value

    def parse_response_content(self, response_content):
        response = super(MybankFinanceYulibaoCapitalRansomResponse, self).parse_response_content(response_content)
        if 'inner_biz_no' in response:
            self.inner_biz_no = response['inner_biz_no']
        if 'remark' in response:
            self.remark = response['remark']
        if 'trans_result' in response:
            self.trans_result = response['trans_result']
