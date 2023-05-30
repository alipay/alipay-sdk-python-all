#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUserquerybyclvuidsQueryModel(object):

    def __init__(self):
        self._clv_user_ids = None
        self._query_role = None
        self._query_skill_group = None
        self._query_user_resource = None
        self._tnt_inst_id = None

    @property
    def clv_user_ids(self):
        return self._clv_user_ids

    @clv_user_ids.setter
    def clv_user_ids(self, value):
        if isinstance(value, list):
            self._clv_user_ids = list()
            for i in value:
                self._clv_user_ids.append(i)
    @property
    def query_role(self):
        return self._query_role

    @query_role.setter
    def query_role(self, value):
        self._query_role = value
    @property
    def query_skill_group(self):
        return self._query_skill_group

    @query_skill_group.setter
    def query_skill_group(self, value):
        self._query_skill_group = value
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
        if self.clv_user_ids:
            if isinstance(self.clv_user_ids, list):
                for i in range(0, len(self.clv_user_ids)):
                    element = self.clv_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clv_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.clv_user_ids, 'to_alipay_dict'):
                params['clv_user_ids'] = self.clv_user_ids.to_alipay_dict()
            else:
                params['clv_user_ids'] = self.clv_user_ids
        if self.query_role:
            if hasattr(self.query_role, 'to_alipay_dict'):
                params['query_role'] = self.query_role.to_alipay_dict()
            else:
                params['query_role'] = self.query_role
        if self.query_skill_group:
            if hasattr(self.query_skill_group, 'to_alipay_dict'):
                params['query_skill_group'] = self.query_skill_group.to_alipay_dict()
            else:
                params['query_skill_group'] = self.query_skill_group
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
        o = AlipayIserviceIsresourceUserquerybyclvuidsQueryModel()
        if 'clv_user_ids' in d:
            o.clv_user_ids = d['clv_user_ids']
        if 'query_role' in d:
            o.query_role = d['query_role']
        if 'query_skill_group' in d:
            o.query_skill_group = d['query_skill_group']
        if 'query_user_resource' in d:
            o.query_user_resource = d['query_user_resource']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


