#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskBizDomain import RiskBizDomain


class AlipayBossBaseFrastressQuerybusinessdomainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseFrastressQuerybusinessdomainQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, RiskBizDomain):
                    self._result.append(i)
                else:
                    self._result.append(RiskBizDomain.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseFrastressQuerybusinessdomainQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
