#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepayDetailVO import RepayDetailVO


class AlipayPcreditLoanRepayDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanRepayDetailQueryResponse, self).__init__()
        self._repay_detail_list = None
        self._total = None

    @property
    def repay_detail_list(self):
        return self._repay_detail_list

    @repay_detail_list.setter
    def repay_detail_list(self, value):
        if isinstance(value, list):
            self._repay_detail_list = list()
            for i in value:
                if isinstance(i, RepayDetailVO):
                    self._repay_detail_list.append(i)
                else:
                    self._repay_detail_list.append(RepayDetailVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanRepayDetailQueryResponse, self).parse_response_content(response_content)
        if 'repay_detail_list' in response:
            self.repay_detail_list = response['repay_detail_list']
        if 'total' in response:
            self.total = response['total']
