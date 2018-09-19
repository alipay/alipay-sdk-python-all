#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbAdvertDealBillResponse import KbAdvertDealBillResponse
from alipay.aop.api.domain.KbAdvertSettleBillResponse import KbAdvertSettleBillResponse


class KoubeiAdvertCommissionBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionBillQueryResponse, self).__init__()
        self._date = None
        self._deal_bill = None
        self._settle_bill = None
        self._type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def deal_bill(self):
        return self._deal_bill

    @deal_bill.setter
    def deal_bill(self, value):
        if isinstance(value, KbAdvertDealBillResponse):
            self._deal_bill = value
        else:
            self._deal_bill = KbAdvertDealBillResponse.from_alipay_dict(value)
    @property
    def settle_bill(self):
        return self._settle_bill

    @settle_bill.setter
    def settle_bill(self, value):
        if isinstance(value, KbAdvertSettleBillResponse):
            self._settle_bill = value
        else:
            self._settle_bill = KbAdvertSettleBillResponse.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionBillQueryResponse, self).parse_response_content(response_content)
        if 'date' in response:
            self.date = response['date']
        if 'deal_bill' in response:
            self.deal_bill = response['deal_bill']
        if 'settle_bill' in response:
            self.settle_bill = response['settle_bill']
        if 'type' in response:
            self.type = response['type']
