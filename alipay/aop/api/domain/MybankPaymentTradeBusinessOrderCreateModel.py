#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserInfoDetail import UserInfoDetail
from alipay.aop.api.domain.BankGoodsDetail import BankGoodsDetail
from alipay.aop.api.domain.OrderExtendParams import OrderExtendParams
from alipay.aop.api.domain.UserInfoDetail import UserInfoDetail


class MybankPaymentTradeBusinessOrderCreateModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._buyer_info = None
        self._currency_value = None
        self._goods_detail = None
        self._match_account_no = None
        self._order_extend_params = None
        self._out_trade_no = None
        self._product_code = None
        self._remark = None
        self._request_no = None
        self._seller_info = None
        self._timeout_express = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, UserInfoDetail):
            self._buyer_info = value
        else:
            self._buyer_info = UserInfoDetail.from_alipay_dict(value)
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, BankGoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(BankGoodsDetail.from_alipay_dict(i))
    @property
    def match_account_no(self):
        return self._match_account_no

    @match_account_no.setter
    def match_account_no(self, value):
        self._match_account_no = value
    @property
    def order_extend_params(self):
        return self._order_extend_params

    @order_extend_params.setter
    def order_extend_params(self, value):
        if isinstance(value, OrderExtendParams):
            self._order_extend_params = value
        else:
            self._order_extend_params = OrderExtendParams.from_alipay_dict(value)
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def seller_info(self):
        return self._seller_info

    @seller_info.setter
    def seller_info(self, value):
        if isinstance(value, UserInfoDetail):
            self._seller_info = value
        else:
            self._seller_info = UserInfoDetail.from_alipay_dict(value)
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.currency_value:
            if hasattr(self.currency_value, 'to_alipay_dict'):
                params['currency_value'] = self.currency_value.to_alipay_dict()
            else:
                params['currency_value'] = self.currency_value
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
        if self.match_account_no:
            if hasattr(self.match_account_no, 'to_alipay_dict'):
                params['match_account_no'] = self.match_account_no.to_alipay_dict()
            else:
                params['match_account_no'] = self.match_account_no
        if self.order_extend_params:
            if hasattr(self.order_extend_params, 'to_alipay_dict'):
                params['order_extend_params'] = self.order_extend_params.to_alipay_dict()
            else:
                params['order_extend_params'] = self.order_extend_params
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.seller_info:
            if hasattr(self.seller_info, 'to_alipay_dict'):
                params['seller_info'] = self.seller_info.to_alipay_dict()
            else:
                params['seller_info'] = self.seller_info
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeBusinessOrderCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'currency_value' in d:
            o.currency_value = d['currency_value']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'match_account_no' in d:
            o.match_account_no = d['match_account_no']
        if 'order_extend_params' in d:
            o.order_extend_params = d['order_extend_params']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'seller_info' in d:
            o.seller_info = d['seller_info']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


