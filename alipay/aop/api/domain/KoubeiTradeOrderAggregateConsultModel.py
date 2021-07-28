#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbGoodsInfo import KbGoodsInfo


class KoubeiTradeOrderAggregateConsultModel(object):

    def __init__(self):
        self._goods_info = None
        self._out_order_no = None
        self._shop_id = None
        self._subject = None
        self._timeout_express = None
        self._total_amount = None
        self._un_discount_amount = None

    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, KbGoodsInfo):
            self._goods_info = value
        else:
            self._goods_info = KbGoodsInfo.from_alipay_dict(value)
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def un_discount_amount(self):
        return self._un_discount_amount

    @un_discount_amount.setter
    def un_discount_amount(self, value):
        self._un_discount_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.un_discount_amount:
            if hasattr(self.un_discount_amount, 'to_alipay_dict'):
                params['un_discount_amount'] = self.un_discount_amount.to_alipay_dict()
            else:
                params['un_discount_amount'] = self.un_discount_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeOrderAggregateConsultModel()
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'un_discount_amount' in d:
            o.un_discount_amount = d['un_discount_amount']
        return o


