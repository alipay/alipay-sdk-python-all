#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateTask import OperateTask


class AlipayCommerceAbntaskModifyModel(object):

    def __init__(self):
        self._operate_task_list = None
        self._operation_time = None
        self._operator_id = None
        self._operator_nick = None

    @property
    def operate_task_list(self):
        return self._operate_task_list

    @operate_task_list.setter
    def operate_task_list(self, value):
        if isinstance(value, list):
            self._operate_task_list = list()
            for i in value:
                if isinstance(i, OperateTask):
                    self._operate_task_list.append(i)
                else:
                    self._operate_task_list.append(OperateTask.from_alipay_dict(i))
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_nick(self):
        return self._operator_nick

    @operator_nick.setter
    def operator_nick(self, value):
        self._operator_nick = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_task_list:
            if isinstance(self.operate_task_list, list):
                for i in range(0, len(self.operate_task_list)):
                    element = self.operate_task_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operate_task_list[i] = element.to_alipay_dict()
            if hasattr(self.operate_task_list, 'to_alipay_dict'):
                params['operate_task_list'] = self.operate_task_list.to_alipay_dict()
            else:
                params['operate_task_list'] = self.operate_task_list
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_nick:
            if hasattr(self.operator_nick, 'to_alipay_dict'):
                params['operator_nick'] = self.operator_nick.to_alipay_dict()
            else:
                params['operator_nick'] = self.operator_nick
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAbntaskModifyModel()
        if 'operate_task_list' in d:
            o.operate_task_list = d['operate_task_list']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_nick' in d:
            o.operator_nick = d['operator_nick']
        return o


