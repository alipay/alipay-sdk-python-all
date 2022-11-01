#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataInteractiverecordListQueryModel(object):

    def __init__(self):
        self._current_page = None
        self._filter_params = None
        self._page_size = None
        self._tenant_id = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def filter_params(self):
        return self._filter_params

    @filter_params.setter
    def filter_params(self, value):
        self._filter_params = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.filter_params:
            if hasattr(self.filter_params, 'to_alipay_dict'):
                params['filter_params'] = self.filter_params.to_alipay_dict()
            else:
                params['filter_params'] = self.filter_params
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataInteractiverecordListQueryModel()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'filter_params' in d:
            o.filter_params = d['filter_params']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


