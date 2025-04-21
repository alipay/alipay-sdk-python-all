#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduPlacePointInfo import EduPlacePointInfo


class EduPlaceInfo(object):

    def __init__(self):
        self._employee_no_list = None
        self._inst_id = None
        self._out_biz_no = None
        self._parent_id = None
        self._place_id = None
        self._place_label = None
        self._place_logo = None
        self._place_name = None
        self._poi = None

    @property
    def employee_no_list(self):
        return self._employee_no_list

    @employee_no_list.setter
    def employee_no_list(self, value):
        if isinstance(value, list):
            self._employee_no_list = list()
            for i in value:
                self._employee_no_list.append(i)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
    @property
    def place_label(self):
        return self._place_label

    @place_label.setter
    def place_label(self, value):
        self._place_label = value
    @property
    def place_logo(self):
        return self._place_logo

    @place_logo.setter
    def place_logo(self, value):
        self._place_logo = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def poi(self):
        return self._poi

    @poi.setter
    def poi(self, value):
        if isinstance(value, EduPlacePointInfo):
            self._poi = value
        else:
            self._poi = EduPlacePointInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.employee_no_list:
            if isinstance(self.employee_no_list, list):
                for i in range(0, len(self.employee_no_list)):
                    element = self.employee_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_no_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_no_list, 'to_alipay_dict'):
                params['employee_no_list'] = self.employee_no_list.to_alipay_dict()
            else:
                params['employee_no_list'] = self.employee_no_list
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        if self.place_label:
            if hasattr(self.place_label, 'to_alipay_dict'):
                params['place_label'] = self.place_label.to_alipay_dict()
            else:
                params['place_label'] = self.place_label
        if self.place_logo:
            if hasattr(self.place_logo, 'to_alipay_dict'):
                params['place_logo'] = self.place_logo.to_alipay_dict()
            else:
                params['place_logo'] = self.place_logo
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.poi:
            if hasattr(self.poi, 'to_alipay_dict'):
                params['poi'] = self.poi.to_alipay_dict()
            else:
                params['poi'] = self.poi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduPlaceInfo()
        if 'employee_no_list' in d:
            o.employee_no_list = d['employee_no_list']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'place_id' in d:
            o.place_id = d['place_id']
        if 'place_label' in d:
            o.place_label = d['place_label']
        if 'place_logo' in d:
            o.place_logo = d['place_logo']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'poi' in d:
            o.poi = d['poi']
        return o


