#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHyInquiryorderSyncModel(object):

    def __init__(self):
        self._order_id = None
        self._order_modify_time = None
        self._out_doctor_id = None
        self._platform_code = None
        self._status = None
        self._status_change_desc = None
        self._sub_status = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_change_desc(self):
        return self._status_change_desc

    @status_change_desc.setter
    def status_change_desc(self, value):
        self._status_change_desc = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_change_desc:
            if hasattr(self.status_change_desc, 'to_alipay_dict'):
                params['status_change_desc'] = self.status_change_desc.to_alipay_dict()
            else:
                params['status_change_desc'] = self.status_change_desc
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHyInquiryorderSyncModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'status' in d:
            o.status = d['status']
        if 'status_change_desc' in d:
            o.status_change_desc = d['status_change_desc']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        return o


