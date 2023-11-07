#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPackageInstance(object):

    def __init__(self):
        self._commodity_code = None
        self._commodity_name = None
        self._end_time = None
        self._spec_code = None
        self._spec_instance_id = None
        self._spec_name = None
        self._start_time = None

    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def spec_instance_id(self):
        return self._spec_instance_id

    @spec_instance_id.setter
    def spec_instance_id(self, value):
        self._spec_instance_id = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.spec_instance_id:
            if hasattr(self.spec_instance_id, 'to_alipay_dict'):
                params['spec_instance_id'] = self.spec_instance_id.to_alipay_dict()
            else:
                params['spec_instance_id'] = self.spec_instance_id
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
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
        o = ItemPackageInstance()
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'spec_instance_id' in d:
            o.spec_instance_id = d['spec_instance_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


