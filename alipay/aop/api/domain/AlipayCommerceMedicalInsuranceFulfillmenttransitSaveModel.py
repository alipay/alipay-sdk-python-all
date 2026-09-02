#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceFulfillmenttransitSaveModel(object):

    def __init__(self):
        self._channel = None
        self._out_unique_biz_no_list = None
        self._product_code = None
        self._product_name = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def out_unique_biz_no_list(self):
        return self._out_unique_biz_no_list

    @out_unique_biz_no_list.setter
    def out_unique_biz_no_list(self, value):
        if isinstance(value, list):
            self._out_unique_biz_no_list = list()
            for i in value:
                self._out_unique_biz_no_list.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.out_unique_biz_no_list:
            if isinstance(self.out_unique_biz_no_list, list):
                for i in range(0, len(self.out_unique_biz_no_list)):
                    element = self.out_unique_biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_unique_biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_unique_biz_no_list, 'to_alipay_dict'):
                params['out_unique_biz_no_list'] = self.out_unique_biz_no_list.to_alipay_dict()
            else:
                params['out_unique_biz_no_list'] = self.out_unique_biz_no_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceFulfillmenttransitSaveModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_unique_biz_no_list' in d:
            o.out_unique_biz_no_list = d['out_unique_biz_no_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


