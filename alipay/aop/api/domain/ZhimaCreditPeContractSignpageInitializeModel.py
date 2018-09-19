#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeContractSignpageInitializeModel(object):

    def __init__(self):
        self._activity_name = None
        self._callback_url = None
        self._category = None
        self._source = None
        self._uid = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeContractSignpageInitializeModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'category' in d:
            o.category = d['category']
        if 'source' in d:
            o.source = d['source']
        if 'uid' in d:
            o.uid = d['uid']
        return o


