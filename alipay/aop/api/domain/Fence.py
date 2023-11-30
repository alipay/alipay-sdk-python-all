#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderPoint import OrderPoint
from alipay.aop.api.domain.FencePoint import FencePoint


class Fence(object):

    def __init__(self):
        self._grid_id = None
        self._hex_id = None
        self._his_order = None
        self._order_count = None
        self._points = None
        self._rank = None

    @property
    def grid_id(self):
        return self._grid_id

    @grid_id.setter
    def grid_id(self, value):
        self._grid_id = value
    @property
    def hex_id(self):
        return self._hex_id

    @hex_id.setter
    def hex_id(self, value):
        self._hex_id = value
    @property
    def his_order(self):
        return self._his_order

    @his_order.setter
    def his_order(self, value):
        if isinstance(value, list):
            self._his_order = list()
            for i in value:
                if isinstance(i, OrderPoint):
                    self._his_order.append(i)
                else:
                    self._his_order.append(OrderPoint.from_alipay_dict(i))
    @property
    def order_count(self):
        return self._order_count

    @order_count.setter
    def order_count(self, value):
        self._order_count = value
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if isinstance(value, list):
            self._points = list()
            for i in value:
                if isinstance(i, FencePoint):
                    self._points.append(i)
                else:
                    self._points.append(FencePoint.from_alipay_dict(i))
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value


    def to_alipay_dict(self):
        params = dict()
        if self.grid_id:
            if hasattr(self.grid_id, 'to_alipay_dict'):
                params['grid_id'] = self.grid_id.to_alipay_dict()
            else:
                params['grid_id'] = self.grid_id
        if self.hex_id:
            if hasattr(self.hex_id, 'to_alipay_dict'):
                params['hex_id'] = self.hex_id.to_alipay_dict()
            else:
                params['hex_id'] = self.hex_id
        if self.his_order:
            if isinstance(self.his_order, list):
                for i in range(0, len(self.his_order)):
                    element = self.his_order[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.his_order[i] = element.to_alipay_dict()
            if hasattr(self.his_order, 'to_alipay_dict'):
                params['his_order'] = self.his_order.to_alipay_dict()
            else:
                params['his_order'] = self.his_order
        if self.order_count:
            if hasattr(self.order_count, 'to_alipay_dict'):
                params['order_count'] = self.order_count.to_alipay_dict()
            else:
                params['order_count'] = self.order_count
        if self.points:
            if isinstance(self.points, list):
                for i in range(0, len(self.points)):
                    element = self.points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.points[i] = element.to_alipay_dict()
            if hasattr(self.points, 'to_alipay_dict'):
                params['points'] = self.points.to_alipay_dict()
            else:
                params['points'] = self.points
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Fence()
        if 'grid_id' in d:
            o.grid_id = d['grid_id']
        if 'hex_id' in d:
            o.hex_id = d['hex_id']
        if 'his_order' in d:
            o.his_order = d['his_order']
        if 'order_count' in d:
            o.order_count = d['order_count']
        if 'points' in d:
            o.points = d['points']
        if 'rank' in d:
            o.rank = d['rank']
        return o


