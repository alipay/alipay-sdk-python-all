#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessDistrictInfo(object):

    def __init__(self):
        self._bindable = None
        self._business_district_id = None
        self._business_district_name = None
        self._unbindable_error_code = None
        self._unbindable_error_msg = None

    @property
    def bindable(self):
        return self._bindable

    @bindable.setter
    def bindable(self, value):
        self._bindable = value
    @property
    def business_district_id(self):
        return self._business_district_id

    @business_district_id.setter
    def business_district_id(self, value):
        self._business_district_id = value
    @property
    def business_district_name(self):
        return self._business_district_name

    @business_district_name.setter
    def business_district_name(self, value):
        self._business_district_name = value
    @property
    def unbindable_error_code(self):
        return self._unbindable_error_code

    @unbindable_error_code.setter
    def unbindable_error_code(self, value):
        self._unbindable_error_code = value
    @property
    def unbindable_error_msg(self):
        return self._unbindable_error_msg

    @unbindable_error_msg.setter
    def unbindable_error_msg(self, value):
        self._unbindable_error_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.bindable:
            if hasattr(self.bindable, 'to_alipay_dict'):
                params['bindable'] = self.bindable.to_alipay_dict()
            else:
                params['bindable'] = self.bindable
        if self.business_district_id:
            if hasattr(self.business_district_id, 'to_alipay_dict'):
                params['business_district_id'] = self.business_district_id.to_alipay_dict()
            else:
                params['business_district_id'] = self.business_district_id
        if self.business_district_name:
            if hasattr(self.business_district_name, 'to_alipay_dict'):
                params['business_district_name'] = self.business_district_name.to_alipay_dict()
            else:
                params['business_district_name'] = self.business_district_name
        if self.unbindable_error_code:
            if hasattr(self.unbindable_error_code, 'to_alipay_dict'):
                params['unbindable_error_code'] = self.unbindable_error_code.to_alipay_dict()
            else:
                params['unbindable_error_code'] = self.unbindable_error_code
        if self.unbindable_error_msg:
            if hasattr(self.unbindable_error_msg, 'to_alipay_dict'):
                params['unbindable_error_msg'] = self.unbindable_error_msg.to_alipay_dict()
            else:
                params['unbindable_error_msg'] = self.unbindable_error_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessDistrictInfo()
        if 'bindable' in d:
            o.bindable = d['bindable']
        if 'business_district_id' in d:
            o.business_district_id = d['business_district_id']
        if 'business_district_name' in d:
            o.business_district_name = d['business_district_name']
        if 'unbindable_error_code' in d:
            o.unbindable_error_code = d['unbindable_error_code']
        if 'unbindable_error_msg' in d:
            o.unbindable_error_msg = d['unbindable_error_msg']
        return o


