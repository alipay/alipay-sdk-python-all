#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTuitioncodePlanruleSendModel(object):

    def __init__(self):
        self._allot_type = None
        self._execute_type = None
        self._out_biz_no = None
        self._period = None
        self._setting_type = None
        self._smid = None

    @property
    def allot_type(self):
        return self._allot_type

    @allot_type.setter
    def allot_type(self, value):
        self._allot_type = value
    @property
    def execute_type(self):
        return self._execute_type

    @execute_type.setter
    def execute_type(self, value):
        self._execute_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def setting_type(self):
        return self._setting_type

    @setting_type.setter
    def setting_type(self, value):
        self._setting_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.allot_type:
            if hasattr(self.allot_type, 'to_alipay_dict'):
                params['allot_type'] = self.allot_type.to_alipay_dict()
            else:
                params['allot_type'] = self.allot_type
        if self.execute_type:
            if hasattr(self.execute_type, 'to_alipay_dict'):
                params['execute_type'] = self.execute_type.to_alipay_dict()
            else:
                params['execute_type'] = self.execute_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.setting_type:
            if hasattr(self.setting_type, 'to_alipay_dict'):
                params['setting_type'] = self.setting_type.to_alipay_dict()
            else:
                params['setting_type'] = self.setting_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodePlanruleSendModel()
        if 'allot_type' in d:
            o.allot_type = d['allot_type']
        if 'execute_type' in d:
            o.execute_type = d['execute_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period' in d:
            o.period = d['period']
        if 'setting_type' in d:
            o.setting_type = d['setting_type']
        if 'smid' in d:
            o.smid = d['smid']
        return o


