#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantNetworkNodeBatchqueryModel(object):

    def __init__(self):
        self._network_type = None
        self._page_size = None
        self._parent_merchant_node_id = None
        self._root_id = None
        self._start_row = None

    @property
    def network_type(self):
        return self._network_type

    @network_type.setter
    def network_type(self, value):
        self._network_type = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def parent_merchant_node_id(self):
        return self._parent_merchant_node_id

    @parent_merchant_node_id.setter
    def parent_merchant_node_id(self, value):
        self._parent_merchant_node_id = value
    @property
    def root_id(self):
        return self._root_id

    @root_id.setter
    def root_id(self, value):
        self._root_id = value
    @property
    def start_row(self):
        return self._start_row

    @start_row.setter
    def start_row(self, value):
        self._start_row = value


    def to_alipay_dict(self):
        params = dict()
        if self.network_type:
            if hasattr(self.network_type, 'to_alipay_dict'):
                params['network_type'] = self.network_type.to_alipay_dict()
            else:
                params['network_type'] = self.network_type
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.parent_merchant_node_id:
            if hasattr(self.parent_merchant_node_id, 'to_alipay_dict'):
                params['parent_merchant_node_id'] = self.parent_merchant_node_id.to_alipay_dict()
            else:
                params['parent_merchant_node_id'] = self.parent_merchant_node_id
        if self.root_id:
            if hasattr(self.root_id, 'to_alipay_dict'):
                params['root_id'] = self.root_id.to_alipay_dict()
            else:
                params['root_id'] = self.root_id
        if self.start_row:
            if hasattr(self.start_row, 'to_alipay_dict'):
                params['start_row'] = self.start_row.to_alipay_dict()
            else:
                params['start_row'] = self.start_row
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantNetworkNodeBatchqueryModel()
        if 'network_type' in d:
            o.network_type = d['network_type']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'parent_merchant_node_id' in d:
            o.parent_merchant_node_id = d['parent_merchant_node_id']
        if 'root_id' in d:
            o.root_id = d['root_id']
        if 'start_row' in d:
            o.start_row = d['start_row']
        return o


