#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalJumpTabApplyModel(object):

    def __init__(self):
        self._from_source = None
        self._open_id = None
        self._user_id = None

    @property
    def from_source(self):
        return self._from_source

    @from_source.setter
    def from_source(self, value):
        self._from_source = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_source:
            if hasattr(self.from_source, 'to_alipay_dict'):
                params['from_source'] = self.from_source.to_alipay_dict()
            else:
                params['from_source'] = self.from_source
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayCommerceMedicalJumpTabApplyModel()
        if 'from_source' in d:
            o.from_source = d['from_source']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


