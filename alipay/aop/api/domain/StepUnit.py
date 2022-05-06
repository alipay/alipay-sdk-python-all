#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StepUnit(object):

    def __init__(self):
        self._deal_date = None
        self._memo = None
        self._operate = None
        self._user = None
        self._work_no = None

    @property
    def deal_date(self):
        return self._deal_date

    @deal_date.setter
    def deal_date(self, value):
        self._deal_date = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deal_date:
            if hasattr(self.deal_date, 'to_alipay_dict'):
                params['deal_date'] = self.deal_date.to_alipay_dict()
            else:
                params['deal_date'] = self.deal_date
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StepUnit()
        if 'deal_date' in d:
            o.deal_date = d['deal_date']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operate' in d:
            o.operate = d['operate']
        if 'user' in d:
            o.user = d['user']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


