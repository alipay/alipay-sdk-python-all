#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountDetail import DiscountDetail
from alipay.aop.api.domain.MCardDetail import MCardDetail


class KoubeiCateringOrderPayConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderPayConsultResponse, self).__init__()
        self._discount_details = None
        self._m_card_detail = None
        self._pay_amount = None
        self._request_id = None
        self._total_amount = None

    @property
    def discount_details(self):
        return self._discount_details

    @discount_details.setter
    def discount_details(self, value):
        if isinstance(value, list):
            self._discount_details = list()
            for i in value:
                if isinstance(i, DiscountDetail):
                    self._discount_details.append(i)
                else:
                    self._discount_details.append(DiscountDetail.from_alipay_dict(i))
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
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderPayConsultResponse, self).parse_response_content(response_content)
        if 'discount_details' in response:
            self.discount_details = response['discount_details']
        if 'm_card_detail' in response:
            self.m_card_detail = response['m_card_detail']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
