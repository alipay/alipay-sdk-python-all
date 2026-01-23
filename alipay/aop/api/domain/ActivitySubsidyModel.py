#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivitySubsidyModel(object):

    def __init__(self):
        self._dec_activity_code = None
        self._dec_fee_fq_rate_version = None
        self._dec_fee_grade = None
        self._install_num = None
        self._user_fq_seller_percent = None

    @property
    def dec_activity_code(self):
        return self._dec_activity_code

    @dec_activity_code.setter
    def dec_activity_code(self, value):
        self._dec_activity_code = value
    @property
    def dec_fee_fq_rate_version(self):
        return self._dec_fee_fq_rate_version

    @dec_fee_fq_rate_version.setter
    def dec_fee_fq_rate_version(self, value):
        self._dec_fee_fq_rate_version = value
    @property
    def dec_fee_grade(self):
        return self._dec_fee_grade

    @dec_fee_grade.setter
    def dec_fee_grade(self, value):
        self._dec_fee_grade = value
    @property
    def install_num(self):
        return self._install_num

    @install_num.setter
    def install_num(self, value):
        self._install_num = value
    @property
    def user_fq_seller_percent(self):
        return self._user_fq_seller_percent

    @user_fq_seller_percent.setter
    def user_fq_seller_percent(self, value):
        self._user_fq_seller_percent = value


    def to_alipay_dict(self):
        params = dict()
        if self.dec_activity_code:
            if hasattr(self.dec_activity_code, 'to_alipay_dict'):
                params['dec_activity_code'] = self.dec_activity_code.to_alipay_dict()
            else:
                params['dec_activity_code'] = self.dec_activity_code
        if self.dec_fee_fq_rate_version:
            if hasattr(self.dec_fee_fq_rate_version, 'to_alipay_dict'):
                params['dec_fee_fq_rate_version'] = self.dec_fee_fq_rate_version.to_alipay_dict()
            else:
                params['dec_fee_fq_rate_version'] = self.dec_fee_fq_rate_version
        if self.dec_fee_grade:
            if hasattr(self.dec_fee_grade, 'to_alipay_dict'):
                params['dec_fee_grade'] = self.dec_fee_grade.to_alipay_dict()
            else:
                params['dec_fee_grade'] = self.dec_fee_grade
        if self.install_num:
            if hasattr(self.install_num, 'to_alipay_dict'):
                params['install_num'] = self.install_num.to_alipay_dict()
            else:
                params['install_num'] = self.install_num
        if self.user_fq_seller_percent:
            if hasattr(self.user_fq_seller_percent, 'to_alipay_dict'):
                params['user_fq_seller_percent'] = self.user_fq_seller_percent.to_alipay_dict()
            else:
                params['user_fq_seller_percent'] = self.user_fq_seller_percent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivitySubsidyModel()
        if 'dec_activity_code' in d:
            o.dec_activity_code = d['dec_activity_code']
        if 'dec_fee_fq_rate_version' in d:
            o.dec_fee_fq_rate_version = d['dec_fee_fq_rate_version']
        if 'dec_fee_grade' in d:
            o.dec_fee_grade = d['dec_fee_grade']
        if 'install_num' in d:
            o.install_num = d['install_num']
        if 'user_fq_seller_percent' in d:
            o.user_fq_seller_percent = d['user_fq_seller_percent']
        return o


