#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcAddressInfo import MpcAddressInfo
from alipay.aop.api.domain.SingleOrderVO import SingleOrderVO
from alipay.aop.api.domain.SingleOrderVO import SingleOrderVO


class AlipayCloudCloudpromoMallPurchaseConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallPurchaseConsultResponse, self).__init__()
        self._address_list = None
        self._can_sell = None
        self._message = None
        self._order_list = None
        self._unsellable_order_list = None

    @property
    def address_list(self):
        return self._address_list

    @address_list.setter
    def address_list(self, value):
        if isinstance(value, MpcAddressInfo):
            self._address_list = value
        else:
            self._address_list = MpcAddressInfo.from_alipay_dict(value)
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, SingleOrderVO):
                    self._order_list.append(i)
                else:
                    self._order_list.append(SingleOrderVO.from_alipay_dict(i))
    @property
    def unsellable_order_list(self):
        return self._unsellable_order_list

    @unsellable_order_list.setter
    def unsellable_order_list(self, value):
        if isinstance(value, SingleOrderVO):
            self._unsellable_order_list = value
        else:
            self._unsellable_order_list = SingleOrderVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallPurchaseConsultResponse, self).parse_response_content(response_content)
        if 'address_list' in response:
            self.address_list = response['address_list']
        if 'can_sell' in response:
            self.can_sell = response['can_sell']
        if 'message' in response:
            self.message = response['message']
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'unsellable_order_list' in response:
            self.unsellable_order_list = response['unsellable_order_list']
