#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YunTaskShopStatisticInfo(object):

    def __init__(self):
        self._received_number = None
        self._status = None
        self._task_end_time = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None
        self._task_type = None
        self._total_marker_amount = None
        self._total_point_amount = None
        self._total_target_point = None

    @property
    def received_number(self):
        return self._received_number

    @received_number.setter
    def received_number(self, value):
        self._received_number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def total_marker_amount(self):
        return self._total_marker_amount

    @total_marker_amount.setter
    def total_marker_amount(self, value):
        self._total_marker_amount = value
    @property
    def total_point_amount(self):
        return self._total_point_amount

    @total_point_amount.setter
    def total_point_amount(self, value):
        self._total_point_amount = value
    @property
    def total_target_point(self):
        return self._total_target_point

    @total_target_point.setter
    def total_target_point(self, value):
        self._total_target_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.received_number:
            if hasattr(self.received_number, 'to_alipay_dict'):
                params['received_number'] = self.received_number.to_alipay_dict()
            else:
                params['received_number'] = self.received_number
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.total_marker_amount:
            if hasattr(self.total_marker_amount, 'to_alipay_dict'):
                params['total_marker_amount'] = self.total_marker_amount.to_alipay_dict()
            else:
                params['total_marker_amount'] = self.total_marker_amount
        if self.total_point_amount:
            if hasattr(self.total_point_amount, 'to_alipay_dict'):
                params['total_point_amount'] = self.total_point_amount.to_alipay_dict()
            else:
                params['total_point_amount'] = self.total_point_amount
        if self.total_target_point:
            if hasattr(self.total_target_point, 'to_alipay_dict'):
                params['total_target_point'] = self.total_target_point.to_alipay_dict()
            else:
                params['total_target_point'] = self.total_target_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskShopStatisticInfo()
        if 'received_number' in d:
            o.received_number = d['received_number']
        if 'status' in d:
            o.status = d['status']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'total_marker_amount' in d:
            o.total_marker_amount = d['total_marker_amount']
        if 'total_point_amount' in d:
            o.total_point_amount = d['total_point_amount']
        if 'total_target_point' in d:
            o.total_target_point = d['total_target_point']
        return o


