#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskConfirmModel(object):

    def __init__(self):
        self._funder_id = None
        self._funder_type = None
        self._operate_user_id = None
        self._owner_pid = None
        self._task_template_id = None

    @property
    def funder_id(self):
        return self._funder_id

    @funder_id.setter
    def funder_id(self, value):
        self._funder_id = value
    @property
    def funder_type(self):
        return self._funder_type

    @funder_type.setter
    def funder_type(self, value):
        self._funder_type = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.funder_id:
            if hasattr(self.funder_id, 'to_alipay_dict'):
                params['funder_id'] = self.funder_id.to_alipay_dict()
            else:
                params['funder_id'] = self.funder_id
        if self.funder_type:
            if hasattr(self.funder_type, 'to_alipay_dict'):
                params['funder_type'] = self.funder_type.to_alipay_dict()
            else:
                params['funder_type'] = self.funder_type
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskConfirmModel()
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'funder_type' in d:
            o.funder_type = d['funder_type']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


