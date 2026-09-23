#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceCpaNotifyModel(object):

    def __init__(self):
        self._alipay_order_no = None
        self._sub_task_id = None
        self._task_node = None
        self._task_node_finished = None
        self._user_id = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def sub_task_id(self):
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, value):
        self._sub_task_id = value
    @property
    def task_node(self):
        return self._task_node

    @task_node.setter
    def task_node(self, value):
        self._task_node = value
    @property
    def task_node_finished(self):
        return self._task_node_finished

    @task_node_finished.setter
    def task_node_finished(self, value):
        self._task_node_finished = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.sub_task_id:
            if hasattr(self.sub_task_id, 'to_alipay_dict'):
                params['sub_task_id'] = self.sub_task_id.to_alipay_dict()
            else:
                params['sub_task_id'] = self.sub_task_id
        if self.task_node:
            if hasattr(self.task_node, 'to_alipay_dict'):
                params['task_node'] = self.task_node.to_alipay_dict()
            else:
                params['task_node'] = self.task_node
        if self.task_node_finished:
            if hasattr(self.task_node_finished, 'to_alipay_dict'):
                params['task_node_finished'] = self.task_node_finished.to_alipay_dict()
            else:
                params['task_node_finished'] = self.task_node_finished
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
        o = AlipayEbppInstserviceCpaNotifyModel()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'sub_task_id' in d:
            o.sub_task_id = d['sub_task_id']
        if 'task_node' in d:
            o.task_node = d['task_node']
        if 'task_node_finished' in d:
            o.task_node_finished = d['task_node_finished']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


