#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoNfccheckinQueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._user_mark = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def user_mark(self):
        return self._user_mark

    @user_mark.setter
    def user_mark(self, value):
        self._user_mark = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.user_mark:
            if hasattr(self.user_mark, 'to_alipay_dict'):
                params['user_mark'] = self.user_mark.to_alipay_dict()
            else:
                params['user_mark'] = self.user_mark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderExpoNfccheckinQueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'user_mark' in d:
            o.user_mark = d['user_mark']
        return o


