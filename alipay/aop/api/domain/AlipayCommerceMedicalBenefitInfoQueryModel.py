#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalBenefitInfoQueryModel(object):

    def __init__(self):
        self._benefit_id = None
        self._biz_id = None
        self._open_id = None
        self._out_benefit_id = None
        self._user_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_benefit_id(self):
        return self._out_benefit_id

    @out_benefit_id.setter
    def out_benefit_id(self, value):
        self._out_benefit_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_benefit_id:
            if hasattr(self.out_benefit_id, 'to_alipay_dict'):
                params['out_benefit_id'] = self.out_benefit_id.to_alipay_dict()
            else:
                params['out_benefit_id'] = self.out_benefit_id
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
        o = AlipayCommerceMedicalBenefitInfoQueryModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_benefit_id' in d:
            o.out_benefit_id = d['out_benefit_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


