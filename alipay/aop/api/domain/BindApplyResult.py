#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceSalesParticipate import DeviceSalesParticipate


class BindApplyResult(object):

    def __init__(self):
        self._apply_status = None
        self._device_bind_status = None
        self._device_bind_time = None
        self._error_code = None
        self._out_biz_no = None
        self._sales_participate = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def device_bind_status(self):
        return self._device_bind_status

    @device_bind_status.setter
    def device_bind_status(self, value):
        self._device_bind_status = value
    @property
    def device_bind_time(self):
        return self._device_bind_time

    @device_bind_time.setter
    def device_bind_time(self, value):
        self._device_bind_time = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sales_participate(self):
        return self._sales_participate

    @sales_participate.setter
    def sales_participate(self, value):
        if isinstance(value, DeviceSalesParticipate):
            self._sales_participate = value
        else:
            self._sales_participate = DeviceSalesParticipate.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.device_bind_status:
            if hasattr(self.device_bind_status, 'to_alipay_dict'):
                params['device_bind_status'] = self.device_bind_status.to_alipay_dict()
            else:
                params['device_bind_status'] = self.device_bind_status
        if self.device_bind_time:
            if hasattr(self.device_bind_time, 'to_alipay_dict'):
                params['device_bind_time'] = self.device_bind_time.to_alipay_dict()
            else:
                params['device_bind_time'] = self.device_bind_time
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sales_participate:
            if hasattr(self.sales_participate, 'to_alipay_dict'):
                params['sales_participate'] = self.sales_participate.to_alipay_dict()
            else:
                params['sales_participate'] = self.sales_participate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BindApplyResult()
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'device_bind_status' in d:
            o.device_bind_status = d['device_bind_status']
        if 'device_bind_time' in d:
            o.device_bind_time = d['device_bind_time']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sales_participate' in d:
            o.sales_participate = d['sales_participate']
        return o


