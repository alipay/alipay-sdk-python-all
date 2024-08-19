#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YunTaskWhiteUserDTO import YunTaskWhiteUserDTO


class AlipayCommerceYuntaskWhitehistoryBatchcreateModel(object):

    def __init__(self):
        self._operate_open_id = None
        self._operate_user_id = None
        self._task_template_id = None
        self._white_list = None

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
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                if isinstance(i, YunTaskWhiteUserDTO):
                    self._white_list.append(i)
                else:
                    self._white_list.append(YunTaskWhiteUserDTO.from_alipay_dict(i))


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
        if self.white_list:
            if isinstance(self.white_list, list):
                for i in range(0, len(self.white_list)):
                    element = self.white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_list[i] = element.to_alipay_dict()
            if hasattr(self.white_list, 'to_alipay_dict'):
                params['white_list'] = self.white_list.to_alipay_dict()
            else:
                params['white_list'] = self.white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskWhitehistoryBatchcreateModel()
        if 'operate_open_id' in d:
            o.operate_open_id = d['operate_open_id']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'white_list' in d:
            o.white_list = d['white_list']
        return o


