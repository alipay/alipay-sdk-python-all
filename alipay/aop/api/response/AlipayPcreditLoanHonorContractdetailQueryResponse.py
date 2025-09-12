#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorContractDTO import HonorContractDTO


class AlipayPcreditLoanHonorContractdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorContractdetailQueryResponse, self).__init__()
        self._records = None
        self._total_num = None

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, HonorContractDTO):
                    self._records.append(i)
                else:
                    self._records.append(HonorContractDTO.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorContractdetailQueryResponse, self).parse_response_content(response_content)
        if 'records' in response:
            self.records = response['records']
        if 'total_num' in response:
            self.total_num = response['total_num']
