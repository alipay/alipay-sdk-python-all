#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObcustomercoreUserentityQueryModel(object):

    def __init__(self):
        self._entity_type = None
        self._eq_name = None
        self._page_no = None
        self._page_size = None

    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def eq_name(self):
        return self._eq_name

    @eq_name.setter
    def eq_name(self, value):
        self._eq_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.eq_name:
            if hasattr(self.eq_name, 'to_alipay_dict'):
                params['eq_name'] = self.eq_name.to_alipay_dict()
            else:
                params['eq_name'] = self.eq_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObcustomercoreUserentityQueryModel()
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'eq_name' in d:
            o.eq_name = d['eq_name']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


