#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntegratedOpenCheckInfoVO import IntegratedOpenCheckInfoVO


class AlipayOpenSpInteopOrderConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOrderConfirmResponse, self).__init__()
        self._check_result = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        if isinstance(value, list):
            self._check_result = list()
            for i in value:
                if isinstance(i, IntegratedOpenCheckInfoVO):
                    self._check_result.append(i)
                else:
                    self._check_result.append(IntegratedOpenCheckInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOrderConfirmResponse, self).parse_response_content(response_content)
        if 'check_result' in response:
            self.check_result = response['check_result']
