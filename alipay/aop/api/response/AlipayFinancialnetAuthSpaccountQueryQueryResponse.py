#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpAccountInfoVo import SpAccountInfoVo


class AlipayFinancialnetAuthSpaccountQueryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthSpaccountQueryQueryResponse, self).__init__()
        self._account_info = None

    @property
    def account_info(self):
        return self._account_info

    @account_info.setter
    def account_info(self, value):
        if isinstance(value, list):
            self._account_info = list()
            for i in value:
                if isinstance(i, SpAccountInfoVo):
                    self._account_info.append(i)
                else:
                    self._account_info.append(SpAccountInfoVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthSpaccountQueryQueryResponse, self).parse_response_content(response_content)
        if 'account_info' in response:
            self.account_info = response['account_info']
