#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardAmountDetailVO import CardAmountDetailVO


class AlipayTradeAccountFundcompositionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeAccountFundcompositionQueryResponse, self).__init__()
        self._account_no = None
        self._card_amount_detail_list = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def card_amount_detail_list(self):
        return self._card_amount_detail_list

    @card_amount_detail_list.setter
    def card_amount_detail_list(self, value):
        if isinstance(value, list):
            self._card_amount_detail_list = list()
            for i in value:
                if isinstance(i, CardAmountDetailVO):
                    self._card_amount_detail_list.append(i)
                else:
                    self._card_amount_detail_list.append(CardAmountDetailVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeAccountFundcompositionQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'card_amount_detail_list' in response:
            self.card_amount_detail_list = response['card_amount_detail_list']
