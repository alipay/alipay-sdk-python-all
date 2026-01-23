#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailBenefitCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._activity_rule = None
        self._activity_scope_list = None
        self._activity_source = None
        self._activity_type = None
        self._brand_logo_image = None
        self._brand_name = None
        self._en_info = None
        self._end_time = None
        self._operator = None
        self._out_biz_id = None
        self._priority = None
        self._prize_infos = None
        self._start_time = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_rule(self):
        return self._activity_rule

    @activity_rule.setter
    def activity_rule(self, value):
        self._activity_rule = value
    @property
    def activity_scope_list(self):
        return self._activity_scope_list

    @activity_scope_list.setter
    def activity_scope_list(self, value):
        if isinstance(value, list):
            self._activity_scope_list = list()
            for i in value:
                self._activity_scope_list.append(i)
    @property
    def activity_source(self):
        return self._activity_source

    @activity_source.setter
    def activity_source(self, value):
        self._activity_source = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def brand_logo_image(self):
        return self._brand_logo_image

    @brand_logo_image.setter
    def brand_logo_image(self, value):
        self._brand_logo_image = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def en_info(self):
        return self._en_info

    @en_info.setter
    def en_info(self, value):
        self._en_info = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def prize_infos(self):
        return self._prize_infos

    @prize_infos.setter
    def prize_infos(self, value):
        if isinstance(value, list):
            self._prize_infos = list()
            for i in value:
                self._prize_infos.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_rule:
            if hasattr(self.activity_rule, 'to_alipay_dict'):
                params['activity_rule'] = self.activity_rule.to_alipay_dict()
            else:
                params['activity_rule'] = self.activity_rule
        if self.activity_scope_list:
            if isinstance(self.activity_scope_list, list):
                for i in range(0, len(self.activity_scope_list)):
                    element = self.activity_scope_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_scope_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_scope_list, 'to_alipay_dict'):
                params['activity_scope_list'] = self.activity_scope_list.to_alipay_dict()
            else:
                params['activity_scope_list'] = self.activity_scope_list
        if self.activity_source:
            if hasattr(self.activity_source, 'to_alipay_dict'):
                params['activity_source'] = self.activity_source.to_alipay_dict()
            else:
                params['activity_source'] = self.activity_source
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.brand_logo_image:
            if hasattr(self.brand_logo_image, 'to_alipay_dict'):
                params['brand_logo_image'] = self.brand_logo_image.to_alipay_dict()
            else:
                params['brand_logo_image'] = self.brand_logo_image
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.en_info:
            if hasattr(self.en_info, 'to_alipay_dict'):
                params['en_info'] = self.en_info.to_alipay_dict()
            else:
                params['en_info'] = self.en_info
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.prize_infos:
            if isinstance(self.prize_infos, list):
                for i in range(0, len(self.prize_infos)):
                    element = self.prize_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_infos[i] = element.to_alipay_dict()
            if hasattr(self.prize_infos, 'to_alipay_dict'):
                params['prize_infos'] = self.prize_infos.to_alipay_dict()
            else:
                params['prize_infos'] = self.prize_infos
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailBenefitCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_rule' in d:
            o.activity_rule = d['activity_rule']
        if 'activity_scope_list' in d:
            o.activity_scope_list = d['activity_scope_list']
        if 'activity_source' in d:
            o.activity_source = d['activity_source']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'brand_logo_image' in d:
            o.brand_logo_image = d['brand_logo_image']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'en_info' in d:
            o.en_info = d['en_info']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'priority' in d:
            o.priority = d['priority']
        if 'prize_infos' in d:
            o.prize_infos = d['prize_infos']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


