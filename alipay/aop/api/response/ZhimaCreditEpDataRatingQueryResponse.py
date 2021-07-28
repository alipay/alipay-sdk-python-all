#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpDataRatingQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDataRatingQueryResponse, self).__init__()
        self._amount = None
        self._biz_code = None
        self._credit_level = None
        self._decision = None
        self._ext_info = None
        self._relation_order_no = None
        self._transaction_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def credit_level(self):
        return self._credit_level

    @credit_level.setter
    def credit_level(self, value):
        self._credit_level = value
    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def relation_order_no(self):
        return self._relation_order_no

    @relation_order_no.setter
    def relation_order_no(self, value):
        self._relation_order_no = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDataRatingQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'credit_level' in response:
            self.credit_level = response['credit_level']
        if 'decision' in response:
            self.decision = response['decision']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'relation_order_no' in response:
            self.relation_order_no = response['relation_order_no']
        if 'transaction_id' in response:
            self.transaction_id = response['transaction_id']
