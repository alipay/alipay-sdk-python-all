#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointLogInfo(object):

    def __init__(self):
        self._point_log_amount = None
        self._point_log_date = None
        self._point_log_id = None
        self._point_log_title = None

    @property
    def point_log_amount(self):
        return self._point_log_amount

    @point_log_amount.setter
    def point_log_amount(self, value):
        self._point_log_amount = value
    @property
    def point_log_date(self):
        return self._point_log_date

    @point_log_date.setter
    def point_log_date(self, value):
        self._point_log_date = value
    @property
    def point_log_id(self):
        return self._point_log_id

    @point_log_id.setter
    def point_log_id(self, value):
        self._point_log_id = value
    @property
    def point_log_title(self):
        return self._point_log_title

    @point_log_title.setter
    def point_log_title(self, value):
        self._point_log_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.point_log_amount:
            if hasattr(self.point_log_amount, 'to_alipay_dict'):
                params['point_log_amount'] = self.point_log_amount.to_alipay_dict()
            else:
                params['point_log_amount'] = self.point_log_amount
        if self.point_log_date:
            if hasattr(self.point_log_date, 'to_alipay_dict'):
                params['point_log_date'] = self.point_log_date.to_alipay_dict()
            else:
                params['point_log_date'] = self.point_log_date
        if self.point_log_id:
            if hasattr(self.point_log_id, 'to_alipay_dict'):
                params['point_log_id'] = self.point_log_id.to_alipay_dict()
            else:
                params['point_log_id'] = self.point_log_id
        if self.point_log_title:
            if hasattr(self.point_log_title, 'to_alipay_dict'):
                params['point_log_title'] = self.point_log_title.to_alipay_dict()
            else:
                params['point_log_title'] = self.point_log_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointLogInfo()
        if 'point_log_amount' in d:
            o.point_log_amount = d['point_log_amount']
        if 'point_log_date' in d:
            o.point_log_date = d['point_log_date']
        if 'point_log_id' in d:
            o.point_log_id = d['point_log_id']
        if 'point_log_title' in d:
            o.point_log_title = d['point_log_title']
        return o


