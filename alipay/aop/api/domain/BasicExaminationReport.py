#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BasicPhysicalItem import BasicPhysicalItem


class BasicExaminationReport(object):

    def __init__(self):
        self._item_code = None
        self._item_name = None
        self._item_project_list = None

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_project_list(self):
        return self._item_project_list

    @item_project_list.setter
    def item_project_list(self, value):
        if isinstance(value, list):
            self._item_project_list = list()
            for i in value:
                if isinstance(i, BasicPhysicalItem):
                    self._item_project_list.append(i)
                else:
                    self._item_project_list.append(BasicPhysicalItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_project_list:
            if isinstance(self.item_project_list, list):
                for i in range(0, len(self.item_project_list)):
                    element = self.item_project_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_project_list[i] = element.to_alipay_dict()
            if hasattr(self.item_project_list, 'to_alipay_dict'):
                params['item_project_list'] = self.item_project_list.to_alipay_dict()
            else:
                params['item_project_list'] = self.item_project_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BasicExaminationReport()
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_project_list' in d:
            o.item_project_list = d['item_project_list']
        return o


