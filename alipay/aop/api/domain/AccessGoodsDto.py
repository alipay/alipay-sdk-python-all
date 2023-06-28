#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessQuotationDto import AccessQuotationDto


class AccessGoodsDto(object):

    def __init__(self):
        self._contract_code = None
        self._data_source = None
        self._is_apply_directory_mall = None
        self._minimum_purchase_quantity = None
        self._quotation_list = None
        self._source_value = None
        self._supplier_id = None
        self._tax_rate = None

    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def is_apply_directory_mall(self):
        return self._is_apply_directory_mall

    @is_apply_directory_mall.setter
    def is_apply_directory_mall(self, value):
        self._is_apply_directory_mall = value
    @property
    def minimum_purchase_quantity(self):
        return self._minimum_purchase_quantity

    @minimum_purchase_quantity.setter
    def minimum_purchase_quantity(self, value):
        self._minimum_purchase_quantity = value
    @property
    def quotation_list(self):
        return self._quotation_list

    @quotation_list.setter
    def quotation_list(self, value):
        if isinstance(value, list):
            self._quotation_list = list()
            for i in value:
                if isinstance(i, AccessQuotationDto):
                    self._quotation_list.append(i)
                else:
                    self._quotation_list.append(AccessQuotationDto.from_alipay_dict(i))
    @property
    def source_value(self):
        return self._source_value

    @source_value.setter
    def source_value(self, value):
        self._source_value = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.is_apply_directory_mall:
            if hasattr(self.is_apply_directory_mall, 'to_alipay_dict'):
                params['is_apply_directory_mall'] = self.is_apply_directory_mall.to_alipay_dict()
            else:
                params['is_apply_directory_mall'] = self.is_apply_directory_mall
        if self.minimum_purchase_quantity:
            if hasattr(self.minimum_purchase_quantity, 'to_alipay_dict'):
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity.to_alipay_dict()
            else:
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity
        if self.quotation_list:
            if isinstance(self.quotation_list, list):
                for i in range(0, len(self.quotation_list)):
                    element = self.quotation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quotation_list[i] = element.to_alipay_dict()
            if hasattr(self.quotation_list, 'to_alipay_dict'):
                params['quotation_list'] = self.quotation_list.to_alipay_dict()
            else:
                params['quotation_list'] = self.quotation_list
        if self.source_value:
            if hasattr(self.source_value, 'to_alipay_dict'):
                params['source_value'] = self.source_value.to_alipay_dict()
            else:
                params['source_value'] = self.source_value
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessGoodsDto()
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'is_apply_directory_mall' in d:
            o.is_apply_directory_mall = d['is_apply_directory_mall']
        if 'minimum_purchase_quantity' in d:
            o.minimum_purchase_quantity = d['minimum_purchase_quantity']
        if 'quotation_list' in d:
            o.quotation_list = d['quotation_list']
        if 'source_value' in d:
            o.source_value = d['source_value']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


