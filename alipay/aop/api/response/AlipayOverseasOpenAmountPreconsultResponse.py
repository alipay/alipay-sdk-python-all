#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionISVAmountInfoDTO import TuitionISVAmountInfoDTO
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult


class AlipayOverseasOpenAmountPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenAmountPreconsultResponse, self).__init__()
        self._amount_info = None
        self._reference_id = None
        self._result = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, TuitionISVAmountInfoDTO):
            self._amount_info = value
        else:
            self._amount_info = TuitionISVAmountInfoDTO.from_alipay_dict(value)
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, TuitionISVResult):
            self._result = value
        else:
            self._result = TuitionISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenAmountPreconsultResponse, self).parse_response_content(response_content)
        if 'amount_info' in response:
            self.amount_info = response['amount_info']
        if 'reference_id' in response:
            self.reference_id = response['reference_id']
        if 'result' in response:
            self.result = response['result']
