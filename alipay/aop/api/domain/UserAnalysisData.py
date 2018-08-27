#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAnalysisData(object):

    def __init__(self):
        self._cancel_user_cnt = None
        self._cumulate_user_cnt = None
        self._date = None
        self._grow_user_cnt = None
        self._new_user_cnt = None

    @property
    def cancel_user_cnt(self):
        return self._cancel_user_cnt

    @cancel_user_cnt.setter
    def cancel_user_cnt(self, value):
        self._cancel_user_cnt = value
    @property
    def cumulate_user_cnt(self):
        return self._cumulate_user_cnt

    @cumulate_user_cnt.setter
    def cumulate_user_cnt(self, value):
        self._cumulate_user_cnt = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def grow_user_cnt(self):
        return self._grow_user_cnt

    @grow_user_cnt.setter
    def grow_user_cnt(self, value):
        self._grow_user_cnt = value
    @property
    def new_user_cnt(self):
        return self._new_user_cnt

    @new_user_cnt.setter
    def new_user_cnt(self, value):
        self._new_user_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_user_cnt:
            if hasattr(self.cancel_user_cnt, 'to_alipay_dict'):
                params['cancel_user_cnt'] = self.cancel_user_cnt.to_alipay_dict()
            else:
                params['cancel_user_cnt'] = self.cancel_user_cnt
        if self.cumulate_user_cnt:
            if hasattr(self.cumulate_user_cnt, 'to_alipay_dict'):
                params['cumulate_user_cnt'] = self.cumulate_user_cnt.to_alipay_dict()
            else:
                params['cumulate_user_cnt'] = self.cumulate_user_cnt
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.grow_user_cnt:
            if hasattr(self.grow_user_cnt, 'to_alipay_dict'):
                params['grow_user_cnt'] = self.grow_user_cnt.to_alipay_dict()
            else:
                params['grow_user_cnt'] = self.grow_user_cnt
        if self.new_user_cnt:
            if hasattr(self.new_user_cnt, 'to_alipay_dict'):
                params['new_user_cnt'] = self.new_user_cnt.to_alipay_dict()
            else:
                params['new_user_cnt'] = self.new_user_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAnalysisData()
        if 'cancel_user_cnt' in d:
            o.cancel_user_cnt = d['cancel_user_cnt']
        if 'cumulate_user_cnt' in d:
            o.cumulate_user_cnt = d['cumulate_user_cnt']
        if 'date' in d:
            o.date = d['date']
        if 'grow_user_cnt' in d:
            o.grow_user_cnt = d['grow_user_cnt']
        if 'new_user_cnt' in d:
            o.new_user_cnt = d['new_user_cnt']
        return o


