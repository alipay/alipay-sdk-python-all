#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult


class AlipayOverseasOpenAccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenAccountConsultResponse, self).__init__()
        self._account_id = None
        self._result = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
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
        response = super(AlipayOverseasOpenAccountConsultResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'result' in response:
            self.result = response['result']
