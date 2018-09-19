#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduOneCardDepositCardQueryResult import EduOneCardDepositCardQueryResult


class AlipayEcardEduCardGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcardEduCardGetResponse, self).__init__()
        self._first_deposit_flag = None
        self._onecard = None

    @property
    def first_deposit_flag(self):
        return self._first_deposit_flag

    @first_deposit_flag.setter
    def first_deposit_flag(self, value):
        self._first_deposit_flag = value
    @property
    def onecard(self):
        return self._onecard

    @onecard.setter
    def onecard(self, value):
        if isinstance(value, list):
            self._onecard = list()
            for i in value:
                if isinstance(i, EduOneCardDepositCardQueryResult):
                    self._onecard.append(i)
                else:
                    self._onecard.append(EduOneCardDepositCardQueryResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcardEduCardGetResponse, self).parse_response_content(response_content)
        if 'first_deposit_flag' in response:
            self.first_deposit_flag = response['first_deposit_flag']
        if 'onecard' in response:
            self.onecard = response['onecard']
