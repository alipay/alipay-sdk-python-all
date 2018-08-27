#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampDetailInfo import CampDetailInfo
from alipay.aop.api.domain.ShopDiscountInfo import ShopDiscountInfo
from alipay.aop.api.domain.ShopDiscountInfo import ShopDiscountInfo


class AlipayOfflineMarketShopDiscountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopDiscountQueryResponse, self).__init__()
        self._camp_list = None
        self._camp_num = None
        self._discount_list = None
        self._item_list = None

    @property
    def camp_list(self):
        return self._camp_list

    @camp_list.setter
    def camp_list(self, value):
        if isinstance(value, list):
            self._camp_list = list()
            for i in value:
                if isinstance(i, CampDetailInfo):
                    self._camp_list.append(i)
                else:
                    self._camp_list.append(CampDetailInfo.from_alipay_dict(i))
    @property
    def camp_num(self):
        return self._camp_num

    @camp_num.setter
    def camp_num(self, value):
        self._camp_num = value
    @property
    def discount_list(self):
        return self._discount_list

    @discount_list.setter
    def discount_list(self, value):
        if isinstance(value, list):
            self._discount_list = list()
            for i in value:
                if isinstance(i, ShopDiscountInfo):
                    self._discount_list.append(i)
                else:
                    self._discount_list.append(ShopDiscountInfo.from_alipay_dict(i))
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ShopDiscountInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ShopDiscountInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopDiscountQueryResponse, self).parse_response_content(response_content)
        if 'camp_list' in response:
            self.camp_list = response['camp_list']
        if 'camp_num' in response:
            self.camp_num = response['camp_num']
        if 'discount_list' in response:
            self.discount_list = response['discount_list']
        if 'item_list' in response:
            self.item_list = response['item_list']
