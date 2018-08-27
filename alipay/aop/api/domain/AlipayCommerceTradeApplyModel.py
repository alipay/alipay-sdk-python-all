#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeApplyParams import TradeApplyParams


class AlipayCommerceTradeApplyModel(object):

    def __init__(self):
        self._amount_detail = None
        self._channel = None
        self._interface_version = None
        self._op_code = None
        self._order_detail = None
        self._scene_code = None
        self._target_id = None
        self._target_id_type = None
        self._trade_apply_params = None

    @property
    def amount_detail(self):
        return self._amount_detail

    @amount_detail.setter
    def amount_detail(self, value):
        self._amount_detail = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def interface_version(self):
        return self._interface_version

    @interface_version.setter
    def interface_version(self, value):
        self._interface_version = value
    @property
    def op_code(self):
        return self._op_code

    @op_code.setter
    def op_code(self, value):
        self._op_code = value
    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        self._order_detail = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_id_type(self):
        return self._target_id_type

    @target_id_type.setter
    def target_id_type(self, value):
        self._target_id_type = value
    @property
    def trade_apply_params(self):
        return self._trade_apply_params

    @trade_apply_params.setter
    def trade_apply_params(self, value):
        if isinstance(value, TradeApplyParams):
            self._trade_apply_params = value
        else:
            self._trade_apply_params = TradeApplyParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount_detail:
            if hasattr(self.amount_detail, 'to_alipay_dict'):
                params['amount_detail'] = self.amount_detail.to_alipay_dict()
            else:
                params['amount_detail'] = self.amount_detail
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.interface_version:
            if hasattr(self.interface_version, 'to_alipay_dict'):
                params['interface_version'] = self.interface_version.to_alipay_dict()
            else:
                params['interface_version'] = self.interface_version
        if self.op_code:
            if hasattr(self.op_code, 'to_alipay_dict'):
                params['op_code'] = self.op_code.to_alipay_dict()
            else:
                params['op_code'] = self.op_code
        if self.order_detail:
            if hasattr(self.order_detail, 'to_alipay_dict'):
                params['order_detail'] = self.order_detail.to_alipay_dict()
            else:
                params['order_detail'] = self.order_detail
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_id_type:
            if hasattr(self.target_id_type, 'to_alipay_dict'):
                params['target_id_type'] = self.target_id_type.to_alipay_dict()
            else:
                params['target_id_type'] = self.target_id_type
        if self.trade_apply_params:
            if hasattr(self.trade_apply_params, 'to_alipay_dict'):
                params['trade_apply_params'] = self.trade_apply_params.to_alipay_dict()
            else:
                params['trade_apply_params'] = self.trade_apply_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTradeApplyModel()
        if 'amount_detail' in d:
            o.amount_detail = d['amount_detail']
        if 'channel' in d:
            o.channel = d['channel']
        if 'interface_version' in d:
            o.interface_version = d['interface_version']
        if 'op_code' in d:
            o.op_code = d['op_code']
        if 'order_detail' in d:
            o.order_detail = d['order_detail']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_id_type' in d:
            o.target_id_type = d['target_id_type']
        if 'trade_apply_params' in d:
            o.trade_apply_params = d['trade_apply_params']
        return o


