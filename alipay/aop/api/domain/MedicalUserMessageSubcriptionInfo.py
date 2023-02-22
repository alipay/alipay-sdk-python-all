#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalUserMessageSubcriptionInfo(object):

    def __init__(self):
        self._industry_type_id = None
        self._open_id = None
        self._state = None
        self._user_id = None

    @property
    def industry_type_id(self):
        return self._industry_type_id

    @industry_type_id.setter
    def industry_type_id(self, value):
        self._industry_type_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_type_id:
            if hasattr(self.industry_type_id, 'to_alipay_dict'):
                params['industry_type_id'] = self.industry_type_id.to_alipay_dict()
            else:
                params['industry_type_id'] = self.industry_type_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
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
        o = MedicalUserMessageSubcriptionInfo()
        if 'industry_type_id' in d:
            o.industry_type_id = d['industry_type_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'state' in d:
            o.state = d['state']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


