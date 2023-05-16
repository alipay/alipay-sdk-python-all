#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceRecordDetailVO(object):

    def __init__(self):
        self._customer_cert_no = None
        self._customer_id = None
        self._customer_phone = None
        self._end_time = None
        self._memo = None
        self._out_biz_no = None
        self._request_id = None
        self._service_record_id = None
        self._service_source = None
        self._start_time = None

    @property
    def customer_cert_no(self):
        return self._customer_cert_no

    @customer_cert_no.setter
    def customer_cert_no(self, value):
        self._customer_cert_no = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def customer_phone(self):
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, value):
        self._customer_phone = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_record_id(self):
        return self._service_record_id

    @service_record_id.setter
    def service_record_id(self, value):
        self._service_record_id = value
    @property
    def service_source(self):
        return self._service_source

    @service_source.setter
    def service_source(self, value):
        self._service_source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_cert_no:
            if hasattr(self.customer_cert_no, 'to_alipay_dict'):
                params['customer_cert_no'] = self.customer_cert_no.to_alipay_dict()
            else:
                params['customer_cert_no'] = self.customer_cert_no
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.customer_phone:
            if hasattr(self.customer_phone, 'to_alipay_dict'):
                params['customer_phone'] = self.customer_phone.to_alipay_dict()
            else:
                params['customer_phone'] = self.customer_phone
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_record_id:
            if hasattr(self.service_record_id, 'to_alipay_dict'):
                params['service_record_id'] = self.service_record_id.to_alipay_dict()
            else:
                params['service_record_id'] = self.service_record_id
        if self.service_source:
            if hasattr(self.service_source, 'to_alipay_dict'):
                params['service_source'] = self.service_source.to_alipay_dict()
            else:
                params['service_source'] = self.service_source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceRecordDetailVO()
        if 'customer_cert_no' in d:
            o.customer_cert_no = d['customer_cert_no']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'customer_phone' in d:
            o.customer_phone = d['customer_phone']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_record_id' in d:
            o.service_record_id = d['service_record_id']
        if 'service_source' in d:
            o.service_source = d['service_source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


