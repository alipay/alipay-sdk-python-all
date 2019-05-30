#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSupplierAssetBatchqueryModel(object):

    def __init__(self):
        self._cur_page_num = None
        self._keyword = None
        self._page_size = None
        self._supplier_pid = None

    @property
    def cur_page_num(self):
        return self._cur_page_num

    @cur_page_num.setter
    def cur_page_num(self, value):
        self._cur_page_num = value
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def supplier_pid(self):
        return self._supplier_pid

    @supplier_pid.setter
    def supplier_pid(self, value):
        self._supplier_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_page_num:
            if hasattr(self.cur_page_num, 'to_alipay_dict'):
                params['cur_page_num'] = self.cur_page_num.to_alipay_dict()
            else:
                params['cur_page_num'] = self.cur_page_num
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.supplier_pid:
            if hasattr(self.supplier_pid, 'to_alipay_dict'):
                params['supplier_pid'] = self.supplier_pid.to_alipay_dict()
            else:
                params['supplier_pid'] = self.supplier_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSupplierAssetBatchqueryModel()
        if 'cur_page_num' in d:
            o.cur_page_num = d['cur_page_num']
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'supplier_pid' in d:
            o.supplier_pid = d['supplier_pid']
        return o


