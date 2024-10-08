#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo


class PoiListDayVo(object):

    def __init__(self):
        self._day = None
        self._poi_info_vo_list = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
    @property
    def poi_info_vo_list(self):
        return self._poi_info_vo_list

    @poi_info_vo_list.setter
    def poi_info_vo_list(self, value):
        if isinstance(value, list):
            self._poi_info_vo_list = list()
            for i in value:
                if isinstance(i, PoiInfoVo):
                    self._poi_info_vo_list.append(i)
                else:
                    self._poi_info_vo_list.append(PoiInfoVo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.day:
            if hasattr(self.day, 'to_alipay_dict'):
                params['day'] = self.day.to_alipay_dict()
            else:
                params['day'] = self.day
        if self.poi_info_vo_list:
            if isinstance(self.poi_info_vo_list, list):
                for i in range(0, len(self.poi_info_vo_list)):
                    element = self.poi_info_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_info_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.poi_info_vo_list, 'to_alipay_dict'):
                params['poi_info_vo_list'] = self.poi_info_vo_list.to_alipay_dict()
            else:
                params['poi_info_vo_list'] = self.poi_info_vo_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiListDayVo()
        if 'day' in d:
            o.day = d['day']
        if 'poi_info_vo_list' in d:
            o.poi_info_vo_list = d['poi_info_vo_list']
        return o


