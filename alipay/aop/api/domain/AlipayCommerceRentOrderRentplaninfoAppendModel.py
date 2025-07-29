#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentInstallmentInfo import RentInstallmentInfo


class AlipayCommerceRentOrderRentplaninfoAppendModel(object):

    def __init__(self):
        self._installments = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._rent_end_time = None
        self._user_id = None

    @property
    def installments(self):
        return self._installments

    @installments.setter
    def installments(self, value):
        if isinstance(value, list):
            self._installments = list()
            for i in value:
                if isinstance(i, RentInstallmentInfo):
                    self._installments.append(i)
                else:
                    self._installments.append(RentInstallmentInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.installments:
            if isinstance(self.installments, list):
                for i in range(0, len(self.installments)):
                    element = self.installments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installments[i] = element.to_alipay_dict()
            if hasattr(self.installments, 'to_alipay_dict'):
                params['installments'] = self.installments.to_alipay_dict()
            else:
                params['installments'] = self.installments
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderRentplaninfoAppendModel()
        if 'installments' in d:
            o.installments = d['installments']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


