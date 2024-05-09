#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtendStrategy import ExtendStrategy
from alipay.aop.api.domain.WalletMarketingRule import WalletMarketingRule
from alipay.aop.api.domain.WithdrawExtend import WithdrawExtend


class AlipayFundWalletWithdrawModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._extend_strategy = None
        self._order_title = None
        self._out_biz_no = None
        self._product_code = None
        self._user_wallet_id = None
        self._wallet_marketing_rule = None
        self._withdraw_extend = None

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
    def extend_strategy(self):
        return self._extend_strategy

    @extend_strategy.setter
    def extend_strategy(self, value):
        if isinstance(value, ExtendStrategy):
            self._extend_strategy = value
        else:
            self._extend_strategy = ExtendStrategy.from_alipay_dict(value)
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value
    @property
    def wallet_marketing_rule(self):
        return self._wallet_marketing_rule

    @wallet_marketing_rule.setter
    def wallet_marketing_rule(self, value):
        if isinstance(value, WalletMarketingRule):
            self._wallet_marketing_rule = value
        else:
            self._wallet_marketing_rule = WalletMarketingRule.from_alipay_dict(value)
    @property
    def withdraw_extend(self):
        return self._withdraw_extend

    @withdraw_extend.setter
    def withdraw_extend(self, value):
        if isinstance(value, WithdrawExtend):
            self._withdraw_extend = value
        else:
            self._withdraw_extend = WithdrawExtend.from_alipay_dict(value)


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
        if self.extend_strategy:
            if hasattr(self.extend_strategy, 'to_alipay_dict'):
                params['extend_strategy'] = self.extend_strategy.to_alipay_dict()
            else:
                params['extend_strategy'] = self.extend_strategy
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        if self.wallet_marketing_rule:
            if hasattr(self.wallet_marketing_rule, 'to_alipay_dict'):
                params['wallet_marketing_rule'] = self.wallet_marketing_rule.to_alipay_dict()
            else:
                params['wallet_marketing_rule'] = self.wallet_marketing_rule
        if self.withdraw_extend:
            if hasattr(self.withdraw_extend, 'to_alipay_dict'):
                params['withdraw_extend'] = self.withdraw_extend.to_alipay_dict()
            else:
                params['withdraw_extend'] = self.withdraw_extend
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletWithdrawModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'extend_strategy' in d:
            o.extend_strategy = d['extend_strategy']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        if 'wallet_marketing_rule' in d:
            o.wallet_marketing_rule = d['wallet_marketing_rule']
        if 'withdraw_extend' in d:
            o.withdraw_extend = d['withdraw_extend']
        return o


