#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserCreditCard import AlipayUserCreditCard


class AlipayUserFinanceinfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFinanceinfoShareResponse, self).__init__()
        self._credit_card_list = None

    @property
    def credit_card_list(self):
        return self._credit_card_list

    @credit_card_list.setter
    def credit_card_list(self, value):
        if isinstance(value, list):
            self._credit_card_list = list()
            for i in value:
                if isinstance(i, AlipayUserCreditCard):
                    self._credit_card_list.append(i)
                else:
                    self._credit_card_list.append(AlipayUserCreditCard.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserFinanceinfoShareResponse, self).parse_response_content(response_content)
        if 'credit_card_list' in response:
            self.credit_card_list = response['credit_card_list']
