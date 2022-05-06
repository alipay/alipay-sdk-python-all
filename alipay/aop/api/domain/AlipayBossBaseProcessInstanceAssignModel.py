#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessInstanceAssignModel(object):

    def __init__(self):
        self._assignee = None
        self._assignee_work_no = None
        self._memo = None
        self._node = None
        self._operator_id = None
        self._pu_id = None
        self._task_operator_id = None

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._assignee = value
    @property
    def assignee_work_no(self):
        return self._assignee_work_no

    @assignee_work_no.setter
    def assignee_work_no(self, value):
        self._assignee_work_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def pu_id(self):
        return self._pu_id

    @pu_id.setter
    def pu_id(self, value):
        self._pu_id = value
    @property
    def task_operator_id(self):
        return self._task_operator_id

    @task_operator_id.setter
    def task_operator_id(self, value):
        self._task_operator_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assignee:
            if hasattr(self.assignee, 'to_alipay_dict'):
                params['assignee'] = self.assignee.to_alipay_dict()
            else:
                params['assignee'] = self.assignee
        if self.assignee_work_no:
            if hasattr(self.assignee_work_no, 'to_alipay_dict'):
                params['assignee_work_no'] = self.assignee_work_no.to_alipay_dict()
            else:
                params['assignee_work_no'] = self.assignee_work_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.pu_id:
            if hasattr(self.pu_id, 'to_alipay_dict'):
                params['pu_id'] = self.pu_id.to_alipay_dict()
            else:
                params['pu_id'] = self.pu_id
        if self.task_operator_id:
            if hasattr(self.task_operator_id, 'to_alipay_dict'):
                params['task_operator_id'] = self.task_operator_id.to_alipay_dict()
            else:
                params['task_operator_id'] = self.task_operator_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessInstanceAssignModel()
        if 'assignee' in d:
            o.assignee = d['assignee']
        if 'assignee_work_no' in d:
            o.assignee_work_no = d['assignee_work_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'node' in d:
            o.node = d['node']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'pu_id' in d:
            o.pu_id = d['pu_id']
        if 'task_operator_id' in d:
            o.task_operator_id = d['task_operator_id']
        return o


