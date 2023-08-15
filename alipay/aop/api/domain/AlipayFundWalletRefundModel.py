#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundBusinessExtend import RefundBusinessExtend


class AlipayFundWalletRefundModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._original_deposit_order_id = None
        self._out_biz_no = None
        self._principal_id = None
        self._principal_open_id = None
        self._principal_type = None
        self._product_code = None
        self._refund_business_extend = None
        self._refund_strategy = None
        self._user_wallet_id = None

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
    def original_deposit_order_id(self):
        return self._original_deposit_order_id

    @original_deposit_order_id.setter
    def original_deposit_order_id(self, value):
        self._original_deposit_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def refund_business_extend(self):
        return self._refund_business_extend

    @refund_business_extend.setter
    def refund_business_extend(self, value):
        if isinstance(value, RefundBusinessExtend):
            self._refund_business_extend = value
        else:
            self._refund_business_extend = RefundBusinessExtend.from_alipay_dict(value)
    @property
    def refund_strategy(self):
        return self._refund_strategy

    @refund_strategy.setter
    def refund_strategy(self, value):
        self._refund_strategy = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


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
        if self.original_deposit_order_id:
            if hasattr(self.original_deposit_order_id, 'to_alipay_dict'):
                params['original_deposit_order_id'] = self.original_deposit_order_id.to_alipay_dict()
            else:
                params['original_deposit_order_id'] = self.original_deposit_order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_open_id:
            if hasattr(self.principal_open_id, 'to_alipay_dict'):
                params['principal_open_id'] = self.principal_open_id.to_alipay_dict()
            else:
                params['principal_open_id'] = self.principal_open_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.refund_business_extend:
            if hasattr(self.refund_business_extend, 'to_alipay_dict'):
                params['refund_business_extend'] = self.refund_business_extend.to_alipay_dict()
            else:
                params['refund_business_extend'] = self.refund_business_extend
        if self.refund_strategy:
            if hasattr(self.refund_strategy, 'to_alipay_dict'):
                params['refund_strategy'] = self.refund_strategy.to_alipay_dict()
            else:
                params['refund_strategy'] = self.refund_strategy
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletRefundModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'original_deposit_order_id' in d:
            o.original_deposit_order_id = d['original_deposit_order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_open_id' in d:
            o.principal_open_id = d['principal_open_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'refund_business_extend' in d:
            o.refund_business_extend = d['refund_business_extend']
        if 'refund_strategy' in d:
            o.refund_strategy = d['refund_strategy']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


