#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTrafficshareTradeRefundModel(object):

    def __init__(self):
        self._amount_unit = None
        self._biz_scene = None
        self._op_name = None
        self._open_id = None
        self._order_no = None
        self._refund_amount = None
        self._refund_batch_id = None
        self._refund_reason = None
        self._trade_no = None
        self._user_id = None

    @property
    def amount_unit(self):
        return self._amount_unit

    @amount_unit.setter
    def amount_unit(self, value):
        self._amount_unit = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def op_name(self):
        return self._op_name

    @op_name.setter
    def op_name(self, value):
        self._op_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_batch_id(self):
        return self._refund_batch_id

    @refund_batch_id.setter
    def refund_batch_id(self, value):
        self._refund_batch_id = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_unit:
            if hasattr(self.amount_unit, 'to_alipay_dict'):
                params['amount_unit'] = self.amount_unit.to_alipay_dict()
            else:
                params['amount_unit'] = self.amount_unit
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.op_name:
            if hasattr(self.op_name, 'to_alipay_dict'):
                params['op_name'] = self.op_name.to_alipay_dict()
            else:
                params['op_name'] = self.op_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_batch_id:
            if hasattr(self.refund_batch_id, 'to_alipay_dict'):
                params['refund_batch_id'] = self.refund_batch_id.to_alipay_dict()
            else:
                params['refund_batch_id'] = self.refund_batch_id
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTrafficshareTradeRefundModel()
        if 'amount_unit' in d:
            o.amount_unit = d['amount_unit']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'op_name' in d:
            o.op_name = d['op_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_batch_id' in d:
            o.refund_batch_id = d['refund_batch_id']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


