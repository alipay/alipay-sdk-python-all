#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCardExchangeApplyModel(object):

    def __init__(self):
        self._apply_sum = None
        self._apply_time = None
        self._benefit_id = None
        self._biz_no = None
        self._cooperate_mode = None
        self._open_id = None
        self._phone = None
        self._user_id = None

    @property
    def apply_sum(self):
        return self._apply_sum

    @apply_sum.setter
    def apply_sum(self, value):
        self._apply_sum = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def cooperate_mode(self):
        return self._cooperate_mode

    @cooperate_mode.setter
    def cooperate_mode(self, value):
        self._cooperate_mode = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_sum:
            if hasattr(self.apply_sum, 'to_alipay_dict'):
                params['apply_sum'] = self.apply_sum.to_alipay_dict()
            else:
                params['apply_sum'] = self.apply_sum
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.cooperate_mode:
            if hasattr(self.cooperate_mode, 'to_alipay_dict'):
                params['cooperate_mode'] = self.cooperate_mode.to_alipay_dict()
            else:
                params['cooperate_mode'] = self.cooperate_mode
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
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
        o = AlipayCommerceMedicalCardExchangeApplyModel()
        if 'apply_sum' in d:
            o.apply_sum = d['apply_sum']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'cooperate_mode' in d:
            o.cooperate_mode = d['cooperate_mode']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


