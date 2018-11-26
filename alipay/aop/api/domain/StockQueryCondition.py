#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Position import Position


class StockQueryCondition(object):

    def __init__(self):
        self._end_date = None
        self._position = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, list):
            self._position = list()
            for i in value:
                if isinstance(i, Position):
                    self._position.append(i)
                else:
                    self._position.append(Position.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.position:
            if isinstance(self.position, list):
                for i in range(0, len(self.position)):
                    element = self.position[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position[i] = element.to_alipay_dict()
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockQueryCondition()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'position' in d:
            o.position = d['position']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


