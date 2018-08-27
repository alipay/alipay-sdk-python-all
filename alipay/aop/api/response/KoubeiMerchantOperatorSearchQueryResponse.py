#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorBaseInfo import OperatorBaseInfo


class KoubeiMerchantOperatorSearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorSearchQueryResponse, self).__init__()
        self._operator_list = None
        self._total = None

    @property
    def operator_list(self):
        return self._operator_list

    @operator_list.setter
    def operator_list(self, value):
        if isinstance(value, list):
            self._operator_list = list()
            for i in value:
                if isinstance(i, OperatorBaseInfo):
                    self._operator_list.append(i)
                else:
                    self._operator_list.append(OperatorBaseInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorSearchQueryResponse, self).parse_response_content(response_content)
        if 'operator_list' in response:
            self.operator_list = response['operator_list']
        if 'total' in response:
            self.total = response['total']
