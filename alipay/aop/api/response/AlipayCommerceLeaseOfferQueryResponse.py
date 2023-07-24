#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeasePlanOfferDTO import LeasePlanOfferDTO


class AlipayCommerceLeaseOfferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLeaseOfferQueryResponse, self).__init__()
        self._item_id = None
        self._plan_offer_list = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def plan_offer_list(self):
        return self._plan_offer_list

    @plan_offer_list.setter
    def plan_offer_list(self, value):
        if isinstance(value, list):
            self._plan_offer_list = list()
            for i in value:
                if isinstance(i, LeasePlanOfferDTO):
                    self._plan_offer_list.append(i)
                else:
                    self._plan_offer_list.append(LeasePlanOfferDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLeaseOfferQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'plan_offer_list' in response:
            self.plan_offer_list = response['plan_offer_list']
