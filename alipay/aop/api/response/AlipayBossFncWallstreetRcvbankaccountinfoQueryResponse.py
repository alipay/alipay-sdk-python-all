#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BankAccountInfoDto import BankAccountInfoDto


class AlipayBossFncWallstreetRcvbankaccountinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncWallstreetRcvbankaccountinfoQueryResponse, self).__init__()
        self._result_set = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, list):
            self._result_set = list()
            for i in value:
                if isinstance(i, BankAccountInfoDto):
                    self._result_set.append(i)
                else:
                    self._result_set.append(BankAccountInfoDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncWallstreetRcvbankaccountinfoQueryResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
