#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountDetail import DiscountDetail
from alipay.aop.api.domain.MCardDetail import MCardDetail


class KoubeiTradeOrderConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderConsultResponse, self).__init__()
        self._buyer_pay_amount = None
        self._discount_detail = None
        self._m_card_detail = None
        self._request_id = None

    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def discount_detail(self):
        return self._discount_detail

    @discount_detail.setter
    def discount_detail(self, value):
        if isinstance(value, list):
            self._discount_detail = list()
            for i in value:
                if isinstance(i, DiscountDetail):
                    self._discount_detail.append(i)
                else:
                    self._discount_detail.append(DiscountDetail.from_alipay_dict(i))
    @property
    def m_card_detail(self):
        return self._m_card_detail

    @m_card_detail.setter
    def m_card_detail(self, value):
        if isinstance(value, MCardDetail):
            self._m_card_detail = value
        else:
            self._m_card_detail = MCardDetail.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderConsultResponse, self).parse_response_content(response_content)
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'discount_detail' in response:
            self.discount_detail = response['discount_detail']
        if 'm_card_detail' in response:
            self.m_card_detail = response['m_card_detail']
        if 'request_id' in response:
            self.request_id = response['request_id']
