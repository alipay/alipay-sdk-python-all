#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizCard import BizCard
from alipay.aop.api.domain.BizGrantPlan import BizGrantPlan
from alipay.aop.api.domain.BizVoucher import BizVoucher


class AlipayCommerceTransportIndustryCarddetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryCarddetailQueryResponse, self).__init__()
        self._card = None
        self._grant_plan_list = None
        self._voucher_list = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value):
        if isinstance(value, BizCard):
            self._card = value
        else:
            self._card = BizCard.from_alipay_dict(value)
    @property
    def grant_plan_list(self):
        return self._grant_plan_list

    @grant_plan_list.setter
    def grant_plan_list(self, value):
        if isinstance(value, list):
            self._grant_plan_list = list()
            for i in value:
                if isinstance(i, BizGrantPlan):
                    self._grant_plan_list.append(i)
                else:
                    self._grant_plan_list.append(BizGrantPlan.from_alipay_dict(i))
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, BizVoucher):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(BizVoucher.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryCarddetailQueryResponse, self).parse_response_content(response_content)
        if 'card' in response:
            self.card = response['card']
        if 'grant_plan_list' in response:
            self.grant_plan_list = response['grant_plan_list']
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
