#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceBaseInfo(object):

    def __init__(self):
        self._expense_type = None
        self._expense_type_desc = None
        self._expense_type_sub_category = None
        self._expense_type_sub_category_desc = None
        self._order_time = None
        self._related_service_id = None
        self._service_desc = None
        self._service_id = None
        self._service_name = None
        self._service_order_mode = None
        self._service_provider_id = None
        self._service_provider_name = None
        self._service_type = None

    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def expense_type_desc(self):
        return self._expense_type_desc

    @expense_type_desc.setter
    def expense_type_desc(self, value):
        self._expense_type_desc = value
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def expense_type_sub_category_desc(self):
        return self._expense_type_sub_category_desc

    @expense_type_sub_category_desc.setter
    def expense_type_sub_category_desc(self, value):
        self._expense_type_sub_category_desc = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def related_service_id(self):
        return self._related_service_id

    @related_service_id.setter
    def related_service_id(self, value):
        self._related_service_id = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_order_mode(self):
        return self._service_order_mode

    @service_order_mode.setter
    def service_order_mode(self, value):
        self._service_order_mode = value
    @property
    def service_provider_id(self):
        return self._service_provider_id

    @service_provider_id.setter
    def service_provider_id(self, value):
        self._service_provider_id = value
    @property
    def service_provider_name(self):
        return self._service_provider_name

    @service_provider_name.setter
    def service_provider_name(self, value):
        self._service_provider_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.expense_type_desc:
            if hasattr(self.expense_type_desc, 'to_alipay_dict'):
                params['expense_type_desc'] = self.expense_type_desc.to_alipay_dict()
            else:
                params['expense_type_desc'] = self.expense_type_desc
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.expense_type_sub_category_desc:
            if hasattr(self.expense_type_sub_category_desc, 'to_alipay_dict'):
                params['expense_type_sub_category_desc'] = self.expense_type_sub_category_desc.to_alipay_dict()
            else:
                params['expense_type_sub_category_desc'] = self.expense_type_sub_category_desc
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.related_service_id:
            if hasattr(self.related_service_id, 'to_alipay_dict'):
                params['related_service_id'] = self.related_service_id.to_alipay_dict()
            else:
                params['related_service_id'] = self.related_service_id
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_order_mode:
            if hasattr(self.service_order_mode, 'to_alipay_dict'):
                params['service_order_mode'] = self.service_order_mode.to_alipay_dict()
            else:
                params['service_order_mode'] = self.service_order_mode
        if self.service_provider_id:
            if hasattr(self.service_provider_id, 'to_alipay_dict'):
                params['service_provider_id'] = self.service_provider_id.to_alipay_dict()
            else:
                params['service_provider_id'] = self.service_provider_id
        if self.service_provider_name:
            if hasattr(self.service_provider_name, 'to_alipay_dict'):
                params['service_provider_name'] = self.service_provider_name.to_alipay_dict()
            else:
                params['service_provider_name'] = self.service_provider_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceBaseInfo()
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'expense_type_desc' in d:
            o.expense_type_desc = d['expense_type_desc']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'expense_type_sub_category_desc' in d:
            o.expense_type_sub_category_desc = d['expense_type_sub_category_desc']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'related_service_id' in d:
            o.related_service_id = d['related_service_id']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_order_mode' in d:
            o.service_order_mode = d['service_order_mode']
        if 'service_provider_id' in d:
            o.service_provider_id = d['service_provider_id']
        if 'service_provider_name' in d:
            o.service_provider_name = d['service_provider_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


