#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantNetworkLeafnodeDeleteModel(object):

    def __init__(self):
        self._merchant_leafnode_id = None
        self._network_type = None
        self._root_id = None

    @property
    def merchant_leafnode_id(self):
        return self._merchant_leafnode_id

    @merchant_leafnode_id.setter
    def merchant_leafnode_id(self, value):
        self._merchant_leafnode_id = value
    @property
    def network_type(self):
        return self._network_type

    @network_type.setter
    def network_type(self, value):
        self._network_type = value
    @property
    def root_id(self):
        return self._root_id

    @root_id.setter
    def root_id(self, value):
        self._root_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_leafnode_id:
            if hasattr(self.merchant_leafnode_id, 'to_alipay_dict'):
                params['merchant_leafnode_id'] = self.merchant_leafnode_id.to_alipay_dict()
            else:
                params['merchant_leafnode_id'] = self.merchant_leafnode_id
        if self.network_type:
            if hasattr(self.network_type, 'to_alipay_dict'):
                params['network_type'] = self.network_type.to_alipay_dict()
            else:
                params['network_type'] = self.network_type
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
        o = AlipayMerchantNetworkLeafnodeDeleteModel()
        if 'merchant_leafnode_id' in d:
            o.merchant_leafnode_id = d['merchant_leafnode_id']
        if 'network_type' in d:
            o.network_type = d['network_type']
        if 'root_id' in d:
            o.root_id = d['root_id']
        return o


