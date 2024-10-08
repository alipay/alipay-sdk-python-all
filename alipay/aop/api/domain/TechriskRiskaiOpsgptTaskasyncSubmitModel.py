#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatMsg import ChatMsg


class TechriskRiskaiOpsgptTaskasyncSubmitModel(object):

    def __init__(self):
        self._agent_id = None
        self._intention = None
        self._operator = None
        self._task_source = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def intention(self):
        return self._intention

    @intention.setter
    def intention(self, value):
        if isinstance(value, ChatMsg):
            self._intention = value
        else:
            self._intention = ChatMsg.from_alipay_dict(value)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def task_source(self):
        return self._task_source

    @task_source.setter
    def task_source(self, value):
        self._task_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.intention:
            if hasattr(self.intention, 'to_alipay_dict'):
                params['intention'] = self.intention.to_alipay_dict()
            else:
                params['intention'] = self.intention
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.task_source:
            if hasattr(self.task_source, 'to_alipay_dict'):
                params['task_source'] = self.task_source.to_alipay_dict()
            else:
                params['task_source'] = self.task_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskRiskaiOpsgptTaskasyncSubmitModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'intention' in d:
            o.intention = d['intention']
        if 'operator' in d:
            o.operator = d['operator']
        if 'task_source' in d:
            o.task_source = d['task_source']
        return o


