#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusUserInfo import CloudbusUserInfo


class MetroOdItem(object):

    def __init__(self):
        self._dest_geo = None
        self._od = None
        self._time = None
        self._user_info = None
        self._week_od = None
        self._work_od = None

    @property
    def dest_geo(self):
        return self._dest_geo

    @dest_geo.setter
    def dest_geo(self, value):
        self._dest_geo = value
    @property
    def od(self):
        return self._od

    @od.setter
    def od(self, value):
        self._od = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, CloudbusUserInfo):
            self._user_info = value
        else:
            self._user_info = CloudbusUserInfo.from_alipay_dict(value)
    @property
    def week_od(self):
        return self._week_od

    @week_od.setter
    def week_od(self, value):
        self._week_od = value
    @property
    def work_od(self):
        return self._work_od

    @work_od.setter
    def work_od(self, value):
        self._work_od = value


    def to_alipay_dict(self):
        params = dict()
        if self.dest_geo:
            if hasattr(self.dest_geo, 'to_alipay_dict'):
                params['dest_geo'] = self.dest_geo.to_alipay_dict()
            else:
                params['dest_geo'] = self.dest_geo
        if self.od:
            if hasattr(self.od, 'to_alipay_dict'):
                params['od'] = self.od.to_alipay_dict()
            else:
                params['od'] = self.od
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        if self.week_od:
            if hasattr(self.week_od, 'to_alipay_dict'):
                params['week_od'] = self.week_od.to_alipay_dict()
            else:
                params['week_od'] = self.week_od
        if self.work_od:
            if hasattr(self.work_od, 'to_alipay_dict'):
                params['work_od'] = self.work_od.to_alipay_dict()
            else:
                params['work_od'] = self.work_od
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MetroOdItem()
        if 'dest_geo' in d:
            o.dest_geo = d['dest_geo']
        if 'od' in d:
            o.od = d['od']
        if 'time' in d:
            o.time = d['time']
        if 'user_info' in d:
            o.user_info = d['user_info']
        if 'week_od' in d:
            o.week_od = d['week_od']
        if 'work_od' in d:
            o.work_od = d['work_od']
        return o


