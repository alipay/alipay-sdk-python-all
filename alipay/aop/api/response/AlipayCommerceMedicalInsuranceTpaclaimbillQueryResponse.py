#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CbClaimBill import CbClaimBill


class AlipayCommerceMedicalInsuranceTpaclaimbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceTpaclaimbillQueryResponse, self).__init__()
        self._claim_bill_list = None
        self._current_page = None
        self._total_count = None
        self._total_page = None

    @property
    def claim_bill_list(self):
        return self._claim_bill_list

    @claim_bill_list.setter
    def claim_bill_list(self, value):
        if isinstance(value, CbClaimBill):
            self._claim_bill_list = value
        else:
            self._claim_bill_list = CbClaimBill.from_alipay_dict(value)
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceTpaclaimbillQueryResponse, self).parse_response_content(response_content)
        if 'claim_bill_list' in response:
            self.claim_bill_list = response['claim_bill_list']
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page' in response:
            self.total_page = response['total_page']
