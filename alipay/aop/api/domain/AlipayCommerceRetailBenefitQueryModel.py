#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailBenefitQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name_pattern = None
        self._activity_source = None
        self._activity_type = None
        self._page_num = None
        self._page_size = None
        self._status = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name_pattern(self):
        return self._activity_name_pattern

    @activity_name_pattern.setter
    def activity_name_pattern(self, value):
        self._activity_name_pattern = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name_pattern:
            if hasattr(self.activity_name_pattern, 'to_alipay_dict'):
                params['activity_name_pattern'] = self.activity_name_pattern.to_alipay_dict()
            else:
                params['activity_name_pattern'] = self.activity_name_pattern
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailBenefitQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name_pattern' in d:
            o.activity_name_pattern = d['activity_name_pattern']
        if 'activity_source' in d:
            o.activity_source = d['activity_source']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        return o


