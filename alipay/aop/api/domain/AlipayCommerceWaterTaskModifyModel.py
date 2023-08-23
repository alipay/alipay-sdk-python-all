#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeContent import PrizeContent


class AlipayCommerceWaterTaskModifyModel(object):

    def __init__(self):
        self._prize_content = None
        self._task_end = None
        self._task_id = None

    @property
    def prize_content(self):
        return self._prize_content

    @prize_content.setter
    def prize_content(self, value):
        if isinstance(value, PrizeContent):
            self._prize_content = value
        else:
            self._prize_content = PrizeContent.from_alipay_dict(value)
    @property
    def task_end(self):
        return self._task_end

    @task_end.setter
    def task_end(self, value):
        self._task_end = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_content:
            if hasattr(self.prize_content, 'to_alipay_dict'):
                params['prize_content'] = self.prize_content.to_alipay_dict()
            else:
                params['prize_content'] = self.prize_content
        if self.task_end:
            if hasattr(self.task_end, 'to_alipay_dict'):
                params['task_end'] = self.task_end.to_alipay_dict()
            else:
                params['task_end'] = self.task_end
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
        o = AlipayCommerceWaterTaskModifyModel()
        if 'prize_content' in d:
            o.prize_content = d['prize_content']
        if 'task_end' in d:
            o.task_end = d['task_end']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


