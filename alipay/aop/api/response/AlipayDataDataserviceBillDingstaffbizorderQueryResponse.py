#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillDingBizOrder import BillDingBizOrder
from alipay.aop.api.domain.BillDingBizOrderSum import BillDingBizOrderSum


class AlipayDataDataserviceBillDingstaffbizorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceBillDingstaffbizorderQueryResponse, self).__init__()
        self._bill_list = None
        self._bill_sum = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, BillDingBizOrder):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(BillDingBizOrder.from_alipay_dict(i))
    @property
    def bill_sum(self):
        return self._bill_sum

    @bill_sum.setter
    def bill_sum(self, value):
        if isinstance(value, list):
            self._bill_sum = list()
            for i in value:
                if isinstance(i, BillDingBizOrderSum):
                    self._bill_sum.append(i)
                else:
                    self._bill_sum.append(BillDingBizOrderSum.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceBillDingstaffbizorderQueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'bill_sum' in response:
            self.bill_sum = response['bill_sum']
