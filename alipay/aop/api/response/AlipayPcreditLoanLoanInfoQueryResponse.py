#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseLoanApplyVO import BaseLoanApplyVO


class AlipayPcreditLoanLoanInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanLoanInfoQueryResponse, self).__init__()
        self._base_apply_list = None
        self._total = None

    @property
    def base_apply_list(self):
        return self._base_apply_list

    @base_apply_list.setter
    def base_apply_list(self, value):
        if isinstance(value, list):
            self._base_apply_list = list()
            for i in value:
                if isinstance(i, BaseLoanApplyVO):
                    self._base_apply_list.append(i)
                else:
                    self._base_apply_list.append(BaseLoanApplyVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanLoanInfoQueryResponse, self).parse_response_content(response_content)
        if 'base_apply_list' in response:
            self.base_apply_list = response['base_apply_list']
        if 'total' in response:
            self.total = response['total']
