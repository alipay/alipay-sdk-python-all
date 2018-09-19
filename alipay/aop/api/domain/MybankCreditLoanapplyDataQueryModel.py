#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyDataQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_type = None
        self._category = None
        self._data_version = None
        self._entity_code = None
        self._entity_name = None
        self._entity_type = None
        self._ip_id = None
        self._ip_role_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyDataQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'category' in d:
            o.category = d['category']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        return o


