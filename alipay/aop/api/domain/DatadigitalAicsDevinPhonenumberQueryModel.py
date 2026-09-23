#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinPhonenumberQueryModel(object):

    def __init__(self):
        self._business_scene_desc = None
        self._gmt_end = None
        self._gmt_start = None
        self._page_num = None
        self._page_size = None
        self._phone_number = None
        self._phone_usage = None
        self._route_type = None
        self._route_value = None
        self._route_values = None
        self._tenant_id = None

    @property
    def business_scene_desc(self):
        return self._business_scene_desc

    @business_scene_desc.setter
    def business_scene_desc(self, value):
        self._business_scene_desc = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def phone_usage(self):
        return self._phone_usage

    @phone_usage.setter
    def phone_usage(self, value):
        self._phone_usage = value
    @property
    def route_type(self):
        return self._route_type

    @route_type.setter
    def route_type(self, value):
        self._route_type = value
    @property
    def route_value(self):
        return self._route_value

    @route_value.setter
    def route_value(self, value):
        self._route_value = value
    @property
    def route_values(self):
        return self._route_values

    @route_values.setter
    def route_values(self, value):
        if isinstance(value, list):
            self._route_values = list()
            for i in value:
                self._route_values.append(i)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_scene_desc:
            if hasattr(self.business_scene_desc, 'to_alipay_dict'):
                params['business_scene_desc'] = self.business_scene_desc.to_alipay_dict()
            else:
                params['business_scene_desc'] = self.business_scene_desc
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.phone_usage:
            if hasattr(self.phone_usage, 'to_alipay_dict'):
                params['phone_usage'] = self.phone_usage.to_alipay_dict()
            else:
                params['phone_usage'] = self.phone_usage
        if self.route_type:
            if hasattr(self.route_type, 'to_alipay_dict'):
                params['route_type'] = self.route_type.to_alipay_dict()
            else:
                params['route_type'] = self.route_type
        if self.route_value:
            if hasattr(self.route_value, 'to_alipay_dict'):
                params['route_value'] = self.route_value.to_alipay_dict()
            else:
                params['route_value'] = self.route_value
        if self.route_values:
            if isinstance(self.route_values, list):
                for i in range(0, len(self.route_values)):
                    element = self.route_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.route_values[i] = element.to_alipay_dict()
            if hasattr(self.route_values, 'to_alipay_dict'):
                params['route_values'] = self.route_values.to_alipay_dict()
            else:
                params['route_values'] = self.route_values
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinPhonenumberQueryModel()
        if 'business_scene_desc' in d:
            o.business_scene_desc = d['business_scene_desc']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'phone_usage' in d:
            o.phone_usage = d['phone_usage']
        if 'route_type' in d:
            o.route_type = d['route_type']
        if 'route_value' in d:
            o.route_value = d['route_value']
        if 'route_values' in d:
            o.route_values = d['route_values']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


