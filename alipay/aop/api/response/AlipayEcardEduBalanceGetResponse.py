#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduOneCardBalanceQueryResult import EduOneCardBalanceQueryResult


class AlipayEcardEduBalanceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcardEduBalanceGetResponse, self).__init__()
        self._balance = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, list):
            self._balance = list()
            for i in value:
                if isinstance(i, EduOneCardBalanceQueryResult):
                    self._balance.append(i)
                else:
                    self._balance.append(EduOneCardBalanceQueryResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcardEduBalanceGetResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
