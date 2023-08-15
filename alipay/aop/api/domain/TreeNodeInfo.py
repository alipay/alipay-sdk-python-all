#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TreeNodeInfo(object):

    def __init__(self):
        self._biz_info = None
        self._merchant_node_id = None
        self._merchant_node_name = None
        self._node_biz_type = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def merchant_node_id(self):
        return self._merchant_node_id

    @merchant_node_id.setter
    def merchant_node_id(self, value):
        self._merchant_node_id = value
    @property
    def merchant_node_name(self):
        return self._merchant_node_name

    @merchant_node_name.setter
    def merchant_node_name(self, value):
        self._merchant_node_name = value
    @property
    def node_biz_type(self):
        return self._node_biz_type

    @node_biz_type.setter
    def node_biz_type(self, value):
        self._node_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.merchant_node_id:
            if hasattr(self.merchant_node_id, 'to_alipay_dict'):
                params['merchant_node_id'] = self.merchant_node_id.to_alipay_dict()
            else:
                params['merchant_node_id'] = self.merchant_node_id
        if self.merchant_node_name:
            if hasattr(self.merchant_node_name, 'to_alipay_dict'):
                params['merchant_node_name'] = self.merchant_node_name.to_alipay_dict()
            else:
                params['merchant_node_name'] = self.merchant_node_name
        if self.node_biz_type:
            if hasattr(self.node_biz_type, 'to_alipay_dict'):
                params['node_biz_type'] = self.node_biz_type.to_alipay_dict()
            else:
                params['node_biz_type'] = self.node_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreeNodeInfo()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'merchant_node_id' in d:
            o.merchant_node_id = d['merchant_node_id']
        if 'merchant_node_name' in d:
            o.merchant_node_name = d['merchant_node_name']
        if 'node_biz_type' in d:
            o.node_biz_type = d['node_biz_type']
        return o


