#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo


class PoiTagInfo(object):

    def __init__(self):
        self._poi_info_list = None
        self._tag_name = None

    @property
    def poi_info_list(self):
        return self._poi_info_list

    @poi_info_list.setter
    def poi_info_list(self, value):
        if isinstance(value, list):
            self._poi_info_list = list()
            for i in value:
                if isinstance(i, PoiInfoVo):
                    self._poi_info_list.append(i)
                else:
                    self._poi_info_list.append(PoiInfoVo.from_alipay_dict(i))
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.poi_info_list:
            if isinstance(self.poi_info_list, list):
                for i in range(0, len(self.poi_info_list)):
                    element = self.poi_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_info_list[i] = element.to_alipay_dict()
            if hasattr(self.poi_info_list, 'to_alipay_dict'):
                params['poi_info_list'] = self.poi_info_list.to_alipay_dict()
            else:
                params['poi_info_list'] = self.poi_info_list
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiTagInfo()
        if 'poi_info_list' in d:
            o.poi_info_list = d['poi_info_list']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        return o


