#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndraccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndraccountConsultResponse, self).__init__()
        self._beneficiary_account_id = None
        self._result = None

    @property
    def beneficiary_account_id(self):
        return self._beneficiary_account_id

    @beneficiary_account_id.setter
    def beneficiary_account_id(self, value):
        self._beneficiary_account_id = value
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
        response = super(AlipayOverseasOpenIndraccountConsultResponse, self).parse_response_content(response_content)
        if 'beneficiary_account_id' in response:
            self.beneficiary_account_id = response['beneficiary_account_id']
        if 'result' in response:
            self.result = response['result']
