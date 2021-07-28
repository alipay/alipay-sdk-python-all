#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinExtParams import FinExtParams
from alipay.aop.api.domain.GoodsDetailInfo import GoodsDetailInfo
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.UserIdentityExt import UserIdentityExt
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.UserIdentityExt import UserIdentityExt


class HuanxuTradeOrderPayModel(object):

    def __init__(self):
        self._channel = None
        self._ext_params = None
        self._goods_infos = None
        self._is_async_pay = None
        self._merchant_order_no = None
        self._order_amount = None
        self._pay_amount = None
        self._pay_entity_mode = None
        self._pay_mode = None
        self._pay_request_no = None
        self._pay_terminal = None
        self._payee = None
        self._payee_ext = None
        self._payer = None
        self._payer_ext = None
        self._remark = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, FinExtParams):
            self._ext_params = value
        else:
            self._ext_params = FinExtParams.from_alipay_dict(value)
    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, GoodsDetailInfo):
            self._goods_infos = value
        else:
            self._goods_infos = GoodsDetailInfo.from_alipay_dict(value)
    @property
    def is_async_pay(self):
        return self._is_async_pay

    @is_async_pay.setter
    def is_async_pay(self, value):
        self._is_async_pay = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_entity_mode(self):
        return self._pay_entity_mode

    @pay_entity_mode.setter
    def pay_entity_mode(self, value):
        self._pay_entity_mode = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def pay_request_no(self):
        return self._pay_request_no

    @pay_request_no.setter
    def pay_request_no(self, value):
        self._pay_request_no = value
    @property
    def pay_terminal(self):
        return self._pay_terminal

    @pay_terminal.setter
    def pay_terminal(self, value):
        self._pay_terminal = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        if isinstance(value, UserIdentity):
            self._payee = value
        else:
            self._payee = UserIdentity.from_alipay_dict(value)
    @property
    def payee_ext(self):
        return self._payee_ext

    @payee_ext.setter
    def payee_ext(self, value):
        if isinstance(value, UserIdentityExt):
            self._payee_ext = value
        else:
            self._payee_ext = UserIdentityExt.from_alipay_dict(value)
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        if isinstance(value, UserIdentity):
            self._payer = value
        else:
            self._payer = UserIdentity.from_alipay_dict(value)
    @property
    def payer_ext(self):
        return self._payer_ext

    @payer_ext.setter
    def payer_ext(self, value):
        if isinstance(value, UserIdentityExt):
            self._payer_ext = value
        else:
            self._payer_ext = UserIdentityExt.from_alipay_dict(value)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.goods_infos:
            if hasattr(self.goods_infos, 'to_alipay_dict'):
                params['goods_infos'] = self.goods_infos.to_alipay_dict()
            else:
                params['goods_infos'] = self.goods_infos
        if self.is_async_pay:
            if hasattr(self.is_async_pay, 'to_alipay_dict'):
                params['is_async_pay'] = self.is_async_pay.to_alipay_dict()
            else:
                params['is_async_pay'] = self.is_async_pay
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_entity_mode:
            if hasattr(self.pay_entity_mode, 'to_alipay_dict'):
                params['pay_entity_mode'] = self.pay_entity_mode.to_alipay_dict()
            else:
                params['pay_entity_mode'] = self.pay_entity_mode
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.pay_request_no:
            if hasattr(self.pay_request_no, 'to_alipay_dict'):
                params['pay_request_no'] = self.pay_request_no.to_alipay_dict()
            else:
                params['pay_request_no'] = self.pay_request_no
        if self.pay_terminal:
            if hasattr(self.pay_terminal, 'to_alipay_dict'):
                params['pay_terminal'] = self.pay_terminal.to_alipay_dict()
            else:
                params['pay_terminal'] = self.pay_terminal
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.payee_ext:
            if hasattr(self.payee_ext, 'to_alipay_dict'):
                params['payee_ext'] = self.payee_ext.to_alipay_dict()
            else:
                params['payee_ext'] = self.payee_ext
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        if self.payer_ext:
            if hasattr(self.payer_ext, 'to_alipay_dict'):
                params['payer_ext'] = self.payer_ext.to_alipay_dict()
            else:
                params['payer_ext'] = self.payer_ext
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HuanxuTradeOrderPayModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'is_async_pay' in d:
            o.is_async_pay = d['is_async_pay']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_entity_mode' in d:
            o.pay_entity_mode = d['pay_entity_mode']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'pay_request_no' in d:
            o.pay_request_no = d['pay_request_no']
        if 'pay_terminal' in d:
            o.pay_terminal = d['pay_terminal']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_ext' in d:
            o.payee_ext = d['payee_ext']
        if 'payer' in d:
            o.payer = d['payer']
        if 'payer_ext' in d:
            o.payer_ext = d['payer_ext']
        if 'remark' in d:
            o.remark = d['remark']
        return o


