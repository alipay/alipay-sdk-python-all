#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleSimpleInfoVO(object):

    def __init__(self):
        self._action_type = None
        self._aftersale_id = None
        self._aftersale_reason = None
        self._apply_refund_amount = None
        self._create_time = None
        self._order_id = None
        self._out_aftersale_id = None
        self._status = None
        self._type = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def aftersale_reason(self):
        return self._aftersale_reason

    @aftersale_reason.setter
    def aftersale_reason(self, value):
        self._aftersale_reason = value
    @property
    def apply_refund_amount(self):
        return self._apply_refund_amount

    @apply_refund_amount.setter
    def apply_refund_amount(self, value):
        self._apply_refund_amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.aftersale_reason:
            if hasattr(self.aftersale_reason, 'to_alipay_dict'):
                params['aftersale_reason'] = self.aftersale_reason.to_alipay_dict()
            else:
                params['aftersale_reason'] = self.aftersale_reason
        if self.apply_refund_amount:
            if hasattr(self.apply_refund_amount, 'to_alipay_dict'):
                params['apply_refund_amount'] = self.apply_refund_amount.to_alipay_dict()
            else:
                params['apply_refund_amount'] = self.apply_refund_amount
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_aftersale_id:
            if hasattr(self.out_aftersale_id, 'to_alipay_dict'):
                params['out_aftersale_id'] = self.out_aftersale_id.to_alipay_dict()
            else:
                params['out_aftersale_id'] = self.out_aftersale_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleSimpleInfoVO()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'aftersale_reason' in d:
            o.aftersale_reason = d['aftersale_reason']
        if 'apply_refund_amount' in d:
            o.apply_refund_amount = d['apply_refund_amount']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_aftersale_id' in d:
            o.out_aftersale_id = d['out_aftersale_id']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


