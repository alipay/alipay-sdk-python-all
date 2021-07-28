#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniResourcePromotionsourceNotifyModel(object):

    def __init__(self):
        self._author_id = None
        self._params = None
        self._promotion_id = None
        self._promotion_name = None
        self._source = None

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        self._author_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def promotion_id(self):
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, value):
        self._promotion_id = value
    @property
    def promotion_name(self):
        return self._promotion_name

    @promotion_name.setter
    def promotion_name(self, value):
        self._promotion_name = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.author_id:
            if hasattr(self.author_id, 'to_alipay_dict'):
                params['author_id'] = self.author_id.to_alipay_dict()
            else:
                params['author_id'] = self.author_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.promotion_id:
            if hasattr(self.promotion_id, 'to_alipay_dict'):
                params['promotion_id'] = self.promotion_id.to_alipay_dict()
            else:
                params['promotion_id'] = self.promotion_id
        if self.promotion_name:
            if hasattr(self.promotion_name, 'to_alipay_dict'):
                params['promotion_name'] = self.promotion_name.to_alipay_dict()
            else:
                params['promotion_name'] = self.promotion_name
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourcePromotionsourceNotifyModel()
        if 'author_id' in d:
            o.author_id = d['author_id']
        if 'params' in d:
            o.params = d['params']
        if 'promotion_id' in d:
            o.promotion_id = d['promotion_id']
        if 'promotion_name' in d:
            o.promotion_name = d['promotion_name']
        if 'source' in d:
            o.source = d['source']
        return o


