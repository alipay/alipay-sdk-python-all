#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchApplyPageQueryRequest(object):

    def __init__(self):
        self._apply_type = None
        self._audit_status_list = None
        self._category_code = None
        self._name = None
        self._page_num = None
        self._page_size = None
        self._service_code = None
        self._service_id = None
        self._start_row = None
        self._sub_service_code = None

    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def audit_status_list(self):
        return self._audit_status_list

    @audit_status_list.setter
    def audit_status_list(self, value):
        if isinstance(value, list):
            self._audit_status_list = list()
            for i in value:
                self._audit_status_list.append(i)
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def start_row(self):
        return self._start_row

    @start_row.setter
    def start_row(self, value):
        self._start_row = value
    @property
    def sub_service_code(self):
        return self._sub_service_code

    @sub_service_code.setter
    def sub_service_code(self, value):
        self._sub_service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.audit_status_list:
            if isinstance(self.audit_status_list, list):
                for i in range(0, len(self.audit_status_list)):
                    element = self.audit_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audit_status_list[i] = element.to_alipay_dict()
            if hasattr(self.audit_status_list, 'to_alipay_dict'):
                params['audit_status_list'] = self.audit_status_list.to_alipay_dict()
            else:
                params['audit_status_list'] = self.audit_status_list
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.start_row:
            if hasattr(self.start_row, 'to_alipay_dict'):
                params['start_row'] = self.start_row.to_alipay_dict()
            else:
                params['start_row'] = self.start_row
        if self.sub_service_code:
            if hasattr(self.sub_service_code, 'to_alipay_dict'):
                params['sub_service_code'] = self.sub_service_code.to_alipay_dict()
            else:
                params['sub_service_code'] = self.sub_service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchApplyPageQueryRequest()
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'audit_status_list' in d:
            o.audit_status_list = d['audit_status_list']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'name' in d:
            o.name = d['name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'start_row' in d:
            o.start_row = d['start_row']
        if 'sub_service_code' in d:
            o.sub_service_code = d['sub_service_code']
        return o


