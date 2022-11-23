#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfoSecAnalyzeSyncContent(object):

    def __init__(self):
        self._business_id = None
        self._check_labels = None
        self._data = None
        self._data_id = None
        self._product_id = None
        self._publish_time = None
        self._request_id = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def check_labels(self):
        return self._check_labels

    @check_labels.setter
    def check_labels(self, value):
        self._check_labels = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.check_labels:
            if hasattr(self.check_labels, 'to_alipay_dict'):
                params['check_labels'] = self.check_labels.to_alipay_dict()
            else:
                params['check_labels'] = self.check_labels
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfoSecAnalyzeSyncContent()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'check_labels' in d:
            o.check_labels = d['check_labels']
        if 'data' in d:
            o.data = d['data']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


