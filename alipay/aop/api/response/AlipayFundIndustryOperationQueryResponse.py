#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundOperationDTO import FundOperationDTO


class AlipayFundIndustryOperationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundIndustryOperationQueryResponse, self).__init__()
        self._operation = None

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        if isinstance(value, FundOperationDTO):
            self._operation = value
        else:
            self._operation = FundOperationDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundIndustryOperationQueryResponse, self).parse_response_content(response_content)
        if 'operation' in response:
            self.operation = response['operation']
