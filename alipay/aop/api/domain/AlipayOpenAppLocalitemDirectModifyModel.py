#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO
from alipay.aop.api.domain.LocalItemDirectModifySku import LocalItemDirectModifySku
from alipay.aop.api.domain.TimeRangeStructVO import TimeRangeStructVO


class AlipayOpenAppLocalitemDirectModifyModel(object):

    def __init__(self):
        self._attrs = None
        self._item_id = None
        self._out_item_id = None
        self._skus = None
        self._sold_time = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, AppItemAttrVO):
                    self._attrs.append(i)
                else:
                    self._attrs.append(AppItemAttrVO.from_alipay_dict(i))
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LocalItemDirectModifySku):
                    self._skus.append(i)
                else:
                    self._skus.append(LocalItemDirectModifySku.from_alipay_dict(i))
    @property
    def sold_time(self):
        return self._sold_time

    @sold_time.setter
    def sold_time(self, value):
        if isinstance(value, TimeRangeStructVO):
            self._sold_time = value
        else:
            self._sold_time = TimeRangeStructVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.sold_time:
            if hasattr(self.sold_time, 'to_alipay_dict'):
                params['sold_time'] = self.sold_time.to_alipay_dict()
            else:
                params['sold_time'] = self.sold_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppLocalitemDirectModifyModel()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'skus' in d:
            o.skus = d['skus']
        if 'sold_time' in d:
            o.sold_time = d['sold_time']
        return o


