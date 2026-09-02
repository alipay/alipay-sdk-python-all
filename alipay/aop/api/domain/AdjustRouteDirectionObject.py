#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdjustRouteDirectionObject(object):

    def __init__(self):
        self._adjustment_detail = None
        self._adjustment_type = None
        self._rank = None
        self._route_name = None

    @property
    def adjustment_detail(self):
        return self._adjustment_detail

    @adjustment_detail.setter
    def adjustment_detail(self, value):
        self._adjustment_detail = value
    @property
    def adjustment_type(self):
        return self._adjustment_type

    @adjustment_type.setter
    def adjustment_type(self, value):
        self._adjustment_type = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def route_name(self):
        return self._route_name

    @route_name.setter
    def route_name(self, value):
        self._route_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjustment_detail:
            if hasattr(self.adjustment_detail, 'to_alipay_dict'):
                params['adjustment_detail'] = self.adjustment_detail.to_alipay_dict()
            else:
                params['adjustment_detail'] = self.adjustment_detail
        if self.adjustment_type:
            if hasattr(self.adjustment_type, 'to_alipay_dict'):
                params['adjustment_type'] = self.adjustment_type.to_alipay_dict()
            else:
                params['adjustment_type'] = self.adjustment_type
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.route_name:
            if hasattr(self.route_name, 'to_alipay_dict'):
                params['route_name'] = self.route_name.to_alipay_dict()
            else:
                params['route_name'] = self.route_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdjustRouteDirectionObject()
        if 'adjustment_detail' in d:
            o.adjustment_detail = d['adjustment_detail']
        if 'adjustment_type' in d:
            o.adjustment_type = d['adjustment_type']
        if 'rank' in d:
            o.rank = d['rank']
        if 'route_name' in d:
            o.route_name = d['route_name']
        return o


