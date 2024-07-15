#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyBaseVO import CompanyBaseVO
from alipay.aop.api.domain.CorpCompanyVO import CorpCompanyVO


class CompanyListQueryResult(object):

    def __init__(self):
        self._company_base_model_list = None
        self._data = None
        self._field_info_list = None
        self._page_num = None
        self._page_size = None
        self._paging = None
        self._total = None

    @property
    def company_base_model_list(self):
        return self._company_base_model_list

    @company_base_model_list.setter
    def company_base_model_list(self, value):
        if isinstance(value, list):
            self._company_base_model_list = list()
            for i in value:
                if isinstance(i, CompanyBaseVO):
                    self._company_base_model_list.append(i)
                else:
                    self._company_base_model_list.append(CompanyBaseVO.from_alipay_dict(i))
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, CorpCompanyVO):
                    self._data.append(i)
                else:
                    self._data.append(CorpCompanyVO.from_alipay_dict(i))
    @property
    def field_info_list(self):
        return self._field_info_list

    @field_info_list.setter
    def field_info_list(self, value):
        if isinstance(value, list):
            self._field_info_list = list()
            for i in value:
                self._field_info_list.append(i)
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
    def paging(self):
        return self._paging

    @paging.setter
    def paging(self, value):
        self._paging = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_base_model_list:
            if isinstance(self.company_base_model_list, list):
                for i in range(0, len(self.company_base_model_list)):
                    element = self.company_base_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_base_model_list[i] = element.to_alipay_dict()
            if hasattr(self.company_base_model_list, 'to_alipay_dict'):
                params['company_base_model_list'] = self.company_base_model_list.to_alipay_dict()
            else:
                params['company_base_model_list'] = self.company_base_model_list
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.field_info_list:
            if isinstance(self.field_info_list, list):
                for i in range(0, len(self.field_info_list)):
                    element = self.field_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.field_info_list[i] = element.to_alipay_dict()
            if hasattr(self.field_info_list, 'to_alipay_dict'):
                params['field_info_list'] = self.field_info_list.to_alipay_dict()
            else:
                params['field_info_list'] = self.field_info_list
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
        if self.paging:
            if hasattr(self.paging, 'to_alipay_dict'):
                params['paging'] = self.paging.to_alipay_dict()
            else:
                params['paging'] = self.paging
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyListQueryResult()
        if 'company_base_model_list' in d:
            o.company_base_model_list = d['company_base_model_list']
        if 'data' in d:
            o.data = d['data']
        if 'field_info_list' in d:
            o.field_info_list = d['field_info_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'paging' in d:
            o.paging = d['paging']
        if 'total' in d:
            o.total = d['total']
        return o


