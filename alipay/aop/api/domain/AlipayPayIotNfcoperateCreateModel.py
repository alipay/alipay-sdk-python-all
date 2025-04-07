#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayIotNfcoperateCreateModel(object):

    def __init__(self):
        self._device_ids = None
        self._end_time = None
        self._img_url = None
        self._merchant_id = None
        self._operator = None
        self._poster_name = None
        self._start_time = None

    @property
    def device_ids(self):
        return self._device_ids

    @device_ids.setter
    def device_ids(self, value):
        if isinstance(value, list):
            self._device_ids = list()
            for i in value:
                self._device_ids.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def poster_name(self):
        return self._poster_name

    @poster_name.setter
    def poster_name(self, value):
        self._poster_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_ids:
            if isinstance(self.device_ids, list):
                for i in range(0, len(self.device_ids)):
                    element = self.device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_ids[i] = element.to_alipay_dict()
            if hasattr(self.device_ids, 'to_alipay_dict'):
                params['device_ids'] = self.device_ids.to_alipay_dict()
            else:
                params['device_ids'] = self.device_ids
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.poster_name:
            if hasattr(self.poster_name, 'to_alipay_dict'):
                params['poster_name'] = self.poster_name.to_alipay_dict()
            else:
                params['poster_name'] = self.poster_name
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
        o = AlipayPayIotNfcoperateCreateModel()
        if 'device_ids' in d:
            o.device_ids = d['device_ids']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'poster_name' in d:
            o.poster_name = d['poster_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


