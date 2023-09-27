#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaoKeRewardRecordDTO(object):

    def __init__(self):
        self._guided_open_id = None
        self._guided_uid = None
        self._hunter_id = None
        self._hunter_open_id = None
        self._mini_app_id = None
        self._out_biz_no = None
        self._reward_amount = None
        self._status = None
        self._task_instance_id = None

    @property
    def guided_open_id(self):
        return self._guided_open_id

    @guided_open_id.setter
    def guided_open_id(self, value):
        self._guided_open_id = value
    @property
    def guided_uid(self):
        return self._guided_uid

    @guided_uid.setter
    def guided_uid(self, value):
        self._guided_uid = value
    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def hunter_open_id(self):
        return self._hunter_open_id

    @hunter_open_id.setter
    def hunter_open_id(self, value):
        self._hunter_open_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reward_amount(self):
        return self._reward_amount

    @reward_amount.setter
    def reward_amount(self, value):
        self._reward_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.guided_open_id:
            if hasattr(self.guided_open_id, 'to_alipay_dict'):
                params['guided_open_id'] = self.guided_open_id.to_alipay_dict()
            else:
                params['guided_open_id'] = self.guided_open_id
        if self.guided_uid:
            if hasattr(self.guided_uid, 'to_alipay_dict'):
                params['guided_uid'] = self.guided_uid.to_alipay_dict()
            else:
                params['guided_uid'] = self.guided_uid
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.hunter_open_id:
            if hasattr(self.hunter_open_id, 'to_alipay_dict'):
                params['hunter_open_id'] = self.hunter_open_id.to_alipay_dict()
            else:
                params['hunter_open_id'] = self.hunter_open_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reward_amount:
            if hasattr(self.reward_amount, 'to_alipay_dict'):
                params['reward_amount'] = self.reward_amount.to_alipay_dict()
            else:
                params['reward_amount'] = self.reward_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaoKeRewardRecordDTO()
        if 'guided_open_id' in d:
            o.guided_open_id = d['guided_open_id']
        if 'guided_uid' in d:
            o.guided_uid = d['guided_uid']
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'hunter_open_id' in d:
            o.hunter_open_id = d['hunter_open_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reward_amount' in d:
            o.reward_amount = d['reward_amount']
        if 'status' in d:
            o.status = d['status']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        return o


