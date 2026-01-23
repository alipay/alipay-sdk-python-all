#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndrbeneficiaryApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrbeneficiaryApplyResponse, self).__init__()
        self._beneficiary_id = None
        self._result = None

    @property
    def beneficiary_id(self):
        return self._beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value):
        self._beneficiary_id = value
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
        response = super(AlipayOverseasOpenIndrbeneficiaryApplyResponse, self).parse_response_content(response_content)
        if 'beneficiary_id' in response:
            self.beneficiary_id = response['beneficiary_id']
        if 'result' in response:
            self.result = response['result']
