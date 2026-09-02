#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductSyncItem import ProductSyncItem


class ActivitySyncItem(object):

    def __init__(self):
        self._activity_batch_id = None
        self._activity_description = None
        self._activity_end_time = None
        self._activity_name = None
        self._activity_slogan = None
        self._activity_start_time = None
        self._activity_type = None
        self._merchant_activity_id = None
        self._products = None
        self._source_channel_code = None
        self._source_channel_name = None
        self._source_logo = None

    @property
    def activity_batch_id(self):
        return self._activity_batch_id

    @activity_batch_id.setter
    def activity_batch_id(self, value):
        self._activity_batch_id = value
    @property
    def activity_description(self):
        return self._activity_description

    @activity_description.setter
    def activity_description(self, value):
        self._activity_description = value
    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_slogan(self):
        return self._activity_slogan

    @activity_slogan.setter
    def activity_slogan(self, value):
        self._activity_slogan = value
    @property
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def merchant_activity_id(self):
        return self._merchant_activity_id

    @merchant_activity_id.setter
    def merchant_activity_id(self, value):
        self._merchant_activity_id = value
    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = list()
            for i in value:
                if isinstance(i, ProductSyncItem):
                    self._products.append(i)
                else:
                    self._products.append(ProductSyncItem.from_alipay_dict(i))
    @property
    def source_channel_code(self):
        return self._source_channel_code

    @source_channel_code.setter
    def source_channel_code(self, value):
        self._source_channel_code = value
    @property
    def source_channel_name(self):
        return self._source_channel_name

    @source_channel_name.setter
    def source_channel_name(self, value):
        self._source_channel_name = value
    @property
    def source_logo(self):
        return self._source_logo

    @source_logo.setter
    def source_logo(self, value):
        self._source_logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_batch_id:
            if hasattr(self.activity_batch_id, 'to_alipay_dict'):
                params['activity_batch_id'] = self.activity_batch_id.to_alipay_dict()
            else:
                params['activity_batch_id'] = self.activity_batch_id
        if self.activity_description:
            if hasattr(self.activity_description, 'to_alipay_dict'):
                params['activity_description'] = self.activity_description.to_alipay_dict()
            else:
                params['activity_description'] = self.activity_description
        if self.activity_end_time:
            if hasattr(self.activity_end_time, 'to_alipay_dict'):
                params['activity_end_time'] = self.activity_end_time.to_alipay_dict()
            else:
                params['activity_end_time'] = self.activity_end_time
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_slogan:
            if hasattr(self.activity_slogan, 'to_alipay_dict'):
                params['activity_slogan'] = self.activity_slogan.to_alipay_dict()
            else:
                params['activity_slogan'] = self.activity_slogan
        if self.activity_start_time:
            if hasattr(self.activity_start_time, 'to_alipay_dict'):
                params['activity_start_time'] = self.activity_start_time.to_alipay_dict()
            else:
                params['activity_start_time'] = self.activity_start_time
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.merchant_activity_id:
            if hasattr(self.merchant_activity_id, 'to_alipay_dict'):
                params['merchant_activity_id'] = self.merchant_activity_id.to_alipay_dict()
            else:
                params['merchant_activity_id'] = self.merchant_activity_id
        if self.products:
            if isinstance(self.products, list):
                for i in range(0, len(self.products)):
                    element = self.products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.products[i] = element.to_alipay_dict()
            if hasattr(self.products, 'to_alipay_dict'):
                params['products'] = self.products.to_alipay_dict()
            else:
                params['products'] = self.products
        if self.source_channel_code:
            if hasattr(self.source_channel_code, 'to_alipay_dict'):
                params['source_channel_code'] = self.source_channel_code.to_alipay_dict()
            else:
                params['source_channel_code'] = self.source_channel_code
        if self.source_channel_name:
            if hasattr(self.source_channel_name, 'to_alipay_dict'):
                params['source_channel_name'] = self.source_channel_name.to_alipay_dict()
            else:
                params['source_channel_name'] = self.source_channel_name
        if self.source_logo:
            if hasattr(self.source_logo, 'to_alipay_dict'):
                params['source_logo'] = self.source_logo.to_alipay_dict()
            else:
                params['source_logo'] = self.source_logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivitySyncItem()
        if 'activity_batch_id' in d:
            o.activity_batch_id = d['activity_batch_id']
        if 'activity_description' in d:
            o.activity_description = d['activity_description']
        if 'activity_end_time' in d:
            o.activity_end_time = d['activity_end_time']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_slogan' in d:
            o.activity_slogan = d['activity_slogan']
        if 'activity_start_time' in d:
            o.activity_start_time = d['activity_start_time']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'merchant_activity_id' in d:
            o.merchant_activity_id = d['merchant_activity_id']
        if 'products' in d:
            o.products = d['products']
        if 'source_channel_code' in d:
            o.source_channel_code = d['source_channel_code']
        if 'source_channel_name' in d:
            o.source_channel_name = d['source_channel_name']
        if 'source_logo' in d:
            o.source_logo = d['source_logo']
        return o


