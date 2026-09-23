#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmountDetail import AmountDetail


class AlipayDataDataserviceAdBudgetapplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdBudgetapplyQueryResponse, self).__init__()
        self._amount_detail = None
        self._apply_no = None
        self._status = None

    @property
    def amount_detail(self):
        return self._amount_detail

    @amount_detail.setter
    def amount_detail(self, value):
        if isinstance(value, AmountDetail):
            self._amount_detail = value
        else:
            self._amount_detail = AmountDetail.from_alipay_dict(value)
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdBudgetapplyQueryResponse, self).parse_response_content(response_content)
        if 'amount_detail' in response:
            self.amount_detail = response['amount_detail']
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'status' in response:
            self.status = response['status']
