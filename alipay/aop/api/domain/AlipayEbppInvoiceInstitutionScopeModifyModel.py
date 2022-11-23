#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceInstitutionScopeModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._adapter_type = None
        self._add_owner_id_list = None
        self._add_owner_open_id_list = None
        self._agreement_no = None
        self._enterprise_id = None
        self._institution_id = None
        self._owner_type = None
        self._remove_owner_id_list = None
        self._remove_owner_open_id_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def add_owner_id_list(self):
        return self._add_owner_id_list

    @add_owner_id_list.setter
    def add_owner_id_list(self, value):
        if isinstance(value, list):
            self._add_owner_id_list = list()
            for i in value:
                self._add_owner_id_list.append(i)
    @property
    def add_owner_open_id_list(self):
        return self._add_owner_open_id_list

    @add_owner_open_id_list.setter
    def add_owner_open_id_list(self, value):
        if isinstance(value, list):
            self._add_owner_open_id_list = list()
            for i in value:
                self._add_owner_open_id_list.append(i)
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def remove_owner_id_list(self):
        return self._remove_owner_id_list

    @remove_owner_id_list.setter
    def remove_owner_id_list(self, value):
        if isinstance(value, list):
            self._remove_owner_id_list = list()
            for i in value:
                self._remove_owner_id_list.append(i)
    @property
    def remove_owner_open_id_list(self):
        return self._remove_owner_open_id_list

    @remove_owner_open_id_list.setter
    def remove_owner_open_id_list(self, value):
        if isinstance(value, list):
            self._remove_owner_open_id_list = list()
            for i in value:
                self._remove_owner_open_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.adapter_type:
            if hasattr(self.adapter_type, 'to_alipay_dict'):
                params['adapter_type'] = self.adapter_type.to_alipay_dict()
            else:
                params['adapter_type'] = self.adapter_type
        if self.add_owner_id_list:
            if isinstance(self.add_owner_id_list, list):
                for i in range(0, len(self.add_owner_id_list)):
                    element = self.add_owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.add_owner_id_list, 'to_alipay_dict'):
                params['add_owner_id_list'] = self.add_owner_id_list.to_alipay_dict()
            else:
                params['add_owner_id_list'] = self.add_owner_id_list
        if self.add_owner_open_id_list:
            if isinstance(self.add_owner_open_id_list, list):
                for i in range(0, len(self.add_owner_open_id_list)):
                    element = self.add_owner_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_owner_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.add_owner_open_id_list, 'to_alipay_dict'):
                params['add_owner_open_id_list'] = self.add_owner_open_id_list.to_alipay_dict()
            else:
                params['add_owner_open_id_list'] = self.add_owner_open_id_list
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.remove_owner_id_list:
            if isinstance(self.remove_owner_id_list, list):
                for i in range(0, len(self.remove_owner_id_list)):
                    element = self.remove_owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.remove_owner_id_list, 'to_alipay_dict'):
                params['remove_owner_id_list'] = self.remove_owner_id_list.to_alipay_dict()
            else:
                params['remove_owner_id_list'] = self.remove_owner_id_list
        if self.remove_owner_open_id_list:
            if isinstance(self.remove_owner_open_id_list, list):
                for i in range(0, len(self.remove_owner_open_id_list)):
                    element = self.remove_owner_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_owner_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.remove_owner_open_id_list, 'to_alipay_dict'):
                params['remove_owner_open_id_list'] = self.remove_owner_open_id_list.to_alipay_dict()
            else:
                params['remove_owner_open_id_list'] = self.remove_owner_open_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceInstitutionScopeModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'adapter_type' in d:
            o.adapter_type = d['adapter_type']
        if 'add_owner_id_list' in d:
            o.add_owner_id_list = d['add_owner_id_list']
        if 'add_owner_open_id_list' in d:
            o.add_owner_open_id_list = d['add_owner_open_id_list']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'remove_owner_id_list' in d:
            o.remove_owner_id_list = d['remove_owner_id_list']
        if 'remove_owner_open_id_list' in d:
            o.remove_owner_open_id_list = d['remove_owner_open_id_list']
        return o


