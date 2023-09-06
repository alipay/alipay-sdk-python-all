#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVReceiptApplyResultDTO import IndrISVReceiptApplyResultDTO
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndrreceiptApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrreceiptApplyResponse, self).__init__()
        self._apply_result_list = None
        self._result = None

    @property
    def apply_result_list(self):
        return self._apply_result_list

    @apply_result_list.setter
    def apply_result_list(self, value):
        if isinstance(value, list):
            self._apply_result_list = list()
            for i in value:
                if isinstance(i, IndrISVReceiptApplyResultDTO):
                    self._apply_result_list.append(i)
                else:
                    self._apply_result_list.append(IndrISVReceiptApplyResultDTO.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenIndrreceiptApplyResponse, self).parse_response_content(response_content)
        if 'apply_result_list' in response:
            self.apply_result_list = response['apply_result_list']
        if 'result' in response:
            self.result = response['result']
