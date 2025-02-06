#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InquiryDoctorShiftCaseData import InquiryDoctorShiftCaseData


class InquiryChannel(object):

    def __init__(self):
        self._inquiry_doctor_shift_case_list = None
        self._inquiry_mode = None
        self._inquiry_price = None
        self._inquiry_type = None
        self._inquiry_url = None
        self._register_flag = None
        self._service_duration = None

    @property
    def inquiry_doctor_shift_case_list(self):
        return self._inquiry_doctor_shift_case_list

    @inquiry_doctor_shift_case_list.setter
    def inquiry_doctor_shift_case_list(self, value):
        if isinstance(value, list):
            self._inquiry_doctor_shift_case_list = list()
            for i in value:
                if isinstance(i, InquiryDoctorShiftCaseData):
                    self._inquiry_doctor_shift_case_list.append(i)
                else:
                    self._inquiry_doctor_shift_case_list.append(InquiryDoctorShiftCaseData.from_alipay_dict(i))
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def inquiry_price(self):
        return self._inquiry_price

    @inquiry_price.setter
    def inquiry_price(self, value):
        self._inquiry_price = value
    @property
    def inquiry_type(self):
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, value):
        self._inquiry_type = value
    @property
    def inquiry_url(self):
        return self._inquiry_url

    @inquiry_url.setter
    def inquiry_url(self, value):
        self._inquiry_url = value
    @property
    def register_flag(self):
        return self._register_flag

    @register_flag.setter
    def register_flag(self, value):
        self._register_flag = value
    @property
    def service_duration(self):
        return self._service_duration

    @service_duration.setter
    def service_duration(self, value):
        self._service_duration = value


    def to_alipay_dict(self):
        params = dict()
        if self.inquiry_doctor_shift_case_list:
            if isinstance(self.inquiry_doctor_shift_case_list, list):
                for i in range(0, len(self.inquiry_doctor_shift_case_list)):
                    element = self.inquiry_doctor_shift_case_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inquiry_doctor_shift_case_list[i] = element.to_alipay_dict()
            if hasattr(self.inquiry_doctor_shift_case_list, 'to_alipay_dict'):
                params['inquiry_doctor_shift_case_list'] = self.inquiry_doctor_shift_case_list.to_alipay_dict()
            else:
                params['inquiry_doctor_shift_case_list'] = self.inquiry_doctor_shift_case_list
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.inquiry_price:
            if hasattr(self.inquiry_price, 'to_alipay_dict'):
                params['inquiry_price'] = self.inquiry_price.to_alipay_dict()
            else:
                params['inquiry_price'] = self.inquiry_price
        if self.inquiry_type:
            if hasattr(self.inquiry_type, 'to_alipay_dict'):
                params['inquiry_type'] = self.inquiry_type.to_alipay_dict()
            else:
                params['inquiry_type'] = self.inquiry_type
        if self.inquiry_url:
            if hasattr(self.inquiry_url, 'to_alipay_dict'):
                params['inquiry_url'] = self.inquiry_url.to_alipay_dict()
            else:
                params['inquiry_url'] = self.inquiry_url
        if self.register_flag:
            if hasattr(self.register_flag, 'to_alipay_dict'):
                params['register_flag'] = self.register_flag.to_alipay_dict()
            else:
                params['register_flag'] = self.register_flag
        if self.service_duration:
            if hasattr(self.service_duration, 'to_alipay_dict'):
                params['service_duration'] = self.service_duration.to_alipay_dict()
            else:
                params['service_duration'] = self.service_duration
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryChannel()
        if 'inquiry_doctor_shift_case_list' in d:
            o.inquiry_doctor_shift_case_list = d['inquiry_doctor_shift_case_list']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'inquiry_price' in d:
            o.inquiry_price = d['inquiry_price']
        if 'inquiry_type' in d:
            o.inquiry_type = d['inquiry_type']
        if 'inquiry_url' in d:
            o.inquiry_url = d['inquiry_url']
        if 'register_flag' in d:
            o.register_flag = d['register_flag']
        if 'service_duration' in d:
            o.service_duration = d['service_duration']
        return o


