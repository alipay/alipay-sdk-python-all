#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneApplicationMobileApplyModel(object):

    def __init__(self):
        self._applicant = None
        self._biz_data = None
        self._channel = None
        self._effective_end_time = None
        self._effective_start_time = None
        self._insured = None
        self._out_biz_no = None
        self._period = None
        self._premium = None
        self._repair_type = None
        self._sp_no = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsPerson):
            self._applicant = value
        else:
            self._applicant = InsPerson.from_alipay_dict(value)
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def effective_end_time(self):
        return self._effective_end_time

    @effective_end_time.setter
    def effective_end_time(self, value):
        self._effective_end_time = value
    @property
    def effective_start_time(self):
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, value):
        self._effective_start_time = value
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsPerson):
            self._insured = value
        else:
            self._insured = InsPerson.from_alipay_dict(value)
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
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def repair_type(self):
        return self._repair_type

    @repair_type.setter
    def repair_type(self, value):
        self._repair_type = value
    @property
    def sp_no(self):
        return self._sp_no

    @sp_no.setter
    def sp_no(self, value):
        self._sp_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.effective_end_time:
            if hasattr(self.effective_end_time, 'to_alipay_dict'):
                params['effective_end_time'] = self.effective_end_time.to_alipay_dict()
            else:
                params['effective_end_time'] = self.effective_end_time
        if self.effective_start_time:
            if hasattr(self.effective_start_time, 'to_alipay_dict'):
                params['effective_start_time'] = self.effective_start_time.to_alipay_dict()
            else:
                params['effective_start_time'] = self.effective_start_time
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
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
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.repair_type:
            if hasattr(self.repair_type, 'to_alipay_dict'):
                params['repair_type'] = self.repair_type.to_alipay_dict()
            else:
                params['repair_type'] = self.repair_type
        if self.sp_no:
            if hasattr(self.sp_no, 'to_alipay_dict'):
                params['sp_no'] = self.sp_no.to_alipay_dict()
            else:
                params['sp_no'] = self.sp_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationMobileApplyModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'channel' in d:
            o.channel = d['channel']
        if 'effective_end_time' in d:
            o.effective_end_time = d['effective_end_time']
        if 'effective_start_time' in d:
            o.effective_start_time = d['effective_start_time']
        if 'insured' in d:
            o.insured = d['insured']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period' in d:
            o.period = d['period']
        if 'premium' in d:
            o.premium = d['premium']
        if 'repair_type' in d:
            o.repair_type = d['repair_type']
        if 'sp_no' in d:
            o.sp_no = d['sp_no']
        return o


