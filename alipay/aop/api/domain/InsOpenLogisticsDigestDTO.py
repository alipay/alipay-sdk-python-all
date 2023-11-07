#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenLogisticsDigestDTO(object):

    def __init__(self):
        self._auth_code = None
        self._auth_type = None
        self._logistics_company_code = None
        self._logistics_company_name = None
        self._logistics_no = None
        self._logistics_status = None
        self._reserve_end_time = None
        self._reserve_start_time = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def logistics_company_code(self):
        return self._logistics_company_code

    @logistics_company_code.setter
    def logistics_company_code(self, value):
        self._logistics_company_code = value
    @property
    def logistics_company_name(self):
        return self._logistics_company_name

    @logistics_company_name.setter
    def logistics_company_name(self, value):
        self._logistics_company_name = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def reserve_end_time(self):
        return self._reserve_end_time

    @reserve_end_time.setter
    def reserve_end_time(self, value):
        self._reserve_end_time = value
    @property
    def reserve_start_time(self):
        return self._reserve_start_time

    @reserve_start_time.setter
    def reserve_start_time(self, value):
        self._reserve_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.logistics_company_code:
            if hasattr(self.logistics_company_code, 'to_alipay_dict'):
                params['logistics_company_code'] = self.logistics_company_code.to_alipay_dict()
            else:
                params['logistics_company_code'] = self.logistics_company_code
        if self.logistics_company_name:
            if hasattr(self.logistics_company_name, 'to_alipay_dict'):
                params['logistics_company_name'] = self.logistics_company_name.to_alipay_dict()
            else:
                params['logistics_company_name'] = self.logistics_company_name
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        if self.reserve_end_time:
            if hasattr(self.reserve_end_time, 'to_alipay_dict'):
                params['reserve_end_time'] = self.reserve_end_time.to_alipay_dict()
            else:
                params['reserve_end_time'] = self.reserve_end_time
        if self.reserve_start_time:
            if hasattr(self.reserve_start_time, 'to_alipay_dict'):
                params['reserve_start_time'] = self.reserve_start_time.to_alipay_dict()
            else:
                params['reserve_start_time'] = self.reserve_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenLogisticsDigestDTO()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'logistics_company_code' in d:
            o.logistics_company_code = d['logistics_company_code']
        if 'logistics_company_name' in d:
            o.logistics_company_name = d['logistics_company_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'reserve_end_time' in d:
            o.reserve_end_time = d['reserve_end_time']
        if 'reserve_start_time' in d:
            o.reserve_start_time = d['reserve_start_time']
        return o


