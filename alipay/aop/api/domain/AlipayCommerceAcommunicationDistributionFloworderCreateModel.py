#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDistributionFloworderCreateModel(object):

    def __init__(self):
        self._inst_order_id = None
        self._item_id = None
        self._mobile = None
        self._pay_type = None
        self._price = None
        self._protocol_sequence_id = None
        self._sms_code = None

    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def protocol_sequence_id(self):
        return self._protocol_sequence_id

    @protocol_sequence_id.setter
    def protocol_sequence_id(self, value):
        self._protocol_sequence_id = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_order_id:
            if hasattr(self.inst_order_id, 'to_alipay_dict'):
                params['inst_order_id'] = self.inst_order_id.to_alipay_dict()
            else:
                params['inst_order_id'] = self.inst_order_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.protocol_sequence_id:
            if hasattr(self.protocol_sequence_id, 'to_alipay_dict'):
                params['protocol_sequence_id'] = self.protocol_sequence_id.to_alipay_dict()
            else:
                params['protocol_sequence_id'] = self.protocol_sequence_id
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionFloworderCreateModel()
        if 'inst_order_id' in d:
            o.inst_order_id = d['inst_order_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'price' in d:
            o.price = d['price']
        if 'protocol_sequence_id' in d:
            o.protocol_sequence_id = d['protocol_sequence_id']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        return o


