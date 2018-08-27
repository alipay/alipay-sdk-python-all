#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketProductBatchqueryModel(object):

    def __init__(self):
        self._op_role = None
        self._page_no = None
        self._shop_id = None

    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketProductBatchqueryModel()
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


