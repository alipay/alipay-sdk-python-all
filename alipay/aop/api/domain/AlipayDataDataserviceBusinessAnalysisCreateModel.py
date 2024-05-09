#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceBusinessAnalysisCreateModel(object):

    def __init__(self):
        self._business_code = None
        self._mall_id = None
        self._mall_range = None
        self._partner_id = None
        self._schedule_end_date = None
        self._schedule_start_date = None
        self._schedule_type = None
        self._task_name = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_range(self):
        return self._mall_range

    @mall_range.setter
    def mall_range(self, value):
        self._mall_range = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def schedule_end_date(self):
        return self._schedule_end_date

    @schedule_end_date.setter
    def schedule_end_date(self, value):
        self._schedule_end_date = value
    @property
    def schedule_start_date(self):
        return self._schedule_start_date

    @schedule_start_date.setter
    def schedule_start_date(self, value):
        self._schedule_start_date = value
    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, value):
        self._schedule_type = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.mall_range:
            if hasattr(self.mall_range, 'to_alipay_dict'):
                params['mall_range'] = self.mall_range.to_alipay_dict()
            else:
                params['mall_range'] = self.mall_range
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.schedule_end_date:
            if hasattr(self.schedule_end_date, 'to_alipay_dict'):
                params['schedule_end_date'] = self.schedule_end_date.to_alipay_dict()
            else:
                params['schedule_end_date'] = self.schedule_end_date
        if self.schedule_start_date:
            if hasattr(self.schedule_start_date, 'to_alipay_dict'):
                params['schedule_start_date'] = self.schedule_start_date.to_alipay_dict()
            else:
                params['schedule_start_date'] = self.schedule_start_date
        if self.schedule_type:
            if hasattr(self.schedule_type, 'to_alipay_dict'):
                params['schedule_type'] = self.schedule_type.to_alipay_dict()
            else:
                params['schedule_type'] = self.schedule_type
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceBusinessAnalysisCreateModel()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'mall_range' in d:
            o.mall_range = d['mall_range']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'schedule_end_date' in d:
            o.schedule_end_date = d['schedule_end_date']
        if 'schedule_start_date' in d:
            o.schedule_start_date = d['schedule_start_date']
        if 'schedule_type' in d:
            o.schedule_type = d['schedule_type']
        if 'task_name' in d:
            o.task_name = d['task_name']
        return o


