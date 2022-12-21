#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemPlanContentDO import ItemPlanContentDO


class AlipayMerchantLiveItemplanModifyModel(object):

    def __init__(self):
        self._content = None
        self._end_time = None
        self._op_type = None
        self._operator_appid = None
        self._operator_type = None
        self._plan_name = None
        self._start_time = None
        self._status = None
        self._target_id = None
        self._target_range = None
        self._target_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, ItemPlanContentDO):
                    self._content.append(i)
                else:
                    self._content.append(ItemPlanContentDO.from_alipay_dict(i))
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def operator_appid(self):
        return self._operator_appid

    @operator_appid.setter
    def operator_appid(self, value):
        self._operator_appid = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_range(self):
        return self._target_range

    @target_range.setter
    def target_range(self, value):
        self._target_range = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if isinstance(self.content, list):
                for i in range(0, len(self.content)):
                    element = self.content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content[i] = element.to_alipay_dict()
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.operator_appid:
            if hasattr(self.operator_appid, 'to_alipay_dict'):
                params['operator_appid'] = self.operator_appid.to_alipay_dict()
            else:
                params['operator_appid'] = self.operator_appid
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_range:
            if hasattr(self.target_range, 'to_alipay_dict'):
                params['target_range'] = self.target_range.to_alipay_dict()
            else:
                params['target_range'] = self.target_range
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantLiveItemplanModifyModel()
        if 'content' in d:
            o.content = d['content']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'operator_appid' in d:
            o.operator_appid = d['operator_appid']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_range' in d:
            o.target_range = d['target_range']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


