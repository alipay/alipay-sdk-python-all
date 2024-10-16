#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarQuoteadvQueryModel(object):

    def __init__(self):
        self._page_no = None
        self._page_size = None
        self._sku_id = None
        self._sku_sname = None
        self._start_city_name = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_sname(self):
        return self._sku_sname

    @sku_sname.setter
    def sku_sname(self, value):
        self._sku_sname = value
    @property
    def start_city_name(self):
        return self._start_city_name

    @start_city_name.setter
    def start_city_name(self, value):
        self._start_city_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_sname:
            if hasattr(self.sku_sname, 'to_alipay_dict'):
                params['sku_sname'] = self.sku_sname.to_alipay_dict()
            else:
                params['sku_sname'] = self.sku_sname
        if self.start_city_name:
            if hasattr(self.start_city_name, 'to_alipay_dict'):
                params['start_city_name'] = self.start_city_name.to_alipay_dict()
            else:
                params['start_city_name'] = self.start_city_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarQuoteadvQueryModel()
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_sname' in d:
            o.sku_sname = d['sku_sname']
        if 'start_city_name' in d:
            o.start_city_name = d['start_city_name']
        return o


