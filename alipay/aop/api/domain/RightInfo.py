#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RightInfo(object):

    def __init__(self):
        self._fulfillment_type = None
        self._remaining_times = None
        self._right_subtitle = None
        self._right_title = None
        self._sku_code = None
        self._total_times = None

    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def remaining_times(self):
        return self._remaining_times

    @remaining_times.setter
    def remaining_times(self, value):
        self._remaining_times = value
    @property
    def right_subtitle(self):
        return self._right_subtitle

    @right_subtitle.setter
    def right_subtitle(self, value):
        self._right_subtitle = value
    @property
    def right_title(self):
        return self._right_title

    @right_title.setter
    def right_title(self, value):
        self._right_title = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def total_times(self):
        return self._total_times

    @total_times.setter
    def total_times(self, value):
        self._total_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_type:
            if hasattr(self.fulfillment_type, 'to_alipay_dict'):
                params['fulfillment_type'] = self.fulfillment_type.to_alipay_dict()
            else:
                params['fulfillment_type'] = self.fulfillment_type
        if self.remaining_times:
            if hasattr(self.remaining_times, 'to_alipay_dict'):
                params['remaining_times'] = self.remaining_times.to_alipay_dict()
            else:
                params['remaining_times'] = self.remaining_times
        if self.right_subtitle:
            if hasattr(self.right_subtitle, 'to_alipay_dict'):
                params['right_subtitle'] = self.right_subtitle.to_alipay_dict()
            else:
                params['right_subtitle'] = self.right_subtitle
        if self.right_title:
            if hasattr(self.right_title, 'to_alipay_dict'):
                params['right_title'] = self.right_title.to_alipay_dict()
            else:
                params['right_title'] = self.right_title
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.total_times:
            if hasattr(self.total_times, 'to_alipay_dict'):
                params['total_times'] = self.total_times.to_alipay_dict()
            else:
                params['total_times'] = self.total_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RightInfo()
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'remaining_times' in d:
            o.remaining_times = d['remaining_times']
        if 'right_subtitle' in d:
            o.right_subtitle = d['right_subtitle']
        if 'right_title' in d:
            o.right_title = d['right_title']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'total_times' in d:
            o.total_times = d['total_times']
        return o


