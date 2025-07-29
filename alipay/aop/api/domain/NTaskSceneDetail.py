#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NTaskSceneDetail(object):

    def __init__(self):
        self._device_id = None
        self._device_type = None
        self._modify_time = None
        self._operator_contact_number = None
        self._operator_name = None
        self._position_id = None
        self._related_device_id = None
        self._status = None
        self._task_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def operator_contact_number(self):
        return self._operator_contact_number

    @operator_contact_number.setter
    def operator_contact_number(self, value):
        self._operator_contact_number = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def related_device_id(self):
        return self._related_device_id

    @related_device_id.setter
    def related_device_id(self, value):
        self._related_device_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.operator_contact_number:
            if hasattr(self.operator_contact_number, 'to_alipay_dict'):
                params['operator_contact_number'] = self.operator_contact_number.to_alipay_dict()
            else:
                params['operator_contact_number'] = self.operator_contact_number
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.related_device_id:
            if hasattr(self.related_device_id, 'to_alipay_dict'):
                params['related_device_id'] = self.related_device_id.to_alipay_dict()
            else:
                params['related_device_id'] = self.related_device_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NTaskSceneDetail()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'operator_contact_number' in d:
            o.operator_contact_number = d['operator_contact_number']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'related_device_id' in d:
            o.related_device_id = d['related_device_id']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


