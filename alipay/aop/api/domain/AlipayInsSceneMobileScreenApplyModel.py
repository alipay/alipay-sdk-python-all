#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsurancePerson import InsurancePerson
from alipay.aop.api.domain.ChannelBizData import ChannelBizData
from alipay.aop.api.domain.InsurancePeriod import InsurancePeriod
from alipay.aop.api.domain.InsurancePerson import InsurancePerson
from alipay.aop.api.domain.MobileDeviceInfo import MobileDeviceInfo


class AlipayInsSceneMobileScreenApplyModel(object):

    def __init__(self):
        self._applicant = None
        self._channel = None
        self._channel_biz_data = None
        self._effective_start_time = None
        self._insurance_period = None
        self._insured = None
        self._mobile_device_info = None
        self._out_biz_no = None
        self._premium = None
        self._repair_type = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsurancePerson):
            self._applicant = value
        else:
            self._applicant = InsurancePerson.from_alipay_dict(value)
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_biz_data(self):
        return self._channel_biz_data

    @channel_biz_data.setter
    def channel_biz_data(self, value):
        if isinstance(value, ChannelBizData):
            self._channel_biz_data = value
        else:
            self._channel_biz_data = ChannelBizData.from_alipay_dict(value)
    @property
    def effective_start_time(self):
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, value):
        self._effective_start_time = value
    @property
    def insurance_period(self):
        return self._insurance_period

    @insurance_period.setter
    def insurance_period(self, value):
        if isinstance(value, InsurancePeriod):
            self._insurance_period = value
        else:
            self._insurance_period = InsurancePeriod.from_alipay_dict(value)
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsurancePerson):
            self._insured = value
        else:
            self._insured = InsurancePerson.from_alipay_dict(value)
    @property
    def mobile_device_info(self):
        return self._mobile_device_info

    @mobile_device_info.setter
    def mobile_device_info(self, value):
        if isinstance(value, MobileDeviceInfo):
            self._mobile_device_info = value
        else:
            self._mobile_device_info = MobileDeviceInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_biz_data:
            if hasattr(self.channel_biz_data, 'to_alipay_dict'):
                params['channel_biz_data'] = self.channel_biz_data.to_alipay_dict()
            else:
                params['channel_biz_data'] = self.channel_biz_data
        if self.effective_start_time:
            if hasattr(self.effective_start_time, 'to_alipay_dict'):
                params['effective_start_time'] = self.effective_start_time.to_alipay_dict()
            else:
                params['effective_start_time'] = self.effective_start_time
        if self.insurance_period:
            if hasattr(self.insurance_period, 'to_alipay_dict'):
                params['insurance_period'] = self.insurance_period.to_alipay_dict()
            else:
                params['insurance_period'] = self.insurance_period
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
        if self.mobile_device_info:
            if hasattr(self.mobile_device_info, 'to_alipay_dict'):
                params['mobile_device_info'] = self.mobile_device_info.to_alipay_dict()
            else:
                params['mobile_device_info'] = self.mobile_device_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneMobileScreenApplyModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_biz_data' in d:
            o.channel_biz_data = d['channel_biz_data']
        if 'effective_start_time' in d:
            o.effective_start_time = d['effective_start_time']
        if 'insurance_period' in d:
            o.insurance_period = d['insurance_period']
        if 'insured' in d:
            o.insured = d['insured']
        if 'mobile_device_info' in d:
            o.mobile_device_info = d['mobile_device_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'premium' in d:
            o.premium = d['premium']
        if 'repair_type' in d:
            o.repair_type = d['repair_type']
        return o


