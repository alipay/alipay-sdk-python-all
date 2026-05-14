#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResalePayInfoVO(object):

    def __init__(self):
        self._pay_amount = None
        self._pay_memo = None
        self._pay_scene = None

    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_memo(self):
        return self._pay_memo

    @pay_memo.setter
    def pay_memo(self, value):
        self._pay_memo = value
    @property
    def pay_scene(self):
        return self._pay_scene

    @pay_scene.setter
    def pay_scene(self, value):
        self._pay_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_memo:
            if hasattr(self.pay_memo, 'to_alipay_dict'):
                params['pay_memo'] = self.pay_memo.to_alipay_dict()
            else:
                params['pay_memo'] = self.pay_memo
        if self.pay_scene:
            if hasattr(self.pay_scene, 'to_alipay_dict'):
                params['pay_scene'] = self.pay_scene.to_alipay_dict()
            else:
                params['pay_scene'] = self.pay_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResalePayInfoVO()
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_memo' in d:
            o.pay_memo = d['pay_memo']
        if 'pay_scene' in d:
            o.pay_scene = d['pay_scene']
        return o


