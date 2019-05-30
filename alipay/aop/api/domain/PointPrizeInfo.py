#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointPrizeInfo(object):

    def __init__(self):
        self._end_time = None
        self._exchange_point = None
        self._intro = None
        self._pic_url = None
        self._prize_name = None
        self._prize_no = None
        self._prize_type = None
        self._start_time = None
        self._stock = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exchange_point(self):
        return self._exchange_point

    @exchange_point.setter
    def exchange_point(self, value):
        self._exchange_point = value
    @property
    def intro(self):
        return self._intro

    @intro.setter
    def intro(self, value):
        self._intro = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_no(self):
        return self._prize_no

    @prize_no.setter
    def prize_no(self, value):
        self._prize_no = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.exchange_point:
            if hasattr(self.exchange_point, 'to_alipay_dict'):
                params['exchange_point'] = self.exchange_point.to_alipay_dict()
            else:
                params['exchange_point'] = self.exchange_point
        if self.intro:
            if hasattr(self.intro, 'to_alipay_dict'):
                params['intro'] = self.intro.to_alipay_dict()
            else:
                params['intro'] = self.intro
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_no:
            if hasattr(self.prize_no, 'to_alipay_dict'):
                params['prize_no'] = self.prize_no.to_alipay_dict()
            else:
                params['prize_no'] = self.prize_no
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.stock:
            if hasattr(self.stock, 'to_alipay_dict'):
                params['stock'] = self.stock.to_alipay_dict()
            else:
                params['stock'] = self.stock
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointPrizeInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exchange_point' in d:
            o.exchange_point = d['exchange_point']
        if 'intro' in d:
            o.intro = d['intro']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_no' in d:
            o.prize_no = d['prize_no']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stock' in d:
            o.stock = d['stock']
        return o


