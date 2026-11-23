#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailCashbackplanBatchqueryModel(object):

    def __init__(self):
        self._delivery_form = None
        self._page_no = None
        self._page_size = None
        self._search_config = None

    @property
    def delivery_form(self):
        return self._delivery_form

    @delivery_form.setter
    def delivery_form(self, value):
        self._delivery_form = value
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
    def search_config(self):
        return self._search_config

    @search_config.setter
    def search_config(self, value):
        self._search_config = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_form:
            if hasattr(self.delivery_form, 'to_alipay_dict'):
                params['delivery_form'] = self.delivery_form.to_alipay_dict()
            else:
                params['delivery_form'] = self.delivery_form
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
        if self.search_config:
            if hasattr(self.search_config, 'to_alipay_dict'):
                params['search_config'] = self.search_config.to_alipay_dict()
            else:
                params['search_config'] = self.search_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackplanBatchqueryModel()
        if 'delivery_form' in d:
            o.delivery_form = d['delivery_form']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'search_config' in d:
            o.search_config = d['search_config']
        return o


