#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallDiscountDetail import MallDiscountDetail
from alipay.aop.api.domain.MallGoodsDetail import MallGoodsDetail


class KoubeiMallScanpurchaseTradePayModel(object):

    def __init__(self):
        self._advance_order_id = None
        self._buyer_user_id = None
        self._discount_details = None
        self._discountable_amount = None
        self._goods_detail = None
        self._out_trade_no = None
        self._total_amount = None
        self._undiscountable_amount = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value
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
    def discountable_amount(self):
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, value):
        self._discountable_amount = value
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, MallGoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(MallGoodsDetail.from_alipay_dict(i))
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_order_id:
            if hasattr(self.advance_order_id, 'to_alipay_dict'):
                params['advance_order_id'] = self.advance_order_id.to_alipay_dict()
            else:
                params['advance_order_id'] = self.advance_order_id
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
        if self.discountable_amount:
            if hasattr(self.discountable_amount, 'to_alipay_dict'):
                params['discountable_amount'] = self.discountable_amount.to_alipay_dict()
            else:
                params['discountable_amount'] = self.discountable_amount
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMallScanpurchaseTradePayModel()
        if 'advance_order_id' in d:
            o.advance_order_id = d['advance_order_id']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'discount_details' in d:
            o.discount_details = d['discount_details']
        if 'discountable_amount' in d:
            o.discountable_amount = d['discountable_amount']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        return o


