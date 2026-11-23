#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailCashbackrelationBatchqueryModel(object):

    def __init__(self):
        self._delivery_plan_id = None
        self._page_no = None
        self._page_size = None

    @property
    def delivery_plan_id(self):
        return self._delivery_plan_id

    @delivery_plan_id.setter
    def delivery_plan_id(self, value):
        self._delivery_plan_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_plan_id:
            if hasattr(self.delivery_plan_id, 'to_alipay_dict'):
                params['delivery_plan_id'] = self.delivery_plan_id.to_alipay_dict()
            else:
                params['delivery_plan_id'] = self.delivery_plan_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackrelationBatchqueryModel()
        if 'delivery_plan_id' in d:
            o.delivery_plan_id = d['delivery_plan_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


