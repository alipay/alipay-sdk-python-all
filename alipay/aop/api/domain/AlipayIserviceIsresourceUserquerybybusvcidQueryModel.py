#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUserquerybybusvcidQueryModel(object):

    def __init__(self):
        self._busvc_id = None
        self._query_org_node = None
        self._query_role = None
        self._query_user_resource = None
        self._tnt_inst_id = None

    @property
    def busvc_id(self):
        return self._busvc_id

    @busvc_id.setter
    def busvc_id(self, value):
        self._busvc_id = value
    @property
    def query_org_node(self):
        return self._query_org_node

    @query_org_node.setter
    def query_org_node(self, value):
        self._query_org_node = value
    @property
    def query_role(self):
        return self._query_role

    @query_role.setter
    def query_role(self, value):
        self._query_role = value
    @property
    def query_user_resource(self):
        return self._query_user_resource

    @query_user_resource.setter
    def query_user_resource(self, value):
        self._query_user_resource = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.busvc_id:
            if hasattr(self.busvc_id, 'to_alipay_dict'):
                params['busvc_id'] = self.busvc_id.to_alipay_dict()
            else:
                params['busvc_id'] = self.busvc_id
        if self.query_org_node:
            if hasattr(self.query_org_node, 'to_alipay_dict'):
                params['query_org_node'] = self.query_org_node.to_alipay_dict()
            else:
                params['query_org_node'] = self.query_org_node
        if self.query_role:
            if hasattr(self.query_role, 'to_alipay_dict'):
                params['query_role'] = self.query_role.to_alipay_dict()
            else:
                params['query_role'] = self.query_role
        if self.query_user_resource:
            if hasattr(self.query_user_resource, 'to_alipay_dict'):
                params['query_user_resource'] = self.query_user_resource.to_alipay_dict()
            else:
                params['query_user_resource'] = self.query_user_resource
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
        o = AlipayIserviceIsresourceUserquerybybusvcidQueryModel()
        if 'busvc_id' in d:
            o.busvc_id = d['busvc_id']
        if 'query_org_node' in d:
            o.query_org_node = d['query_org_node']
        if 'query_role' in d:
            o.query_role = d['query_role']
        if 'query_user_resource' in d:
            o.query_user_resource = d['query_user_resource']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


