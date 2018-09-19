#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsQueryPerson import InsQueryPerson


class AlipayInsUnderwriteUserPolicyQueryModel(object):

    def __init__(self):
        self._page_no = None
        self._page_size = None
        self._person = None
        self._product_list = None
        self._status = None

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
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        if isinstance(value, InsQueryPerson):
            self._person = value
        else:
            self._person = InsQueryPerson.from_alipay_dict(value)
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                self._product_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.person:
            if hasattr(self.person, 'to_alipay_dict'):
                params['person'] = self.person.to_alipay_dict()
            else:
                params['person'] = self.person
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsUnderwriteUserPolicyQueryModel()
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'person' in d:
            o.person = d['person']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'status' in d:
            o.status = d['status']
        return o


