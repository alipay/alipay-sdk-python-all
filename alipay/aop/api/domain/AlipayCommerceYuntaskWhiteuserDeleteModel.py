#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskWhiteuserDeleteModel(object):

    def __init__(self):
        self._operate_open_id = None
        self._operate_user_id = None
        self._task_template_id = None
        self._white_phone = None

    @property
    def operate_open_id(self):
        return self._operate_open_id

    @operate_open_id.setter
    def operate_open_id(self, value):
        self._operate_open_id = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
    @property
    def white_phone(self):
        return self._white_phone

    @white_phone.setter
    def white_phone(self, value):
        self._white_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_open_id:
            if hasattr(self.operate_open_id, 'to_alipay_dict'):
                params['operate_open_id'] = self.operate_open_id.to_alipay_dict()
            else:
                params['operate_open_id'] = self.operate_open_id
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        if self.white_phone:
            if hasattr(self.white_phone, 'to_alipay_dict'):
                params['white_phone'] = self.white_phone.to_alipay_dict()
            else:
                params['white_phone'] = self.white_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskWhiteuserDeleteModel()
        if 'operate_open_id' in d:
            o.operate_open_id = d['operate_open_id']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'white_phone' in d:
            o.white_phone = d['white_phone']
        return o


