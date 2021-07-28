#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoBenefitCheckavailableModel(object):

    def __init__(self):
        self._benefit_code = None
        self._extend = None
        self._user_id = None

    @property
    def benefit_code(self):
        return self._benefit_code

    @benefit_code.setter
    def benefit_code(self, value):
        self._benefit_code = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_code:
            if hasattr(self.benefit_code, 'to_alipay_dict'):
                params['benefit_code'] = self.benefit_code.to_alipay_dict()
            else:
                params['benefit_code'] = self.benefit_code
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
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
        o = AlipayInsAutoBenefitCheckavailableModel()
        if 'benefit_code' in d:
            o.benefit_code = d['benefit_code']
        if 'extend' in d:
            o.extend = d['extend']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


