#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AbilityResourceBizMark import AbilityResourceBizMark


class AbilityResourceConsume(object):

    def __init__(self):
        self._ability_resource_biz_mark = None
        self._consume_code = None
        self._end_time = None
        self._m_app_id = None
        self._record_val = None
        self._start_time = None

    @property
    def ability_resource_biz_mark(self):
        return self._ability_resource_biz_mark

    @ability_resource_biz_mark.setter
    def ability_resource_biz_mark(self, value):
        if isinstance(value, list):
            self._ability_resource_biz_mark = list()
            for i in value:
                if isinstance(i, AbilityResourceBizMark):
                    self._ability_resource_biz_mark.append(i)
                else:
                    self._ability_resource_biz_mark.append(AbilityResourceBizMark.from_alipay_dict(i))
    @property
    def consume_code(self):
        return self._consume_code

    @consume_code.setter
    def consume_code(self, value):
        self._consume_code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def m_app_id(self):
        return self._m_app_id

    @m_app_id.setter
    def m_app_id(self, value):
        self._m_app_id = value
    @property
    def record_val(self):
        return self._record_val

    @record_val.setter
    def record_val(self, value):
        self._record_val = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_resource_biz_mark:
            if isinstance(self.ability_resource_biz_mark, list):
                for i in range(0, len(self.ability_resource_biz_mark)):
                    element = self.ability_resource_biz_mark[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ability_resource_biz_mark[i] = element.to_alipay_dict()
            if hasattr(self.ability_resource_biz_mark, 'to_alipay_dict'):
                params['ability_resource_biz_mark'] = self.ability_resource_biz_mark.to_alipay_dict()
            else:
                params['ability_resource_biz_mark'] = self.ability_resource_biz_mark
        if self.consume_code:
            if hasattr(self.consume_code, 'to_alipay_dict'):
                params['consume_code'] = self.consume_code.to_alipay_dict()
            else:
                params['consume_code'] = self.consume_code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.m_app_id:
            if hasattr(self.m_app_id, 'to_alipay_dict'):
                params['m_app_id'] = self.m_app_id.to_alipay_dict()
            else:
                params['m_app_id'] = self.m_app_id
        if self.record_val:
            if hasattr(self.record_val, 'to_alipay_dict'):
                params['record_val'] = self.record_val.to_alipay_dict()
            else:
                params['record_val'] = self.record_val
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AbilityResourceConsume()
        if 'ability_resource_biz_mark' in d:
            o.ability_resource_biz_mark = d['ability_resource_biz_mark']
        if 'consume_code' in d:
            o.consume_code = d['consume_code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'm_app_id' in d:
            o.m_app_id = d['m_app_id']
        if 'record_val' in d:
            o.record_val = d['record_val']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


