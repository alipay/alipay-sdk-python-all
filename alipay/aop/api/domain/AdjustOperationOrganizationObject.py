#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdjustOperationOrganizationObject(object):

    def __init__(self):
        self._adjust_operational_summary = None
        self._down_adjust_operational_detail = None
        self._down_direction = None
        self._route_name = None
        self._up_adjust_operational_detail = None
        self._up_direction = None

    @property
    def adjust_operational_summary(self):
        return self._adjust_operational_summary

    @adjust_operational_summary.setter
    def adjust_operational_summary(self, value):
        self._adjust_operational_summary = value
    @property
    def down_adjust_operational_detail(self):
        return self._down_adjust_operational_detail

    @down_adjust_operational_detail.setter
    def down_adjust_operational_detail(self, value):
        self._down_adjust_operational_detail = value
    @property
    def down_direction(self):
        return self._down_direction

    @down_direction.setter
    def down_direction(self, value):
        self._down_direction = value
    @property
    def route_name(self):
        return self._route_name

    @route_name.setter
    def route_name(self, value):
        self._route_name = value
    @property
    def up_adjust_operational_detail(self):
        return self._up_adjust_operational_detail

    @up_adjust_operational_detail.setter
    def up_adjust_operational_detail(self, value):
        self._up_adjust_operational_detail = value
    @property
    def up_direction(self):
        return self._up_direction

    @up_direction.setter
    def up_direction(self, value):
        self._up_direction = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_operational_summary:
            if hasattr(self.adjust_operational_summary, 'to_alipay_dict'):
                params['adjust_operational_summary'] = self.adjust_operational_summary.to_alipay_dict()
            else:
                params['adjust_operational_summary'] = self.adjust_operational_summary
        if self.down_adjust_operational_detail:
            if hasattr(self.down_adjust_operational_detail, 'to_alipay_dict'):
                params['down_adjust_operational_detail'] = self.down_adjust_operational_detail.to_alipay_dict()
            else:
                params['down_adjust_operational_detail'] = self.down_adjust_operational_detail
        if self.down_direction:
            if hasattr(self.down_direction, 'to_alipay_dict'):
                params['down_direction'] = self.down_direction.to_alipay_dict()
            else:
                params['down_direction'] = self.down_direction
        if self.route_name:
            if hasattr(self.route_name, 'to_alipay_dict'):
                params['route_name'] = self.route_name.to_alipay_dict()
            else:
                params['route_name'] = self.route_name
        if self.up_adjust_operational_detail:
            if hasattr(self.up_adjust_operational_detail, 'to_alipay_dict'):
                params['up_adjust_operational_detail'] = self.up_adjust_operational_detail.to_alipay_dict()
            else:
                params['up_adjust_operational_detail'] = self.up_adjust_operational_detail
        if self.up_direction:
            if hasattr(self.up_direction, 'to_alipay_dict'):
                params['up_direction'] = self.up_direction.to_alipay_dict()
            else:
                params['up_direction'] = self.up_direction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdjustOperationOrganizationObject()
        if 'adjust_operational_summary' in d:
            o.adjust_operational_summary = d['adjust_operational_summary']
        if 'down_adjust_operational_detail' in d:
            o.down_adjust_operational_detail = d['down_adjust_operational_detail']
        if 'down_direction' in d:
            o.down_direction = d['down_direction']
        if 'route_name' in d:
            o.route_name = d['route_name']
        if 'up_adjust_operational_detail' in d:
            o.up_adjust_operational_detail = d['up_adjust_operational_detail']
        if 'up_direction' in d:
            o.up_direction = d['up_direction']
        return o


