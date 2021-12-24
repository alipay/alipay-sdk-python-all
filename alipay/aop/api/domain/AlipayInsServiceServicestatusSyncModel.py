#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsServiceServicestatusSyncModel(object):

    def __init__(self):
        self._biz_data = None
        self._service_no = None
        self._service_status = None
        self._status_update_time = None
        self._trace_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def service_no(self):
        return self._service_no

    @service_no.setter
    def service_no(self, value):
        self._service_no = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def status_update_time(self):
        return self._status_update_time

    @status_update_time.setter
    def status_update_time(self, value):
        self._status_update_time = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.service_no:
            if hasattr(self.service_no, 'to_alipay_dict'):
                params['service_no'] = self.service_no.to_alipay_dict()
            else:
                params['service_no'] = self.service_no
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.status_update_time:
            if hasattr(self.status_update_time, 'to_alipay_dict'):
                params['status_update_time'] = self.status_update_time.to_alipay_dict()
            else:
                params['status_update_time'] = self.status_update_time
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsServiceServicestatusSyncModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'service_no' in d:
            o.service_no = d['service_no']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'status_update_time' in d:
            o.status_update_time = d['status_update_time']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


