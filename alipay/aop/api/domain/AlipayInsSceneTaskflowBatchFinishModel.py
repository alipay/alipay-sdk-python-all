#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneTaskflowBatchFinishModel(object):

    def __init__(self):
        self._extra_map = None
        self._out_biz_no = None
        self._task_flow_id_list = None
        self._user_id = None

    @property
    def extra_map(self):
        return self._extra_map

    @extra_map.setter
    def extra_map(self, value):
        self._extra_map = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def task_flow_id_list(self):
        return self._task_flow_id_list

    @task_flow_id_list.setter
    def task_flow_id_list(self, value):
        if isinstance(value, list):
            self._task_flow_id_list = list()
            for i in value:
                self._task_flow_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_map:
            if hasattr(self.extra_map, 'to_alipay_dict'):
                params['extra_map'] = self.extra_map.to_alipay_dict()
            else:
                params['extra_map'] = self.extra_map
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.task_flow_id_list:
            if isinstance(self.task_flow_id_list, list):
                for i in range(0, len(self.task_flow_id_list)):
                    element = self.task_flow_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_flow_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_flow_id_list, 'to_alipay_dict'):
                params['task_flow_id_list'] = self.task_flow_id_list.to_alipay_dict()
            else:
                params['task_flow_id_list'] = self.task_flow_id_list
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
        o = AlipayInsSceneTaskflowBatchFinishModel()
        if 'extra_map' in d:
            o.extra_map = d['extra_map']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'task_flow_id_list' in d:
            o.task_flow_id_list = d['task_flow_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


