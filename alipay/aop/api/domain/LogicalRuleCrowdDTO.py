#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogicalRuleGroupDTO import LogicalRuleGroupDTO


class LogicalRuleCrowdDTO(object):

    def __init__(self):
        self._crowd_name = None
        self._crowd_scene = None
        self._export_to_gotone = None
        self._gmt_expired_time = None
        self._rules = None
        self._schedule_time = None
        self._schedule_type = None
        self._source_type = None

    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def crowd_scene(self):
        return self._crowd_scene

    @crowd_scene.setter
    def crowd_scene(self, value):
        self._crowd_scene = value
    @property
    def export_to_gotone(self):
        return self._export_to_gotone

    @export_to_gotone.setter
    def export_to_gotone(self, value):
        self._export_to_gotone = value
    @property
    def gmt_expired_time(self):
        return self._gmt_expired_time

    @gmt_expired_time.setter
    def gmt_expired_time(self, value):
        self._gmt_expired_time = value
    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        if isinstance(value, list):
            self._rules = list()
            for i in value:
                if isinstance(i, LogicalRuleGroupDTO):
                    self._rules.append(i)
                else:
                    self._rules.append(LogicalRuleGroupDTO.from_alipay_dict(i))
    @property
    def schedule_time(self):
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, value):
        self._schedule_time = value
    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, value):
        self._schedule_type = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.crowd_scene:
            if hasattr(self.crowd_scene, 'to_alipay_dict'):
                params['crowd_scene'] = self.crowd_scene.to_alipay_dict()
            else:
                params['crowd_scene'] = self.crowd_scene
        if self.export_to_gotone:
            if hasattr(self.export_to_gotone, 'to_alipay_dict'):
                params['export_to_gotone'] = self.export_to_gotone.to_alipay_dict()
            else:
                params['export_to_gotone'] = self.export_to_gotone
        if self.gmt_expired_time:
            if hasattr(self.gmt_expired_time, 'to_alipay_dict'):
                params['gmt_expired_time'] = self.gmt_expired_time.to_alipay_dict()
            else:
                params['gmt_expired_time'] = self.gmt_expired_time
        if self.rules:
            if isinstance(self.rules, list):
                for i in range(0, len(self.rules)):
                    element = self.rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rules[i] = element.to_alipay_dict()
            if hasattr(self.rules, 'to_alipay_dict'):
                params['rules'] = self.rules.to_alipay_dict()
            else:
                params['rules'] = self.rules
        if self.schedule_time:
            if hasattr(self.schedule_time, 'to_alipay_dict'):
                params['schedule_time'] = self.schedule_time.to_alipay_dict()
            else:
                params['schedule_time'] = self.schedule_time
        if self.schedule_type:
            if hasattr(self.schedule_type, 'to_alipay_dict'):
                params['schedule_type'] = self.schedule_type.to_alipay_dict()
            else:
                params['schedule_type'] = self.schedule_type
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogicalRuleCrowdDTO()
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'crowd_scene' in d:
            o.crowd_scene = d['crowd_scene']
        if 'export_to_gotone' in d:
            o.export_to_gotone = d['export_to_gotone']
        if 'gmt_expired_time' in d:
            o.gmt_expired_time = d['gmt_expired_time']
        if 'rules' in d:
            o.rules = d['rules']
        if 'schedule_time' in d:
            o.schedule_time = d['schedule_time']
        if 'schedule_type' in d:
            o.schedule_type = d['schedule_type']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


