#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrganizationContractDTO import OrganizationContractDTO


class UserSubOrganizationDTO(object):

    def __init__(self):
        self._id = None
        self._org_contract_list = None
        self._org_id = None
        self._org_name = None
        self._role_type = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def org_contract_list(self):
        return self._org_contract_list

    @org_contract_list.setter
    def org_contract_list(self, value):
        if isinstance(value, list):
            self._org_contract_list = list()
            for i in value:
                if isinstance(i, OrganizationContractDTO):
                    self._org_contract_list.append(i)
                else:
                    self._org_contract_list.append(OrganizationContractDTO.from_alipay_dict(i))
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.org_contract_list:
            if isinstance(self.org_contract_list, list):
                for i in range(0, len(self.org_contract_list)):
                    element = self.org_contract_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.org_contract_list[i] = element.to_alipay_dict()
            if hasattr(self.org_contract_list, 'to_alipay_dict'):
                params['org_contract_list'] = self.org_contract_list.to_alipay_dict()
            else:
                params['org_contract_list'] = self.org_contract_list
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserSubOrganizationDTO()
        if 'id' in d:
            o.id = d['id']
        if 'org_contract_list' in d:
            o.org_contract_list = d['org_contract_list']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'role_type' in d:
            o.role_type = d['role_type']
        return o


