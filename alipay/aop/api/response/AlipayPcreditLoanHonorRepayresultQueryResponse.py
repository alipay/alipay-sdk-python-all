#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorRepayApplyTermDTO import HonorRepayApplyTermDTO


class AlipayPcreditLoanHonorRepayresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorRepayresultQueryResponse, self).__init__()
        self._out_repay_no = None
        self._repay_amount = None
        self._repay_no = None
        self._repay_result = None
        self._repay_status = None
        self._repay_terms = None
        self._repay_time = None

    @property
    def out_repay_no(self):
        return self._out_repay_no

    @out_repay_no.setter
    def out_repay_no(self, value):
        self._out_repay_no = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_no(self):
        return self._repay_no

    @repay_no.setter
    def repay_no(self, value):
        self._repay_no = value
    @property
    def repay_result(self):
        return self._repay_result

    @repay_result.setter
    def repay_result(self, value):
        self._repay_result = value
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value
    @property
    def repay_terms(self):
        return self._repay_terms

    @repay_terms.setter
    def repay_terms(self, value):
        if isinstance(value, list):
            self._repay_terms = list()
            for i in value:
                if isinstance(i, HonorRepayApplyTermDTO):
                    self._repay_terms.append(i)
                else:
                    self._repay_terms.append(HonorRepayApplyTermDTO.from_alipay_dict(i))
    @property
    def repay_time(self):
        return self._repay_time

    @repay_time.setter
    def repay_time(self, value):
        self._repay_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorRepayresultQueryResponse, self).parse_response_content(response_content)
        if 'out_repay_no' in response:
            self.out_repay_no = response['out_repay_no']
        if 'repay_amount' in response:
            self.repay_amount = response['repay_amount']
        if 'repay_no' in response:
            self.repay_no = response['repay_no']
        if 'repay_result' in response:
            self.repay_result = response['repay_result']
        if 'repay_status' in response:
            self.repay_status = response['repay_status']
        if 'repay_terms' in response:
            self.repay_terms = response['repay_terms']
        if 'repay_time' in response:
            self.repay_time = response['repay_time']
