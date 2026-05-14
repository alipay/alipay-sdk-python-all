#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalExaminationCspulistQueryModel(object):

    def __init__(self):
        self._category_id_list = None
        self._category_type = None
        self._page_index = None
        self._page_size = None
        self._spu_title = None

    @property
    def category_id_list(self):
        return self._category_id_list

    @category_id_list.setter
    def category_id_list(self, value):
        if isinstance(value, list):
            self._category_id_list = list()
            for i in value:
                self._category_id_list.append(i)
    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, value):
        self._category_type = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def spu_title(self):
        return self._spu_title

    @spu_title.setter
    def spu_title(self, value):
        self._spu_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id_list:
            if isinstance(self.category_id_list, list):
                for i in range(0, len(self.category_id_list)):
                    element = self.category_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_id_list[i] = element.to_alipay_dict()
            if hasattr(self.category_id_list, 'to_alipay_dict'):
                params['category_id_list'] = self.category_id_list.to_alipay_dict()
            else:
                params['category_id_list'] = self.category_id_list
        if self.category_type:
            if hasattr(self.category_type, 'to_alipay_dict'):
                params['category_type'] = self.category_type.to_alipay_dict()
            else:
                params['category_type'] = self.category_type
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.spu_title:
            if hasattr(self.spu_title, 'to_alipay_dict'):
                params['spu_title'] = self.spu_title.to_alipay_dict()
            else:
                params['spu_title'] = self.spu_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalExaminationCspulistQueryModel()
        if 'category_id_list' in d:
            o.category_id_list = d['category_id_list']
        if 'category_type' in d:
            o.category_type = d['category_type']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'spu_title' in d:
            o.spu_title = d['spu_title']
        return o


