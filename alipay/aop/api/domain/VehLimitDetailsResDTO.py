#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehLimitDetailsResDTO(object):

    def __init__(self):
        self._isv_code = None
        self._lbs_city_code = None
        self._limit_area = None
        self._limit_rule_detail = None
        self._limit_rule_name = None
        self._limit_tail_num = None
        self._limit_time = None

    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def lbs_city_code(self):
        return self._lbs_city_code

    @lbs_city_code.setter
    def lbs_city_code(self, value):
        self._lbs_city_code = value
    @property
    def limit_area(self):
        return self._limit_area

    @limit_area.setter
    def limit_area(self, value):
        self._limit_area = value
    @property
    def limit_rule_detail(self):
        return self._limit_rule_detail

    @limit_rule_detail.setter
    def limit_rule_detail(self, value):
        self._limit_rule_detail = value
    @property
    def limit_rule_name(self):
        return self._limit_rule_name

    @limit_rule_name.setter
    def limit_rule_name(self, value):
        self._limit_rule_name = value
    @property
    def limit_tail_num(self):
        return self._limit_tail_num

    @limit_tail_num.setter
    def limit_tail_num(self, value):
        self._limit_tail_num = value
    @property
    def limit_time(self):
        return self._limit_time

    @limit_time.setter
    def limit_time(self, value):
        self._limit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.lbs_city_code:
            if hasattr(self.lbs_city_code, 'to_alipay_dict'):
                params['lbs_city_code'] = self.lbs_city_code.to_alipay_dict()
            else:
                params['lbs_city_code'] = self.lbs_city_code
        if self.limit_area:
            if hasattr(self.limit_area, 'to_alipay_dict'):
                params['limit_area'] = self.limit_area.to_alipay_dict()
            else:
                params['limit_area'] = self.limit_area
        if self.limit_rule_detail:
            if hasattr(self.limit_rule_detail, 'to_alipay_dict'):
                params['limit_rule_detail'] = self.limit_rule_detail.to_alipay_dict()
            else:
                params['limit_rule_detail'] = self.limit_rule_detail
        if self.limit_rule_name:
            if hasattr(self.limit_rule_name, 'to_alipay_dict'):
                params['limit_rule_name'] = self.limit_rule_name.to_alipay_dict()
            else:
                params['limit_rule_name'] = self.limit_rule_name
        if self.limit_tail_num:
            if hasattr(self.limit_tail_num, 'to_alipay_dict'):
                params['limit_tail_num'] = self.limit_tail_num.to_alipay_dict()
            else:
                params['limit_tail_num'] = self.limit_tail_num
        if self.limit_time:
            if hasattr(self.limit_time, 'to_alipay_dict'):
                params['limit_time'] = self.limit_time.to_alipay_dict()
            else:
                params['limit_time'] = self.limit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehLimitDetailsResDTO()
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'lbs_city_code' in d:
            o.lbs_city_code = d['lbs_city_code']
        if 'limit_area' in d:
            o.limit_area = d['limit_area']
        if 'limit_rule_detail' in d:
            o.limit_rule_detail = d['limit_rule_detail']
        if 'limit_rule_name' in d:
            o.limit_rule_name = d['limit_rule_name']
        if 'limit_tail_num' in d:
            o.limit_tail_num = d['limit_tail_num']
        if 'limit_time' in d:
            o.limit_time = d['limit_time']
        return o


