#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPaymentTermsItemDTO import OpenApiPaymentTermsItemDTO


class OpenApiPaymentTermsDTO(object):

    def __init__(self):
        self._contract_id = None
        self._id = None
        self._is_default = None
        self._other_terms = None
        self._pay_on_percent = None
        self._payment_name = None
        self._payment_terms_item_list = None
        self._payment_type = None
        self._sort = None
        self._term_source = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_default(self):
        return self._is_default

    @is_default.setter
    def is_default(self, value):
        self._is_default = value
    @property
    def other_terms(self):
        return self._other_terms

    @other_terms.setter
    def other_terms(self, value):
        self._other_terms = value
    @property
    def pay_on_percent(self):
        return self._pay_on_percent

    @pay_on_percent.setter
    def pay_on_percent(self, value):
        self._pay_on_percent = value
    @property
    def payment_name(self):
        return self._payment_name

    @payment_name.setter
    def payment_name(self, value):
        self._payment_name = value
    @property
    def payment_terms_item_list(self):
        return self._payment_terms_item_list

    @payment_terms_item_list.setter
    def payment_terms_item_list(self, value):
        if isinstance(value, list):
            self._payment_terms_item_list = list()
            for i in value:
                if isinstance(i, OpenApiPaymentTermsItemDTO):
                    self._payment_terms_item_list.append(i)
                else:
                    self._payment_terms_item_list.append(OpenApiPaymentTermsItemDTO.from_alipay_dict(i))
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def term_source(self):
        return self._term_source

    @term_source.setter
    def term_source(self, value):
        self._term_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_default:
            if hasattr(self.is_default, 'to_alipay_dict'):
                params['is_default'] = self.is_default.to_alipay_dict()
            else:
                params['is_default'] = self.is_default
        if self.other_terms:
            if hasattr(self.other_terms, 'to_alipay_dict'):
                params['other_terms'] = self.other_terms.to_alipay_dict()
            else:
                params['other_terms'] = self.other_terms
        if self.pay_on_percent:
            if hasattr(self.pay_on_percent, 'to_alipay_dict'):
                params['pay_on_percent'] = self.pay_on_percent.to_alipay_dict()
            else:
                params['pay_on_percent'] = self.pay_on_percent
        if self.payment_name:
            if hasattr(self.payment_name, 'to_alipay_dict'):
                params['payment_name'] = self.payment_name.to_alipay_dict()
            else:
                params['payment_name'] = self.payment_name
        if self.payment_terms_item_list:
            if isinstance(self.payment_terms_item_list, list):
                for i in range(0, len(self.payment_terms_item_list)):
                    element = self.payment_terms_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_terms_item_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_terms_item_list, 'to_alipay_dict'):
                params['payment_terms_item_list'] = self.payment_terms_item_list.to_alipay_dict()
            else:
                params['payment_terms_item_list'] = self.payment_terms_item_list
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.term_source:
            if hasattr(self.term_source, 'to_alipay_dict'):
                params['term_source'] = self.term_source.to_alipay_dict()
            else:
                params['term_source'] = self.term_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPaymentTermsDTO()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'id' in d:
            o.id = d['id']
        if 'is_default' in d:
            o.is_default = d['is_default']
        if 'other_terms' in d:
            o.other_terms = d['other_terms']
        if 'pay_on_percent' in d:
            o.pay_on_percent = d['pay_on_percent']
        if 'payment_name' in d:
            o.payment_name = d['payment_name']
        if 'payment_terms_item_list' in d:
            o.payment_terms_item_list = d['payment_terms_item_list']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'sort' in d:
            o.sort = d['sort']
        if 'term_source' in d:
            o.term_source = d['term_source']
        return o


