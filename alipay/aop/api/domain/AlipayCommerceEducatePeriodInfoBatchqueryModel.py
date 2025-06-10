#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducatePeriodInfoBatchqueryModel(object):

    def __init__(self):
        self._inst_id = None
        self._page_num = None
        self._page_size = None
        self._period_id = None
        self._period_name = None

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
    def period_id(self):
        return self._period_id

    @period_id.setter
    def period_id(self, value):
        self._period_id = value
    @property
    def period_name(self):
        return self._period_name

    @period_name.setter
    def period_name(self, value):
        self._period_name = value


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
        if self.period_id:
            if hasattr(self.period_id, 'to_alipay_dict'):
                params['period_id'] = self.period_id.to_alipay_dict()
            else:
                params['period_id'] = self.period_id
        if self.period_name:
            if hasattr(self.period_name, 'to_alipay_dict'):
                params['period_name'] = self.period_name.to_alipay_dict()
            else:
                params['period_name'] = self.period_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducatePeriodInfoBatchqueryModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'period_id' in d:
            o.period_id = d['period_id']
        if 'period_name' in d:
            o.period_name = d['period_name']
        return o


