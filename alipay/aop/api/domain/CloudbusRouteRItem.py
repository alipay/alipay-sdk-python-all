#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusPredictRItem import CloudbusPredictRItem
from alipay.aop.api.domain.CloudbusPredictRItem import CloudbusPredictRItem


class CloudbusRouteRItem(object):

    def __init__(self):
        self._after = None
        self._before = None
        self._direction = None
        self._line_id = None
        self._line_name = None

    @property
    def after(self):
        return self._after

    @after.setter
    def after(self, value):
        if isinstance(value, CloudbusPredictRItem):
            self._after = value
        else:
            self._after = CloudbusPredictRItem.from_alipay_dict(value)
    @property
    def before(self):
        return self._before

    @before.setter
    def before(self, value):
        if isinstance(value, CloudbusPredictRItem):
            self._before = value
        else:
            self._before = CloudbusPredictRItem.from_alipay_dict(value)
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def line_name(self):
        return self._line_name

    @line_name.setter
    def line_name(self, value):
        self._line_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.after:
            if hasattr(self.after, 'to_alipay_dict'):
                params['after'] = self.after.to_alipay_dict()
            else:
                params['after'] = self.after
        if self.before:
            if hasattr(self.before, 'to_alipay_dict'):
                params['before'] = self.before.to_alipay_dict()
            else:
                params['before'] = self.before
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.line_name:
            if hasattr(self.line_name, 'to_alipay_dict'):
                params['line_name'] = self.line_name.to_alipay_dict()
            else:
                params['line_name'] = self.line_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusRouteRItem()
        if 'after' in d:
            o.after = d['after']
        if 'before' in d:
            o.before = d['before']
        if 'direction' in d:
            o.direction = d['direction']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_name' in d:
            o.line_name = d['line_name']
        return o


