#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceLeafnodequerybyorgidQueryModel(object):

    def __init__(self):
        self._org_node_id = None
        self._tnt_inst_id = None

    @property
    def org_node_id(self):
        return self._org_node_id

    @org_node_id.setter
    def org_node_id(self, value):
        self._org_node_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_node_id:
            if hasattr(self.org_node_id, 'to_alipay_dict'):
                params['org_node_id'] = self.org_node_id.to_alipay_dict()
            else:
                params['org_node_id'] = self.org_node_id
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceLeafnodequerybyorgidQueryModel()
        if 'org_node_id' in d:
            o.org_node_id = d['org_node_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


