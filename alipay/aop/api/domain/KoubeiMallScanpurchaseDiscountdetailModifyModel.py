#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallDiscountDetail import MallDiscountDetail


class KoubeiMallScanpurchaseDiscountdetailModifyModel(object):

    def __init__(self):
        self._buyer_user_id = None
        self._discount_details = None
        self._order_id = None
        self._trade_no = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def discount_details(self):
        return self._discount_details

    @discount_details.setter
    def discount_details(self, value):
        if isinstance(value, list):
            self._discount_details = list()
            for i in value:
                if isinstance(i, MallDiscountDetail):
                    self._discount_details.append(i)
                else:
                    self._discount_details.append(MallDiscountDetail.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.discount_details:
            if isinstance(self.discount_details, list):
                for i in range(0, len(self.discount_details)):
                    element = self.discount_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_details[i] = element.to_alipay_dict()
            if hasattr(self.discount_details, 'to_alipay_dict'):
                params['discount_details'] = self.discount_details.to_alipay_dict()
            else:
                params['discount_details'] = self.discount_details
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = KoubeiMallScanpurchaseDiscountdetailModifyModel()
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'discount_details' in d:
            o.discount_details = d['discount_details']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


