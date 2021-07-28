#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessMallPointsNotifyModel(object):

    def __init__(self):
        self._buyer_id = None
        self._earn_points = None
        self._no_points_remarks = None
        self._obtain_points = None
        self._points_update_time = None
        self._total_points = None
        self._trade_no = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def earn_points(self):
        return self._earn_points

    @earn_points.setter
    def earn_points(self, value):
        self._earn_points = value
    @property
    def no_points_remarks(self):
        return self._no_points_remarks

    @no_points_remarks.setter
    def no_points_remarks(self, value):
        self._no_points_remarks = value
    @property
    def obtain_points(self):
        return self._obtain_points

    @obtain_points.setter
    def obtain_points(self, value):
        self._obtain_points = value
    @property
    def points_update_time(self):
        return self._points_update_time

    @points_update_time.setter
    def points_update_time(self, value):
        self._points_update_time = value
    @property
    def total_points(self):
        return self._total_points

    @total_points.setter
    def total_points(self, value):
        self._total_points = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.earn_points:
            if hasattr(self.earn_points, 'to_alipay_dict'):
                params['earn_points'] = self.earn_points.to_alipay_dict()
            else:
                params['earn_points'] = self.earn_points
        if self.no_points_remarks:
            if hasattr(self.no_points_remarks, 'to_alipay_dict'):
                params['no_points_remarks'] = self.no_points_remarks.to_alipay_dict()
            else:
                params['no_points_remarks'] = self.no_points_remarks
        if self.obtain_points:
            if hasattr(self.obtain_points, 'to_alipay_dict'):
                params['obtain_points'] = self.obtain_points.to_alipay_dict()
            else:
                params['obtain_points'] = self.obtain_points
        if self.points_update_time:
            if hasattr(self.points_update_time, 'to_alipay_dict'):
                params['points_update_time'] = self.points_update_time.to_alipay_dict()
            else:
                params['points_update_time'] = self.points_update_time
        if self.total_points:
            if hasattr(self.total_points, 'to_alipay_dict'):
                params['total_points'] = self.total_points.to_alipay_dict()
            else:
                params['total_points'] = self.total_points
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessMallPointsNotifyModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'earn_points' in d:
            o.earn_points = d['earn_points']
        if 'no_points_remarks' in d:
            o.no_points_remarks = d['no_points_remarks']
        if 'obtain_points' in d:
            o.obtain_points = d['obtain_points']
        if 'points_update_time' in d:
            o.points_update_time = d['points_update_time']
        if 'total_points' in d:
            o.total_points = d['total_points']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


