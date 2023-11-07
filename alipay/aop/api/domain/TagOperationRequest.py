#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagOperationRequest(object):

    def __init__(self):
        self._domain_table_key = None
        self._operation_code = None
        self._operator = None
        self._resource_id = None
        self._tag_api_name_list = None

    @property
    def domain_table_key(self):
        return self._domain_table_key

    @domain_table_key.setter
    def domain_table_key(self, value):
        self._domain_table_key = value
    @property
    def operation_code(self):
        return self._operation_code

    @operation_code.setter
    def operation_code(self, value):
        self._operation_code = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def tag_api_name_list(self):
        return self._tag_api_name_list

    @tag_api_name_list.setter
    def tag_api_name_list(self, value):
        if isinstance(value, list):
            self._tag_api_name_list = list()
            for i in value:
                self._tag_api_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.domain_table_key:
            if hasattr(self.domain_table_key, 'to_alipay_dict'):
                params['domain_table_key'] = self.domain_table_key.to_alipay_dict()
            else:
                params['domain_table_key'] = self.domain_table_key
        if self.operation_code:
            if hasattr(self.operation_code, 'to_alipay_dict'):
                params['operation_code'] = self.operation_code.to_alipay_dict()
            else:
                params['operation_code'] = self.operation_code
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.tag_api_name_list:
            if isinstance(self.tag_api_name_list, list):
                for i in range(0, len(self.tag_api_name_list)):
                    element = self.tag_api_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_api_name_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_api_name_list, 'to_alipay_dict'):
                params['tag_api_name_list'] = self.tag_api_name_list.to_alipay_dict()
            else:
                params['tag_api_name_list'] = self.tag_api_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TagOperationRequest()
        if 'domain_table_key' in d:
            o.domain_table_key = d['domain_table_key']
        if 'operation_code' in d:
            o.operation_code = d['operation_code']
        if 'operator' in d:
            o.operator = d['operator']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'tag_api_name_list' in d:
            o.tag_api_name_list = d['tag_api_name_list']
        return o


