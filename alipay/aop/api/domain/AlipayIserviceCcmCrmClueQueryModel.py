#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayCondition import AlipayCondition


class AlipayIserviceCcmCrmClueQueryModel(object):

    def __init__(self):
        self._condition = None
        self._current_page = None
        self._obj_code = None
        self._page_size = None
        self._tenant_id = None

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if isinstance(value, list):
            self._condition = list()
            for i in value:
                if isinstance(i, AlipayCondition):
                    self._condition.append(i)
                else:
                    self._condition.append(AlipayCondition.from_alipay_dict(i))
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def obj_code(self):
        return self._obj_code

    @obj_code.setter
    def obj_code(self, value):
        self._obj_code = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition:
            if isinstance(self.condition, list):
                for i in range(0, len(self.condition)):
                    element = self.condition[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.condition[i] = element.to_alipay_dict()
            if hasattr(self.condition, 'to_alipay_dict'):
                params['condition'] = self.condition.to_alipay_dict()
            else:
                params['condition'] = self.condition
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.obj_code:
            if hasattr(self.obj_code, 'to_alipay_dict'):
                params['obj_code'] = self.obj_code.to_alipay_dict()
            else:
                params['obj_code'] = self.obj_code
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmCrmClueQueryModel()
        if 'condition' in d:
            o.condition = d['condition']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'obj_code' in d:
            o.obj_code = d['obj_code']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


