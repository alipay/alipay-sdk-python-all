#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceUserDataVO(object):

    def __init__(self):
        self._profile_type = None
        self._profile_value = None
        self._report_date = None
        self._user_cnt = None
        self._user_ratio = None

    @property
    def profile_type(self):
        return self._profile_type

    @profile_type.setter
    def profile_type(self, value):
        self._profile_type = value
    @property
    def profile_value(self):
        return self._profile_value

    @profile_value.setter
    def profile_value(self, value):
        self._profile_value = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def user_cnt(self):
        return self._user_cnt

    @user_cnt.setter
    def user_cnt(self, value):
        self._user_cnt = value
    @property
    def user_ratio(self):
        return self._user_ratio

    @user_ratio.setter
    def user_ratio(self, value):
        self._user_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.profile_type:
            if hasattr(self.profile_type, 'to_alipay_dict'):
                params['profile_type'] = self.profile_type.to_alipay_dict()
            else:
                params['profile_type'] = self.profile_type
        if self.profile_value:
            if hasattr(self.profile_value, 'to_alipay_dict'):
                params['profile_value'] = self.profile_value.to_alipay_dict()
            else:
                params['profile_value'] = self.profile_value
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.user_cnt:
            if hasattr(self.user_cnt, 'to_alipay_dict'):
                params['user_cnt'] = self.user_cnt.to_alipay_dict()
            else:
                params['user_cnt'] = self.user_cnt
        if self.user_ratio:
            if hasattr(self.user_ratio, 'to_alipay_dict'):
                params['user_ratio'] = self.user_ratio.to_alipay_dict()
            else:
                params['user_ratio'] = self.user_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceUserDataVO()
        if 'profile_type' in d:
            o.profile_type = d['profile_type']
        if 'profile_value' in d:
            o.profile_value = d['profile_value']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'user_cnt' in d:
            o.user_cnt = d['user_cnt']
        if 'user_ratio' in d:
            o.user_ratio = d['user_ratio']
        return o


