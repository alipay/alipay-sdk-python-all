#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantNetworkLeafnodeCreateModel(object):

    def __init__(self):
        self._biz_info = None
        self._merchant_leafnode_id = None
        self._merchant_leafnode_name = None
        self._network_type = None
        self._parent_merchant_node_id = None
        self._root_id = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def merchant_leafnode_id(self):
        return self._merchant_leafnode_id

    @merchant_leafnode_id.setter
    def merchant_leafnode_id(self, value):
        self._merchant_leafnode_id = value
    @property
    def merchant_leafnode_name(self):
        return self._merchant_leafnode_name

    @merchant_leafnode_name.setter
    def merchant_leafnode_name(self, value):
        self._merchant_leafnode_name = value
    @property
    def network_type(self):
        return self._network_type

    @network_type.setter
    def network_type(self, value):
        self._network_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.merchant_leafnode_id:
            if hasattr(self.merchant_leafnode_id, 'to_alipay_dict'):
                params['merchant_leafnode_id'] = self.merchant_leafnode_id.to_alipay_dict()
            else:
                params['merchant_leafnode_id'] = self.merchant_leafnode_id
        if self.merchant_leafnode_name:
            if hasattr(self.merchant_leafnode_name, 'to_alipay_dict'):
                params['merchant_leafnode_name'] = self.merchant_leafnode_name.to_alipay_dict()
            else:
                params['merchant_leafnode_name'] = self.merchant_leafnode_name
        if self.network_type:
            if hasattr(self.network_type, 'to_alipay_dict'):
                params['network_type'] = self.network_type.to_alipay_dict()
            else:
                params['network_type'] = self.network_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantNetworkLeafnodeCreateModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'merchant_leafnode_id' in d:
            o.merchant_leafnode_id = d['merchant_leafnode_id']
        if 'merchant_leafnode_name' in d:
            o.merchant_leafnode_name = d['merchant_leafnode_name']
        if 'network_type' in d:
            o.network_type = d['network_type']
        if 'parent_merchant_node_id' in d:
            o.parent_merchant_node_id = d['parent_merchant_node_id']
        if 'root_id' in d:
            o.root_id = d['root_id']
        return o


