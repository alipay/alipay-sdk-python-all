#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcTcnInvoiceBatchqueryModel(object):

    def __init__(self):
        self._apply_id = None
        self._page_num = None
        self._page_size = None
        self._platform_apply_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
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
    def platform_apply_id(self):
        return self._platform_apply_id

    @platform_apply_id.setter
    def platform_apply_id(self, value):
        self._platform_apply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
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
        if self.platform_apply_id:
            if hasattr(self.platform_apply_id, 'to_alipay_dict'):
                params['platform_apply_id'] = self.platform_apply_id.to_alipay_dict()
            else:
                params['platform_apply_id'] = self.platform_apply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcTcnInvoiceBatchqueryModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'platform_apply_id' in d:
            o.platform_apply_id = d['platform_apply_id']
        return o


