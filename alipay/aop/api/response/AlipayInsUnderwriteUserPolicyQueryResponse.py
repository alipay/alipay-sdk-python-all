#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPolicy import InsPolicy


class AlipayInsUnderwriteUserPolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsUnderwriteUserPolicyQueryResponse, self).__init__()
        self._policys = None
        self._total = None

    @property
    def policys(self):
        return self._policys

    @policys.setter
    def policys(self, value):
        if isinstance(value, list):
            self._policys = list()
            for i in value:
                if isinstance(i, InsPolicy):
                    self._policys.append(i)
                else:
                    self._policys.append(InsPolicy.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsUnderwriteUserPolicyQueryResponse, self).parse_response_content(response_content)
        if 'policys' in response:
            self.policys = response['policys']
        if 'total' in response:
            self.total = response['total']
