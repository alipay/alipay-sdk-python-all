#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountVO import DiscountVO
from alipay.aop.api.domain.ItemsVO import ItemsVO
from alipay.aop.api.domain.MedicareInfoVO import MedicareInfoVO
from alipay.aop.api.domain.OrderInfoVO import OrderInfoVO
from alipay.aop.api.domain.PaymentVO import PaymentVO
from alipay.aop.api.domain.StoreVO import StoreVO
from alipay.aop.api.domain.UserSimpleVO import UserSimpleVO


class AlipayCommerceMedicalOrderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOrderDetailQueryResponse, self).__init__()
        self._discount = None
        self._items = None
        self._medicare = None
        self._order = None
        self._payment = None
        self._store = None
        self._user = None

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, list):
            self._discount = list()
            for i in value:
                if isinstance(i, DiscountVO):
                    self._discount.append(i)
                else:
                    self._discount.append(DiscountVO.from_alipay_dict(i))
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ItemsVO):
                    self._items.append(i)
                else:
                    self._items.append(ItemsVO.from_alipay_dict(i))
    @property
    def medicare(self):
        return self._medicare

    @medicare.setter
    def medicare(self, value):
        if isinstance(value, MedicareInfoVO):
            self._medicare = value
        else:
            self._medicare = MedicareInfoVO.from_alipay_dict(value)
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if isinstance(value, OrderInfoVO):
            self._order = value
        else:
            self._order = OrderInfoVO.from_alipay_dict(value)
    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        if isinstance(value, PaymentVO):
            self._payment = value
        else:
            self._payment = PaymentVO.from_alipay_dict(value)
    @property
    def store(self):
        return self._store

    @store.setter
    def store(self, value):
        if isinstance(value, StoreVO):
            self._store = value
        else:
            self._store = StoreVO.from_alipay_dict(value)
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserSimpleVO):
            self._user = value
        else:
            self._user = UserSimpleVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOrderDetailQueryResponse, self).parse_response_content(response_content)
        if 'discount' in response:
            self.discount = response['discount']
        if 'items' in response:
            self.items = response['items']
        if 'medicare' in response:
            self.medicare = response['medicare']
        if 'order' in response:
            self.order = response['order']
        if 'payment' in response:
            self.payment = response['payment']
        if 'store' in response:
            self.store = response['store']
        if 'user' in response:
            self.user = response['user']
