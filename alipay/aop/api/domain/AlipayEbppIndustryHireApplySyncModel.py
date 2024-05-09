#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryHireApplySyncModel(object):

    def __init__(self):
        self._apply_id = None
        self._apply_status = None
        self._detail_reason = None
        self._inappropriate_reason = None
        self._open_id = None
        self._operation_time = None
        self._process_exception_reason = None
        self._user_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def detail_reason(self):
        return self._detail_reason

    @detail_reason.setter
    def detail_reason(self, value):
        self._detail_reason = value
    @property
    def inappropriate_reason(self):
        return self._inappropriate_reason

    @inappropriate_reason.setter
    def inappropriate_reason(self, value):
        self._inappropriate_reason = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def process_exception_reason(self):
        return self._process_exception_reason

    @process_exception_reason.setter
    def process_exception_reason(self, value):
        self._process_exception_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.detail_reason:
            if hasattr(self.detail_reason, 'to_alipay_dict'):
                params['detail_reason'] = self.detail_reason.to_alipay_dict()
            else:
                params['detail_reason'] = self.detail_reason
        if self.inappropriate_reason:
            if hasattr(self.inappropriate_reason, 'to_alipay_dict'):
                params['inappropriate_reason'] = self.inappropriate_reason.to_alipay_dict()
            else:
                params['inappropriate_reason'] = self.inappropriate_reason
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.process_exception_reason:
            if hasattr(self.process_exception_reason, 'to_alipay_dict'):
                params['process_exception_reason'] = self.process_exception_reason.to_alipay_dict()
            else:
                params['process_exception_reason'] = self.process_exception_reason
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryHireApplySyncModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'detail_reason' in d:
            o.detail_reason = d['detail_reason']
        if 'inappropriate_reason' in d:
            o.inappropriate_reason = d['inappropriate_reason']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'process_exception_reason' in d:
            o.process_exception_reason = d['process_exception_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


