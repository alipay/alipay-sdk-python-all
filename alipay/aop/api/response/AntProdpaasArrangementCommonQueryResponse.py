#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArrangementVORes import ArrangementVORes


class AntProdpaasArrangementCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasArrangementCommonQueryResponse, self).__init__()
        self._arrangements = None

    @property
    def arrangements(self):
        return self._arrangements

    @arrangements.setter
    def arrangements(self, value):
        if isinstance(value, list):
            self._arrangements = list()
            for i in value:
                if isinstance(i, ArrangementVORes):
                    self._arrangements.append(i)
                else:
                    self._arrangements.append(ArrangementVORes.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntProdpaasArrangementCommonQueryResponse, self).parse_response_content(response_content)
        if 'arrangements' in response:
            self.arrangements = response['arrangements']
