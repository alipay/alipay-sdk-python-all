#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepaymentInfo import RepaymentInfo


class MybankEcnyFundRepaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyFundRepaymentQueryResponse, self).__init__()
        self._repayment_info = None

    @property
    def repayment_info(self):
        return self._repayment_info

    @repayment_info.setter
    def repayment_info(self, value):
        if isinstance(value, list):
            self._repayment_info = list()
            for i in value:
                if isinstance(i, RepaymentInfo):
                    self._repayment_info.append(i)
                else:
                    self._repayment_info.append(RepaymentInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankEcnyFundRepaymentQueryResponse, self).parse_response_content(response_content)
        if 'repayment_info' in response:
            self.repayment_info = response['repayment_info']
