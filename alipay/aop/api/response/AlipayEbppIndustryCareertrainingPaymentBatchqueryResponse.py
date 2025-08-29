#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentObject import PaymentObject


class AlipayEbppIndustryCareertrainingPaymentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingPaymentBatchqueryResponse, self).__init__()
        self._list = None
        self._total = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, PaymentObject):
            self._list = value
        else:
            self._list = PaymentObject.from_alipay_dict(value)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingPaymentBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'total' in response:
            self.total = response['total']
