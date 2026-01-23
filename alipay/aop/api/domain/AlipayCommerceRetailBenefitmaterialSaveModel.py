#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailBenefitmaterialSaveModel(object):

    def __init__(self):
        self._activity_material_feeds_url = None
        self._activity_material_type = None
        self._activity_material_url = None
        self._activity_name = None
        self._activity_rule = None
        self._activity_type = None
        self._brand_name = None
        self._en_info = None
        self._end_time = None
        self._material_id = None
        self._material_source = None
        self._operator = None
        self._priority = None
        self._remark = None
        self._start_time = None
        self._url = None
        self._url_type = None

    @property
    def activity_material_feeds_url(self):
        return self._activity_material_feeds_url

    @activity_material_feeds_url.setter
    def activity_material_feeds_url(self, value):
        self._activity_material_feeds_url = value
    @property
    def activity_material_type(self):
        return self._activity_material_type

    @activity_material_type.setter
    def activity_material_type(self, value):
        self._activity_material_type = value
    @property
    def activity_material_url(self):
        return self._activity_material_url

    @activity_material_url.setter
    def activity_material_url(self, value):
        self._activity_material_url = value
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
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
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
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_source(self):
        return self._material_source

    @material_source.setter
    def material_source(self, value):
        self._material_source = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_material_feeds_url:
            if hasattr(self.activity_material_feeds_url, 'to_alipay_dict'):
                params['activity_material_feeds_url'] = self.activity_material_feeds_url.to_alipay_dict()
            else:
                params['activity_material_feeds_url'] = self.activity_material_feeds_url
        if self.activity_material_type:
            if hasattr(self.activity_material_type, 'to_alipay_dict'):
                params['activity_material_type'] = self.activity_material_type.to_alipay_dict()
            else:
                params['activity_material_type'] = self.activity_material_type
        if self.activity_material_url:
            if hasattr(self.activity_material_url, 'to_alipay_dict'):
                params['activity_material_url'] = self.activity_material_url.to_alipay_dict()
            else:
                params['activity_material_url'] = self.activity_material_url
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
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
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
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_source:
            if hasattr(self.material_source, 'to_alipay_dict'):
                params['material_source'] = self.material_source.to_alipay_dict()
            else:
                params['material_source'] = self.material_source
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.url_type:
            if hasattr(self.url_type, 'to_alipay_dict'):
                params['url_type'] = self.url_type.to_alipay_dict()
            else:
                params['url_type'] = self.url_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailBenefitmaterialSaveModel()
        if 'activity_material_feeds_url' in d:
            o.activity_material_feeds_url = d['activity_material_feeds_url']
        if 'activity_material_type' in d:
            o.activity_material_type = d['activity_material_type']
        if 'activity_material_url' in d:
            o.activity_material_url = d['activity_material_url']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_rule' in d:
            o.activity_rule = d['activity_rule']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'en_info' in d:
            o.en_info = d['en_info']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_source' in d:
            o.material_source = d['material_source']
        if 'operator' in d:
            o.operator = d['operator']
        if 'priority' in d:
            o.priority = d['priority']
        if 'remark' in d:
            o.remark = d['remark']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'url' in d:
            o.url = d['url']
        if 'url_type' in d:
            o.url_type = d['url_type']
        return o


