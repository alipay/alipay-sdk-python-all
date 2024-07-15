#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductVO import ProductVO


class AlipayCloudCloudpromoMallPurchaseCreateModel(object):

    def __init__(self):
        self._address_detail = None
        self._address_id = None
        self._buyer = None
        self._outer_purchase_id = None
        self._product_list = None
        self._receiver = None
        self._receiver_phone = None

    @property
    def address_detail(self):
        return self._address_detail

    @address_detail.setter
    def address_detail(self, value):
        self._address_detail = value
    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        self._buyer = value
    @property
    def outer_purchase_id(self):
        return self._outer_purchase_id

    @outer_purchase_id.setter
    def outer_purchase_id(self, value):
        self._outer_purchase_id = value
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, ProductVO):
                    self._product_list.append(i)
                else:
                    self._product_list.append(ProductVO.from_alipay_dict(i))
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_detail:
            if hasattr(self.address_detail, 'to_alipay_dict'):
                params['address_detail'] = self.address_detail.to_alipay_dict()
            else:
                params['address_detail'] = self.address_detail
        if self.address_id:
            if hasattr(self.address_id, 'to_alipay_dict'):
                params['address_id'] = self.address_id.to_alipay_dict()
            else:
                params['address_id'] = self.address_id
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.outer_purchase_id:
            if hasattr(self.outer_purchase_id, 'to_alipay_dict'):
                params['outer_purchase_id'] = self.outer_purchase_id.to_alipay_dict()
            else:
                params['outer_purchase_id'] = self.outer_purchase_id
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallPurchaseCreateModel()
        if 'address_detail' in d:
            o.address_detail = d['address_detail']
        if 'address_id' in d:
            o.address_id = d['address_id']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'outer_purchase_id' in d:
            o.outer_purchase_id = d['outer_purchase_id']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        return o


