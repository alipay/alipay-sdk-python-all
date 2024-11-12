#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerActivitytaskSyncModel(object):

    def __init__(self):
        self._activity_id = None
        self._activity_service_no = None
        self._event_code = None
        self._open_id = None
        self._operator_uid = None
        self._reward_id = None
        self._task_achieve_time = None
        self._task_registration_time = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_service_no(self):
        return self._activity_service_no

    @activity_service_no.setter
    def activity_service_no(self, value):
        self._activity_service_no = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def reward_id(self):
        return self._reward_id

    @reward_id.setter
    def reward_id(self, value):
        self._reward_id = value
    @property
    def task_achieve_time(self):
        return self._task_achieve_time

    @task_achieve_time.setter
    def task_achieve_time(self, value):
        self._task_achieve_time = value
    @property
    def task_registration_time(self):
        return self._task_registration_time

    @task_registration_time.setter
    def task_registration_time(self, value):
        self._task_registration_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_service_no:
            if hasattr(self.activity_service_no, 'to_alipay_dict'):
                params['activity_service_no'] = self.activity_service_no.to_alipay_dict()
            else:
                params['activity_service_no'] = self.activity_service_no
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.reward_id:
            if hasattr(self.reward_id, 'to_alipay_dict'):
                params['reward_id'] = self.reward_id.to_alipay_dict()
            else:
                params['reward_id'] = self.reward_id
        if self.task_achieve_time:
            if hasattr(self.task_achieve_time, 'to_alipay_dict'):
                params['task_achieve_time'] = self.task_achieve_time.to_alipay_dict()
            else:
                params['task_achieve_time'] = self.task_achieve_time
        if self.task_registration_time:
            if hasattr(self.task_registration_time, 'to_alipay_dict'):
                params['task_registration_time'] = self.task_registration_time.to_alipay_dict()
            else:
                params['task_registration_time'] = self.task_registration_time
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
        o = AlipayCommerceTransportChargerActivitytaskSyncModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_service_no' in d:
            o.activity_service_no = d['activity_service_no']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'reward_id' in d:
            o.reward_id = d['reward_id']
        if 'task_achieve_time' in d:
            o.task_achieve_time = d['task_achieve_time']
        if 'task_registration_time' in d:
            o.task_registration_time = d['task_registration_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


