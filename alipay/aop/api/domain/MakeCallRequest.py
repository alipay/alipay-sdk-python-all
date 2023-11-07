#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MakeCallRequest(object):

    def __init__(self):
        self._callee = None
        self._mask_callee = None
        self._user_id = None

    @property
    def callee(self):
        return self._callee

    @callee.setter
    def callee(self, value):
        self._callee = value
    @property
    def mask_callee(self):
        return self._mask_callee

    @mask_callee.setter
    def mask_callee(self, value):
        self._mask_callee = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callee:
            if hasattr(self.callee, 'to_alipay_dict'):
                params['callee'] = self.callee.to_alipay_dict()
            else:
                params['callee'] = self.callee
        if self.mask_callee:
            if hasattr(self.mask_callee, 'to_alipay_dict'):
                params['mask_callee'] = self.mask_callee.to_alipay_dict()
            else:
                params['mask_callee'] = self.mask_callee
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
        o = MakeCallRequest()
        if 'callee' in d:
            o.callee = d['callee']
        if 'mask_callee' in d:
            o.mask_callee = d['mask_callee']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


