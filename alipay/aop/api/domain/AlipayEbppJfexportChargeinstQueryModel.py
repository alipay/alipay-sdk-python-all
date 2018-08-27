#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJfexportChargeinstQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._extend_field = None
        self._page = None
        self._page_query = None
        self._page_size = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_query(self):
        return self._page_query

    @page_query.setter
    def page_query(self, value):
        self._page_query = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_query:
            if hasattr(self.page_query, 'to_alipay_dict'):
                params['page_query'] = self.page_query.to_alipay_dict()
            else:
                params['page_query'] = self.page_query
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJfexportChargeinstQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'page' in d:
            o.page = d['page']
        if 'page_query' in d:
            o.page_query = d['page_query']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


