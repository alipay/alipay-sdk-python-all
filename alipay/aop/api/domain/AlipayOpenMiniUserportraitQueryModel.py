#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniUserportraitQueryModel(object):

    def __init__(self):
        self._date_scope = None
        self._portrait_type = None
        self._user_type = None

    @property
    def date_scope(self):
        return self._date_scope

    @date_scope.setter
    def date_scope(self, value):
        self._date_scope = value
    @property
    def portrait_type(self):
        return self._portrait_type

    @portrait_type.setter
    def portrait_type(self, value):
        self._portrait_type = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.date_scope:
            if hasattr(self.date_scope, 'to_alipay_dict'):
                params['date_scope'] = self.date_scope.to_alipay_dict()
            else:
                params['date_scope'] = self.date_scope
        if self.portrait_type:
            if hasattr(self.portrait_type, 'to_alipay_dict'):
                params['portrait_type'] = self.portrait_type.to_alipay_dict()
            else:
                params['portrait_type'] = self.portrait_type
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniUserportraitQueryModel()
        if 'date_scope' in d:
            o.date_scope = d['date_scope']
        if 'portrait_type' in d:
            o.portrait_type = d['portrait_type']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


