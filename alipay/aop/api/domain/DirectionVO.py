#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScheduleStationVO import ScheduleStationVO


class DirectionVO(object):

    def __init__(self):
        self._dir = None
        self._dir_name = None
        self._schedules = None
        self._target_station_code = None
        self._target_station_name = None

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, value):
        self._dir = value
    @property
    def dir_name(self):
        return self._dir_name

    @dir_name.setter
    def dir_name(self, value):
        self._dir_name = value
    @property
    def schedules(self):
        return self._schedules

    @schedules.setter
    def schedules(self, value):
        if isinstance(value, list):
            self._schedules = list()
            for i in value:
                if isinstance(i, ScheduleStationVO):
                    self._schedules.append(i)
                else:
                    self._schedules.append(ScheduleStationVO.from_alipay_dict(i))
    @property
    def target_station_code(self):
        return self._target_station_code

    @target_station_code.setter
    def target_station_code(self, value):
        self._target_station_code = value
    @property
    def target_station_name(self):
        return self._target_station_name

    @target_station_name.setter
    def target_station_name(self, value):
        self._target_station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.dir:
            if hasattr(self.dir, 'to_alipay_dict'):
                params['dir'] = self.dir.to_alipay_dict()
            else:
                params['dir'] = self.dir
        if self.dir_name:
            if hasattr(self.dir_name, 'to_alipay_dict'):
                params['dir_name'] = self.dir_name.to_alipay_dict()
            else:
                params['dir_name'] = self.dir_name
        if self.schedules:
            if isinstance(self.schedules, list):
                for i in range(0, len(self.schedules)):
                    element = self.schedules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedules[i] = element.to_alipay_dict()
            if hasattr(self.schedules, 'to_alipay_dict'):
                params['schedules'] = self.schedules.to_alipay_dict()
            else:
                params['schedules'] = self.schedules
        if self.target_station_code:
            if hasattr(self.target_station_code, 'to_alipay_dict'):
                params['target_station_code'] = self.target_station_code.to_alipay_dict()
            else:
                params['target_station_code'] = self.target_station_code
        if self.target_station_name:
            if hasattr(self.target_station_name, 'to_alipay_dict'):
                params['target_station_name'] = self.target_station_name.to_alipay_dict()
            else:
                params['target_station_name'] = self.target_station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DirectionVO()
        if 'dir' in d:
            o.dir = d['dir']
        if 'dir_name' in d:
            o.dir_name = d['dir_name']
        if 'schedules' in d:
            o.schedules = d['schedules']
        if 'target_station_code' in d:
            o.target_station_code = d['target_station_code']
        if 'target_station_name' in d:
            o.target_station_name = d['target_station_name']
        return o


