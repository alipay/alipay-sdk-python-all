#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPayInfoDTO import RentPayInfoDTO


class AlipayCommerceRentOrderInfoSyncModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._installment_no = None
        self._order_id = None
        self._pay_channel = None
        self._rent_pay_info = None
        self._trade_no = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def rent_pay_info(self):
        return self._rent_pay_info

    @rent_pay_info.setter
    def rent_pay_info(self, value):
        if isinstance(value, list):
            self._rent_pay_info = list()
            for i in value:
                if isinstance(i, RentPayInfoDTO):
                    self._rent_pay_info.append(i)
                else:
                    self._rent_pay_info.append(RentPayInfoDTO.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.rent_pay_info:
            if isinstance(self.rent_pay_info, list):
                for i in range(0, len(self.rent_pay_info)):
                    element = self.rent_pay_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_pay_info[i] = element.to_alipay_dict()
            if hasattr(self.rent_pay_info, 'to_alipay_dict'):
                params['rent_pay_info'] = self.rent_pay_info.to_alipay_dict()
            else:
                params['rent_pay_info'] = self.rent_pay_info
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderInfoSyncModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'rent_pay_info' in d:
            o.rent_pay_info = d['rent_pay_info']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


