#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExchangeVoucherValueInfo(object):

    def __init__(self):
        self._change_count = None
        self._product_img_url = None
        self._product_name = None
        self._remain_count = None
        self._total_count = None
        self._used_count = None

    @property
    def change_count(self):
        return self._change_count

    @change_count.setter
    def change_count(self, value):
        self._change_count = value
    @property
    def product_img_url(self):
        return self._product_img_url

    @product_img_url.setter
    def product_img_url(self, value):
        self._product_img_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_count:
            if hasattr(self.change_count, 'to_alipay_dict'):
                params['change_count'] = self.change_count.to_alipay_dict()
            else:
                params['change_count'] = self.change_count
        if self.product_img_url:
            if hasattr(self.product_img_url, 'to_alipay_dict'):
                params['product_img_url'] = self.product_img_url.to_alipay_dict()
            else:
                params['product_img_url'] = self.product_img_url
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExchangeVoucherValueInfo()
        if 'change_count' in d:
            o.change_count = d['change_count']
        if 'product_img_url' in d:
            o.product_img_url = d['product_img_url']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


