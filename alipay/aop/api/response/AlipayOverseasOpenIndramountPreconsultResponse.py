#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVAmountInfoDTO import IndrISVAmountInfoDTO
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndramountPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndramountPreconsultResponse, self).__init__()
        self._amount_info = None
        self._result = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, IndrISVAmountInfoDTO):
            self._amount_info = value
        else:
            self._amount_info = IndrISVAmountInfoDTO.from_alipay_dict(value)
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
        response = super(AlipayOverseasOpenIndramountPreconsultResponse, self).parse_response_content(response_content)
        if 'amount_info' in response:
            self.amount_info = response['amount_info']
        if 'result' in response:
            self.result = response['result']
