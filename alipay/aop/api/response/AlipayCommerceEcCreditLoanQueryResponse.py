#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanApply import LoanApply


class AlipayCommerceEcCreditLoanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcCreditLoanQueryResponse, self).__init__()
        self._loan_apply_infos = None

    @property
    def loan_apply_infos(self):
        return self._loan_apply_infos

    @loan_apply_infos.setter
    def loan_apply_infos(self, value):
        if isinstance(value, list):
            self._loan_apply_infos = list()
            for i in value:
                if isinstance(i, LoanApply):
                    self._loan_apply_infos.append(i)
                else:
                    self._loan_apply_infos.append(LoanApply.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcCreditLoanQueryResponse, self).parse_response_content(response_content)
        if 'loan_apply_infos' in response:
            self.loan_apply_infos = response['loan_apply_infos']
