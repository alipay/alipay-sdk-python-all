#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CatalogNodeData(object):

    def __init__(self):
        self._node_id = None
        self._node_nm = None

    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def node_nm(self):
        return self._node_nm

    @node_nm.setter
    def node_nm(self, value):
        self._node_nm = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.node_nm:
            if hasattr(self.node_nm, 'to_alipay_dict'):
                params['node_nm'] = self.node_nm.to_alipay_dict()
            else:
                params['node_nm'] = self.node_nm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CatalogNodeData()
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'node_nm' in d:
            o.node_nm = d['node_nm']
        return o


