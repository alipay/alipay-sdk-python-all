#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUserpagequeryQueryModel(object):

    def __init__(self):
        self._busvc_id = None
        self._clv_user_ids = None
        self._employee_type_code = None
        self._name = None
        self._org_node_id = None
        self._page_no = None
        self._page_size = None
        self._query_ref_account = None
        self._query_role = None
        self._skill_group_id = None
        self._tnt_inst_id = None

    @property
    def busvc_id(self):
        return self._busvc_id

    @busvc_id.setter
    def busvc_id(self, value):
        self._busvc_id = value
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
    def employee_type_code(self):
        return self._employee_type_code

    @employee_type_code.setter
    def employee_type_code(self, value):
        self._employee_type_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def org_node_id(self):
        return self._org_node_id

    @org_node_id.setter
    def org_node_id(self, value):
        self._org_node_id = value
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
    def query_ref_account(self):
        return self._query_ref_account

    @query_ref_account.setter
    def query_ref_account(self, value):
        self._query_ref_account = value
    @property
    def query_role(self):
        return self._query_role

    @query_role.setter
    def query_role(self, value):
        self._query_role = value
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
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
        if self.employee_type_code:
            if hasattr(self.employee_type_code, 'to_alipay_dict'):
                params['employee_type_code'] = self.employee_type_code.to_alipay_dict()
            else:
                params['employee_type_code'] = self.employee_type_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.org_node_id:
            if hasattr(self.org_node_id, 'to_alipay_dict'):
                params['org_node_id'] = self.org_node_id.to_alipay_dict()
            else:
                params['org_node_id'] = self.org_node_id
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
        if self.query_ref_account:
            if hasattr(self.query_ref_account, 'to_alipay_dict'):
                params['query_ref_account'] = self.query_ref_account.to_alipay_dict()
            else:
                params['query_ref_account'] = self.query_ref_account
        if self.query_role:
            if hasattr(self.query_role, 'to_alipay_dict'):
                params['query_role'] = self.query_role.to_alipay_dict()
            else:
                params['query_role'] = self.query_role
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
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
        o = AlipayIserviceIsresourceUserpagequeryQueryModel()
        if 'busvc_id' in d:
            o.busvc_id = d['busvc_id']
        if 'clv_user_ids' in d:
            o.clv_user_ids = d['clv_user_ids']
        if 'employee_type_code' in d:
            o.employee_type_code = d['employee_type_code']
        if 'name' in d:
            o.name = d['name']
        if 'org_node_id' in d:
            o.org_node_id = d['org_node_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_ref_account' in d:
            o.query_ref_account = d['query_ref_account']
        if 'query_role' in d:
            o.query_role = d['query_role']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


