#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcDoctorLicenseRequest import RcDoctorLicenseRequest


class AlipaySecurityRiskLicenseSuwenIdentifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._doctor_license_request = None
        self._invoke_app_name = None
        self._invoke_token = None
        self._license_type = None
        self._request_id = None
        self._scene_code = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def doctor_license_request(self):
        return self._doctor_license_request

    @doctor_license_request.setter
    def doctor_license_request(self, value):
        if isinstance(value, RcDoctorLicenseRequest):
            self._doctor_license_request = value
        else:
            self._doctor_license_request = RcDoctorLicenseRequest.from_alipay_dict(value)
    @property
    def invoke_app_name(self):
        return self._invoke_app_name

    @invoke_app_name.setter
    def invoke_app_name(self, value):
        self._invoke_app_name = value
    @property
    def invoke_token(self):
        return self._invoke_token

    @invoke_token.setter
    def invoke_token(self, value):
        self._invoke_token = value
    @property
    def license_type(self):
        return self._license_type

    @license_type.setter
    def license_type(self, value):
        self._license_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.doctor_license_request:
            if hasattr(self.doctor_license_request, 'to_alipay_dict'):
                params['doctor_license_request'] = self.doctor_license_request.to_alipay_dict()
            else:
                params['doctor_license_request'] = self.doctor_license_request
        if self.invoke_app_name:
            if hasattr(self.invoke_app_name, 'to_alipay_dict'):
                params['invoke_app_name'] = self.invoke_app_name.to_alipay_dict()
            else:
                params['invoke_app_name'] = self.invoke_app_name
        if self.invoke_token:
            if hasattr(self.invoke_token, 'to_alipay_dict'):
                params['invoke_token'] = self.invoke_token.to_alipay_dict()
            else:
                params['invoke_token'] = self.invoke_token
        if self.license_type:
            if hasattr(self.license_type, 'to_alipay_dict'):
                params['license_type'] = self.license_type.to_alipay_dict()
            else:
                params['license_type'] = self.license_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskLicenseSuwenIdentifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'doctor_license_request' in d:
            o.doctor_license_request = d['doctor_license_request']
        if 'invoke_app_name' in d:
            o.invoke_app_name = d['invoke_app_name']
        if 'invoke_token' in d:
            o.invoke_token = d['invoke_token']
        if 'license_type' in d:
            o.license_type = d['license_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


