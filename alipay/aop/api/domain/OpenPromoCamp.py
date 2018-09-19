#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenPromoCamp(object):

    def __init__(self):
        self._camp_alias = None
        self._camp_desc = None
        self._camp_end_time = None
        self._camp_name = None
        self._camp_start_time = None
        self._camp_type = None

    @property
    def camp_alias(self):
        return self._camp_alias

    @camp_alias.setter
    def camp_alias(self, value):
        self._camp_alias = value
    @property
    def camp_desc(self):
        return self._camp_desc

    @camp_desc.setter
    def camp_desc(self, value):
        self._camp_desc = value
    @property
    def camp_end_time(self):
        return self._camp_end_time

    @camp_end_time.setter
    def camp_end_time(self, value):
        self._camp_end_time = value
    @property
    def camp_name(self):
        return self._camp_name

    @camp_name.setter
    def camp_name(self, value):
        self._camp_name = value
    @property
    def camp_start_time(self):
        return self._camp_start_time

    @camp_start_time.setter
    def camp_start_time(self, value):
        self._camp_start_time = value
    @property
    def camp_type(self):
        return self._camp_type

    @camp_type.setter
    def camp_type(self, value):
        self._camp_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_alias:
            if hasattr(self.camp_alias, 'to_alipay_dict'):
                params['camp_alias'] = self.camp_alias.to_alipay_dict()
            else:
                params['camp_alias'] = self.camp_alias
        if self.camp_desc:
            if hasattr(self.camp_desc, 'to_alipay_dict'):
                params['camp_desc'] = self.camp_desc.to_alipay_dict()
            else:
                params['camp_desc'] = self.camp_desc
        if self.camp_end_time:
            if hasattr(self.camp_end_time, 'to_alipay_dict'):
                params['camp_end_time'] = self.camp_end_time.to_alipay_dict()
            else:
                params['camp_end_time'] = self.camp_end_time
        if self.camp_name:
            if hasattr(self.camp_name, 'to_alipay_dict'):
                params['camp_name'] = self.camp_name.to_alipay_dict()
            else:
                params['camp_name'] = self.camp_name
        if self.camp_start_time:
            if hasattr(self.camp_start_time, 'to_alipay_dict'):
                params['camp_start_time'] = self.camp_start_time.to_alipay_dict()
            else:
                params['camp_start_time'] = self.camp_start_time
        if self.camp_type:
            if hasattr(self.camp_type, 'to_alipay_dict'):
                params['camp_type'] = self.camp_type.to_alipay_dict()
            else:
                params['camp_type'] = self.camp_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPromoCamp()
        if 'camp_alias' in d:
            o.camp_alias = d['camp_alias']
        if 'camp_desc' in d:
            o.camp_desc = d['camp_desc']
        if 'camp_end_time' in d:
            o.camp_end_time = d['camp_end_time']
        if 'camp_name' in d:
            o.camp_name = d['camp_name']
        if 'camp_start_time' in d:
            o.camp_start_time = d['camp_start_time']
        if 'camp_type' in d:
            o.camp_type = d['camp_type']
        return o


