#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDtdeployShiftQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._skill_group_ids = None
        self._start_time = None
        self._tnt_inst_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def skill_group_ids(self):
        return self._skill_group_ids

    @skill_group_ids.setter
    def skill_group_ids(self, value):
        if isinstance(value, list):
            self._skill_group_ids = list()
            for i in value:
                self._skill_group_ids.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.skill_group_ids:
            if isinstance(self.skill_group_ids, list):
                for i in range(0, len(self.skill_group_ids)):
                    element = self.skill_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.skill_group_ids, 'to_alipay_dict'):
                params['skill_group_ids'] = self.skill_group_ids.to_alipay_dict()
            else:
                params['skill_group_ids'] = self.skill_group_ids
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDtdeployShiftQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'skill_group_ids' in d:
            o.skill_group_ids = d['skill_group_ids']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


