#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnterpriseOpenRuleRecordInfo import EnterpriseOpenRuleRecordInfo
from alipay.aop.api.domain.EnterpriseOpenRuleRelationInfo import EnterpriseOpenRuleRelationInfo


class EnterpriseOpenRuleInfo(object):

    def __init__(self):
        self._enterprise_open_rule_record_info_list = None
        self._enterprise_open_rule_relation_info_list = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoice_rule_id = None
        self._invoice_rule_name = None
        self._owner_id = None
        self._seller_type = None

    @property
    def enterprise_open_rule_record_info_list(self):
        return self._enterprise_open_rule_record_info_list

    @enterprise_open_rule_record_info_list.setter
    def enterprise_open_rule_record_info_list(self, value):
        if isinstance(value, list):
            self._enterprise_open_rule_record_info_list = list()
            for i in value:
                if isinstance(i, EnterpriseOpenRuleRecordInfo):
                    self._enterprise_open_rule_record_info_list.append(i)
                else:
                    self._enterprise_open_rule_record_info_list.append(EnterpriseOpenRuleRecordInfo.from_alipay_dict(i))
    @property
    def enterprise_open_rule_relation_info_list(self):
        return self._enterprise_open_rule_relation_info_list

    @enterprise_open_rule_relation_info_list.setter
    def enterprise_open_rule_relation_info_list(self, value):
        if isinstance(value, list):
            self._enterprise_open_rule_relation_info_list = list()
            for i in value:
                if isinstance(i, EnterpriseOpenRuleRelationInfo):
                    self._enterprise_open_rule_relation_info_list.append(i)
                else:
                    self._enterprise_open_rule_relation_info_list.append(EnterpriseOpenRuleRelationInfo.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def invoice_rule_id(self):
        return self._invoice_rule_id

    @invoice_rule_id.setter
    def invoice_rule_id(self, value):
        self._invoice_rule_id = value
    @property
    def invoice_rule_name(self):
        return self._invoice_rule_name

    @invoice_rule_name.setter
    def invoice_rule_name(self, value):
        self._invoice_rule_name = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def seller_type(self):
        return self._seller_type

    @seller_type.setter
    def seller_type(self, value):
        self._seller_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_open_rule_record_info_list:
            if isinstance(self.enterprise_open_rule_record_info_list, list):
                for i in range(0, len(self.enterprise_open_rule_record_info_list)):
                    element = self.enterprise_open_rule_record_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enterprise_open_rule_record_info_list[i] = element.to_alipay_dict()
            if hasattr(self.enterprise_open_rule_record_info_list, 'to_alipay_dict'):
                params['enterprise_open_rule_record_info_list'] = self.enterprise_open_rule_record_info_list.to_alipay_dict()
            else:
                params['enterprise_open_rule_record_info_list'] = self.enterprise_open_rule_record_info_list
        if self.enterprise_open_rule_relation_info_list:
            if isinstance(self.enterprise_open_rule_relation_info_list, list):
                for i in range(0, len(self.enterprise_open_rule_relation_info_list)):
                    element = self.enterprise_open_rule_relation_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enterprise_open_rule_relation_info_list[i] = element.to_alipay_dict()
            if hasattr(self.enterprise_open_rule_relation_info_list, 'to_alipay_dict'):
                params['enterprise_open_rule_relation_info_list'] = self.enterprise_open_rule_relation_info_list.to_alipay_dict()
            else:
                params['enterprise_open_rule_relation_info_list'] = self.enterprise_open_rule_relation_info_list
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.invoice_rule_id:
            if hasattr(self.invoice_rule_id, 'to_alipay_dict'):
                params['invoice_rule_id'] = self.invoice_rule_id.to_alipay_dict()
            else:
                params['invoice_rule_id'] = self.invoice_rule_id
        if self.invoice_rule_name:
            if hasattr(self.invoice_rule_name, 'to_alipay_dict'):
                params['invoice_rule_name'] = self.invoice_rule_name.to_alipay_dict()
            else:
                params['invoice_rule_name'] = self.invoice_rule_name
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.seller_type:
            if hasattr(self.seller_type, 'to_alipay_dict'):
                params['seller_type'] = self.seller_type.to_alipay_dict()
            else:
                params['seller_type'] = self.seller_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseOpenRuleInfo()
        if 'enterprise_open_rule_record_info_list' in d:
            o.enterprise_open_rule_record_info_list = d['enterprise_open_rule_record_info_list']
        if 'enterprise_open_rule_relation_info_list' in d:
            o.enterprise_open_rule_relation_info_list = d['enterprise_open_rule_relation_info_list']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'invoice_rule_id' in d:
            o.invoice_rule_id = d['invoice_rule_id']
        if 'invoice_rule_name' in d:
            o.invoice_rule_name = d['invoice_rule_name']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'seller_type' in d:
            o.seller_type = d['seller_type']
        return o


