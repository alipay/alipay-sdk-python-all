#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketShopSummaryBatchqueryModel(object):

    def __init__(self):
        self._op_role = None
        self._page_no = None
        self._page_size = None
        self._query_type = None
        self._related_partner_id = None
        self._shop_id = None
        self._shop_status = None

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
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def related_partner_id(self):
        return self._related_partner_id

    @related_partner_id.setter
    def related_partner_id(self, value):
        self._related_partner_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value


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
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.related_partner_id:
            if hasattr(self.related_partner_id, 'to_alipay_dict'):
                params['related_partner_id'] = self.related_partner_id.to_alipay_dict()
            else:
                params['related_partner_id'] = self.related_partner_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketShopSummaryBatchqueryModel()
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'related_partner_id' in d:
            o.related_partner_id = d['related_partner_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        return o


