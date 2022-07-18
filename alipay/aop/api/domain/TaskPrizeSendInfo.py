#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeSendInfo import PrizeSendInfo


class TaskPrizeSendInfo(object):

    def __init__(self):
        self._prize_send_list = None
        self._task_id = None

    @property
    def prize_send_list(self):
        return self._prize_send_list

    @prize_send_list.setter
    def prize_send_list(self, value):
        if isinstance(value, list):
            self._prize_send_list = list()
            for i in value:
                if isinstance(i, PrizeSendInfo):
                    self._prize_send_list.append(i)
                else:
                    self._prize_send_list.append(PrizeSendInfo.from_alipay_dict(i))
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_send_list:
            if isinstance(self.prize_send_list, list):
                for i in range(0, len(self.prize_send_list)):
                    element = self.prize_send_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_send_list[i] = element.to_alipay_dict()
            if hasattr(self.prize_send_list, 'to_alipay_dict'):
                params['prize_send_list'] = self.prize_send_list.to_alipay_dict()
            else:
                params['prize_send_list'] = self.prize_send_list
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
        o = TaskPrizeSendInfo()
        if 'prize_send_list' in d:
            o.prize_send_list = d['prize_send_list']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


