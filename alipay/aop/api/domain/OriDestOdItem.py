#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OriDestOdItem(object):

    def __init__(self):
        self._dest_geo = None
        self._od = None
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
        o = OriDestOdItem()
        if 'dest_geo' in d:
            o.dest_geo = d['dest_geo']
        if 'od' in d:
            o.od = d['od']
        if 'week_od' in d:
            o.week_od = d['week_od']
        if 'work_od' in d:
            o.work_od = d['work_od']
        return o


