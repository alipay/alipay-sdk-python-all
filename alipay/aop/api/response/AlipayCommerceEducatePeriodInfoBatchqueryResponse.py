#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduPeriodInfo import EduPeriodInfo


class AlipayCommerceEducatePeriodInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePeriodInfoBatchqueryResponse, self).__init__()
        self._period_list = None
        self._total_num = None

    @property
    def period_list(self):
        return self._period_list

    @period_list.setter
    def period_list(self, value):
        if isinstance(value, list):
            self._period_list = list()
            for i in value:
                if isinstance(i, EduPeriodInfo):
                    self._period_list.append(i)
                else:
                    self._period_list.append(EduPeriodInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePeriodInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'period_list' in response:
            self.period_list = response['period_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
