#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerGrowthOrderNotifyModel(object):

    def __init__(self):
        self._behavior_id = None
        self._biz_time = None
        self._havana_user_id = None
        self._out_biz_no = None
        self._pay_amount = None
        self._scene_code = None

    @property
    def behavior_id(self):
        return self._behavior_id

    @behavior_id.setter
    def behavior_id(self, value):
        self._behavior_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def havana_user_id(self):
        return self._havana_user_id

    @havana_user_id.setter
    def havana_user_id(self, value):
        self._havana_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior_id:
            if hasattr(self.behavior_id, 'to_alipay_dict'):
                params['behavior_id'] = self.behavior_id.to_alipay_dict()
            else:
                params['behavior_id'] = self.behavior_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.havana_user_id:
            if hasattr(self.havana_user_id, 'to_alipay_dict'):
                params['havana_user_id'] = self.havana_user_id.to_alipay_dict()
            else:
                params['havana_user_id'] = self.havana_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerGrowthOrderNotifyModel()
        if 'behavior_id' in d:
            o.behavior_id = d['behavior_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'havana_user_id' in d:
            o.havana_user_id = d['havana_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


