#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefuseVo import RefuseVo
from alipay.aop.api.domain.BillRepayResult import BillRepayResult


class MybankCreditLoantradeBillRepayQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeBillRepayQueryResponse, self).__init__()
        self._refuse_msg = None
        self._repay_result = None
        self._succ = None

    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, RefuseVo):
            self._refuse_msg = value
        else:
            self._refuse_msg = RefuseVo.from_alipay_dict(value)
    @property
    def repay_result(self):
        return self._repay_result

    @repay_result.setter
    def repay_result(self, value):
        if isinstance(value, BillRepayResult):
            self._repay_result = value
        else:
            self._repay_result = BillRepayResult.from_alipay_dict(value)
    @property
    def succ(self):
        return self._succ

    @succ.setter
    def succ(self, value):
        self._succ = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeBillRepayQueryResponse, self).parse_response_content(response_content)
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'repay_result' in response:
            self.repay_result = response['repay_result']
        if 'succ' in response:
            self.succ = response['succ']
