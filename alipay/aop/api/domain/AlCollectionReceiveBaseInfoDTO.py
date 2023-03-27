#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlCollectionReceiveBaseInfoDTO(object):

    def __init__(self):
        self._collection_title = None
        self._memo = None
        self._order_id = None
        self._source_sys = None
        self._template_id = None

    @property
    def collection_title(self):
        return self._collection_title

    @collection_title.setter
    def collection_title(self, value):
        self._collection_title = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.collection_title:
            if hasattr(self.collection_title, 'to_alipay_dict'):
                params['collection_title'] = self.collection_title.to_alipay_dict()
            else:
                params['collection_title'] = self.collection_title
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlCollectionReceiveBaseInfoDTO()
        if 'collection_title' in d:
            o.collection_title = d['collection_title']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


