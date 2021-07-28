#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WorkPatternDetail import WorkPatternDetail


class WorkPattern(object):

    def __init__(self):
        self._direction = None
        self._ext_param = None
        self._max_work_time = None
        self._work_count = None
        self._work_pattern_detail_list = None
        self._work_pattern_id = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def max_work_time(self):
        return self._max_work_time

    @max_work_time.setter
    def max_work_time(self, value):
        self._max_work_time = value
    @property
    def work_count(self):
        return self._work_count

    @work_count.setter
    def work_count(self, value):
        self._work_count = value
    @property
    def work_pattern_detail_list(self):
        return self._work_pattern_detail_list

    @work_pattern_detail_list.setter
    def work_pattern_detail_list(self, value):
        if isinstance(value, list):
            self._work_pattern_detail_list = list()
            for i in value:
                if isinstance(i, WorkPatternDetail):
                    self._work_pattern_detail_list.append(i)
                else:
                    self._work_pattern_detail_list.append(WorkPatternDetail.from_alipay_dict(i))
    @property
    def work_pattern_id(self):
        return self._work_pattern_id

    @work_pattern_id.setter
    def work_pattern_id(self, value):
        self._work_pattern_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.max_work_time:
            if hasattr(self.max_work_time, 'to_alipay_dict'):
                params['max_work_time'] = self.max_work_time.to_alipay_dict()
            else:
                params['max_work_time'] = self.max_work_time
        if self.work_count:
            if hasattr(self.work_count, 'to_alipay_dict'):
                params['work_count'] = self.work_count.to_alipay_dict()
            else:
                params['work_count'] = self.work_count
        if self.work_pattern_detail_list:
            if isinstance(self.work_pattern_detail_list, list):
                for i in range(0, len(self.work_pattern_detail_list)):
                    element = self.work_pattern_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_pattern_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.work_pattern_detail_list, 'to_alipay_dict'):
                params['work_pattern_detail_list'] = self.work_pattern_detail_list.to_alipay_dict()
            else:
                params['work_pattern_detail_list'] = self.work_pattern_detail_list
        if self.work_pattern_id:
            if hasattr(self.work_pattern_id, 'to_alipay_dict'):
                params['work_pattern_id'] = self.work_pattern_id.to_alipay_dict()
            else:
                params['work_pattern_id'] = self.work_pattern_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkPattern()
        if 'direction' in d:
            o.direction = d['direction']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'max_work_time' in d:
            o.max_work_time = d['max_work_time']
        if 'work_count' in d:
            o.work_count = d['work_count']
        if 'work_pattern_detail_list' in d:
            o.work_pattern_detail_list = d['work_pattern_detail_list']
        if 'work_pattern_id' in d:
            o.work_pattern_id = d['work_pattern_id']
        return o


