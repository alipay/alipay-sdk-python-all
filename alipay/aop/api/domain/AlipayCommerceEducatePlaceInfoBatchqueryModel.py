#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducatePlaceInfoBatchqueryModel(object):

    def __init__(self):
        self._inst_id = None
        self._page_num = None
        self._page_size = None
        self._parent_id = None
        self._place_label = None
        self._place_name = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def place_label(self):
        return self._place_label

    @place_label.setter
    def place_label(self, value):
        self._place_label = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.place_label:
            if hasattr(self.place_label, 'to_alipay_dict'):
                params['place_label'] = self.place_label.to_alipay_dict()
            else:
                params['place_label'] = self.place_label
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducatePlaceInfoBatchqueryModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'place_label' in d:
            o.place_label = d['place_label']
        if 'place_name' in d:
            o.place_name = d['place_name']
        return o


