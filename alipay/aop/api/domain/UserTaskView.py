#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserTaskView(object):

    def __init__(self):
        self._identification = None
        self._phone_number = None
        self._service_charge = None
        self._task_id = None
        self._user_id = None
        self._user_task_id = None
        self._weike_user_id = None
        self._weike_user_name = None

    @property
    def identification(self):
        return self._identification

    @identification.setter
    def identification(self, value):
        self._identification = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def service_charge(self):
        return self._service_charge

    @service_charge.setter
    def service_charge(self, value):
        self._service_charge = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value
    @property
    def weike_user_id(self):
        return self._weike_user_id

    @weike_user_id.setter
    def weike_user_id(self, value):
        self._weike_user_id = value
    @property
    def weike_user_name(self):
        return self._weike_user_name

    @weike_user_name.setter
    def weike_user_name(self, value):
        self._weike_user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.identification:
            if hasattr(self.identification, 'to_alipay_dict'):
                params['identification'] = self.identification.to_alipay_dict()
            else:
                params['identification'] = self.identification
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.service_charge:
            if hasattr(self.service_charge, 'to_alipay_dict'):
                params['service_charge'] = self.service_charge.to_alipay_dict()
            else:
                params['service_charge'] = self.service_charge
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_task_id:
            if hasattr(self.user_task_id, 'to_alipay_dict'):
                params['user_task_id'] = self.user_task_id.to_alipay_dict()
            else:
                params['user_task_id'] = self.user_task_id
        if self.weike_user_id:
            if hasattr(self.weike_user_id, 'to_alipay_dict'):
                params['weike_user_id'] = self.weike_user_id.to_alipay_dict()
            else:
                params['weike_user_id'] = self.weike_user_id
        if self.weike_user_name:
            if hasattr(self.weike_user_name, 'to_alipay_dict'):
                params['weike_user_name'] = self.weike_user_name.to_alipay_dict()
            else:
                params['weike_user_name'] = self.weike_user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserTaskView()
        if 'identification' in d:
            o.identification = d['identification']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'service_charge' in d:
            o.service_charge = d['service_charge']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        if 'weike_user_id' in d:
            o.weike_user_id = d['weike_user_id']
        if 'weike_user_name' in d:
            o.weike_user_name = d['weike_user_name']
        return o


