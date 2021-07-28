#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ThirdErrorContext import ThirdErrorContext


class AlipayTradeCreditProductSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditProductSignResponse, self).__init__()
        self._contract_batch_no = None
        self._contract_no_list = None
        self._third_error_context = None

    @property
    def contract_batch_no(self):
        return self._contract_batch_no

    @contract_batch_no.setter
    def contract_batch_no(self, value):
        self._contract_batch_no = value
    @property
    def contract_no_list(self):
        return self._contract_no_list

    @contract_no_list.setter
    def contract_no_list(self, value):
        self._contract_no_list = value
    @property
    def third_error_context(self):
        return self._third_error_context

    @third_error_context.setter
    def third_error_context(self, value):
        if isinstance(value, ThirdErrorContext):
            self._third_error_context = value
        else:
            self._third_error_context = ThirdErrorContext.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditProductSignResponse, self).parse_response_content(response_content)
        if 'contract_batch_no' in response:
            self.contract_batch_no = response['contract_batch_no']
        if 'contract_no_list' in response:
            self.contract_no_list = response['contract_no_list']
        if 'third_error_context' in response:
            self.third_error_context = response['third_error_context']
