#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskStatusInfo(object):

    def __init__(self):
        self._channel_info = None
        self._complete_count = None
        self._complete_time = None
        self._periodic_acc_count = None
        self._receive_expire_time = None
        self._signup_expire_time = None
        self._signup_time = None
        self._status = None
        self._sub_status = None
        self._task_id = None

    @property
    def channel_info(self):
        return self._channel_info

    @channel_info.setter
    def channel_info(self, value):
        self._channel_info = value
    @property
    def complete_count(self):
        return self._complete_count

    @complete_count.setter
    def complete_count(self, value):
        self._complete_count = value
    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
    @property
    def periodic_acc_count(self):
        return self._periodic_acc_count

    @periodic_acc_count.setter
    def periodic_acc_count(self, value):
        self._periodic_acc_count = value
    @property
    def receive_expire_time(self):
        return self._receive_expire_time

    @receive_expire_time.setter
    def receive_expire_time(self, value):
        self._receive_expire_time = value
    @property
    def signup_expire_time(self):
        return self._signup_expire_time

    @signup_expire_time.setter
    def signup_expire_time(self, value):
        self._signup_expire_time = value
    @property
    def signup_time(self):
        return self._signup_time

    @signup_time.setter
    def signup_time(self, value):
        self._signup_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_info:
            if hasattr(self.channel_info, 'to_alipay_dict'):
                params['channel_info'] = self.channel_info.to_alipay_dict()
            else:
                params['channel_info'] = self.channel_info
        if self.complete_count:
            if hasattr(self.complete_count, 'to_alipay_dict'):
                params['complete_count'] = self.complete_count.to_alipay_dict()
            else:
                params['complete_count'] = self.complete_count
        if self.complete_time:
            if hasattr(self.complete_time, 'to_alipay_dict'):
                params['complete_time'] = self.complete_time.to_alipay_dict()
            else:
                params['complete_time'] = self.complete_time
        if self.periodic_acc_count:
            if hasattr(self.periodic_acc_count, 'to_alipay_dict'):
                params['periodic_acc_count'] = self.periodic_acc_count.to_alipay_dict()
            else:
                params['periodic_acc_count'] = self.periodic_acc_count
        if self.receive_expire_time:
            if hasattr(self.receive_expire_time, 'to_alipay_dict'):
                params['receive_expire_time'] = self.receive_expire_time.to_alipay_dict()
            else:
                params['receive_expire_time'] = self.receive_expire_time
        if self.signup_expire_time:
            if hasattr(self.signup_expire_time, 'to_alipay_dict'):
                params['signup_expire_time'] = self.signup_expire_time.to_alipay_dict()
            else:
                params['signup_expire_time'] = self.signup_expire_time
        if self.signup_time:
            if hasattr(self.signup_time, 'to_alipay_dict'):
                params['signup_time'] = self.signup_time.to_alipay_dict()
            else:
                params['signup_time'] = self.signup_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
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
        o = TaskStatusInfo()
        if 'channel_info' in d:
            o.channel_info = d['channel_info']
        if 'complete_count' in d:
            o.complete_count = d['complete_count']
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'periodic_acc_count' in d:
            o.periodic_acc_count = d['periodic_acc_count']
        if 'receive_expire_time' in d:
            o.receive_expire_time = d['receive_expire_time']
        if 'signup_expire_time' in d:
            o.signup_expire_time = d['signup_expire_time']
        if 'signup_time' in d:
            o.signup_time = d['signup_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


