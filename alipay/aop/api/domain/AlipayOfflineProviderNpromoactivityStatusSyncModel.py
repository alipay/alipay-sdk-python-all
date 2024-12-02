#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpromoactivityStatusSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._in_advance_ps = None
        self._in_advance_reason_code = None
        self._operate_type = None
        self._status = None
        self._sub_activity_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def in_advance_ps(self):
        return self._in_advance_ps

    @in_advance_ps.setter
    def in_advance_ps(self, value):
        self._in_advance_ps = value
    @property
    def in_advance_reason_code(self):
        return self._in_advance_reason_code

    @in_advance_reason_code.setter
    def in_advance_reason_code(self, value):
        self._in_advance_reason_code = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.in_advance_ps:
            if hasattr(self.in_advance_ps, 'to_alipay_dict'):
                params['in_advance_ps'] = self.in_advance_ps.to_alipay_dict()
            else:
                params['in_advance_ps'] = self.in_advance_ps
        if self.in_advance_reason_code:
            if hasattr(self.in_advance_reason_code, 'to_alipay_dict'):
                params['in_advance_reason_code'] = self.in_advance_reason_code.to_alipay_dict()
            else:
                params['in_advance_reason_code'] = self.in_advance_reason_code
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_activity_id:
            if hasattr(self.sub_activity_id, 'to_alipay_dict'):
                params['sub_activity_id'] = self.sub_activity_id.to_alipay_dict()
            else:
                params['sub_activity_id'] = self.sub_activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpromoactivityStatusSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'in_advance_ps' in d:
            o.in_advance_ps = d['in_advance_ps']
        if 'in_advance_reason_code' in d:
            o.in_advance_reason_code = d['in_advance_reason_code']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'status' in d:
            o.status = d['status']
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        return o


