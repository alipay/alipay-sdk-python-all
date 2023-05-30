#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromiseDetail(object):

    def __init__(self):
        self._auth_status = None
        self._create_time = None
        self._end_time = None
        self._final_time = None
        self._finish_periods = None
        self._merchant_id = None
        self._merchant_logo = None
        self._merchant_name = None
        self._out_biz_no = None
        self._period_type = None
        self._promise_name = None
        self._record_id = None
        self._record_status = None
        self._start_time = None
        self._sub_record_status = None
        self._sub_title = None
        self._template_id = None
        self._total_periods = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def final_time(self):
        return self._final_time

    @final_time.setter
    def final_time(self, value):
        self._final_time = value
    @property
    def finish_periods(self):
        return self._finish_periods

    @finish_periods.setter
    def finish_periods(self, value):
        self._finish_periods = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def promise_name(self):
        return self._promise_name

    @promise_name.setter
    def promise_name(self, value):
        self._promise_name = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_status(self):
        return self._record_status

    @record_status.setter
    def record_status(self, value):
        self._record_status = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_record_status(self):
        return self._sub_record_status

    @sub_record_status.setter
    def sub_record_status(self, value):
        self._sub_record_status = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total_periods(self):
        return self._total_periods

    @total_periods.setter
    def total_periods(self, value):
        self._total_periods = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.final_time:
            if hasattr(self.final_time, 'to_alipay_dict'):
                params['final_time'] = self.final_time.to_alipay_dict()
            else:
                params['final_time'] = self.final_time
        if self.finish_periods:
            if hasattr(self.finish_periods, 'to_alipay_dict'):
                params['finish_periods'] = self.finish_periods.to_alipay_dict()
            else:
                params['finish_periods'] = self.finish_periods
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.promise_name:
            if hasattr(self.promise_name, 'to_alipay_dict'):
                params['promise_name'] = self.promise_name.to_alipay_dict()
            else:
                params['promise_name'] = self.promise_name
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_status:
            if hasattr(self.record_status, 'to_alipay_dict'):
                params['record_status'] = self.record_status.to_alipay_dict()
            else:
                params['record_status'] = self.record_status
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_record_status:
            if hasattr(self.sub_record_status, 'to_alipay_dict'):
                params['sub_record_status'] = self.sub_record_status.to_alipay_dict()
            else:
                params['sub_record_status'] = self.sub_record_status
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.total_periods:
            if hasattr(self.total_periods, 'to_alipay_dict'):
                params['total_periods'] = self.total_periods.to_alipay_dict()
            else:
                params['total_periods'] = self.total_periods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromiseDetail()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'final_time' in d:
            o.final_time = d['final_time']
        if 'finish_periods' in d:
            o.finish_periods = d['finish_periods']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'promise_name' in d:
            o.promise_name = d['promise_name']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_status' in d:
            o.record_status = d['record_status']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_record_status' in d:
            o.sub_record_status = d['sub_record_status']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'total_periods' in d:
            o.total_periods = d['total_periods']
        return o


