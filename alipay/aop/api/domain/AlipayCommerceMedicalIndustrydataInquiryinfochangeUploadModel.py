#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataInquiryinfochangeUploadModel(object):

    def __init__(self):
        self._doctor_id = None
        self._doctor_name = None
        self._ext_doctor_id = None
        self._inquiry_id = None
        self._platform_code = None
        self._reason = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def ext_doctor_id(self):
        return self._ext_doctor_id

    @ext_doctor_id.setter
    def ext_doctor_id(self, value):
        self._ext_doctor_id = value
    @property
    def inquiry_id(self):
        return self._inquiry_id

    @inquiry_id.setter
    def inquiry_id(self, value):
        self._inquiry_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.ext_doctor_id:
            if hasattr(self.ext_doctor_id, 'to_alipay_dict'):
                params['ext_doctor_id'] = self.ext_doctor_id.to_alipay_dict()
            else:
                params['ext_doctor_id'] = self.ext_doctor_id
        if self.inquiry_id:
            if hasattr(self.inquiry_id, 'to_alipay_dict'):
                params['inquiry_id'] = self.inquiry_id.to_alipay_dict()
            else:
                params['inquiry_id'] = self.inquiry_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataInquiryinfochangeUploadModel()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'ext_doctor_id' in d:
            o.ext_doctor_id = d['ext_doctor_id']
        if 'inquiry_id' in d:
            o.inquiry_id = d['inquiry_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'reason' in d:
            o.reason = d['reason']
        return o


