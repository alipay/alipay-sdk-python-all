#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeContentItem import ApeContentItem
from alipay.aop.api.domain.ApeDataItem import ApeDataItem
from alipay.aop.api.domain.ApeGenericItem import ApeGenericItem
from alipay.aop.api.domain.ApeRetailItem import ApeRetailItem


class AlipayDigitalopUcdpApedataSyncModel(object):

    def __init__(self):
        self._content_list = None
        self._data_list = None
        self._data_type = None
        self._generic_item_list = None
        self._project_id = None
        self._retail_item_list = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, ApeContentItem):
                    self._content_list.append(i)
                else:
                    self._content_list.append(ApeContentItem.from_alipay_dict(i))
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, ApeDataItem):
                    self._data_list.append(i)
                else:
                    self._data_list.append(ApeDataItem.from_alipay_dict(i))
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def generic_item_list(self):
        return self._generic_item_list

    @generic_item_list.setter
    def generic_item_list(self, value):
        if isinstance(value, list):
            self._generic_item_list = list()
            for i in value:
                if isinstance(i, ApeGenericItem):
                    self._generic_item_list.append(i)
                else:
                    self._generic_item_list.append(ApeGenericItem.from_alipay_dict(i))
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def retail_item_list(self):
        return self._retail_item_list

    @retail_item_list.setter
    def retail_item_list(self, value):
        if isinstance(value, list):
            self._retail_item_list = list()
            for i in value:
                if isinstance(i, ApeRetailItem):
                    self._retail_item_list.append(i)
                else:
                    self._retail_item_list.append(ApeRetailItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.generic_item_list:
            if isinstance(self.generic_item_list, list):
                for i in range(0, len(self.generic_item_list)):
                    element = self.generic_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.generic_item_list[i] = element.to_alipay_dict()
            if hasattr(self.generic_item_list, 'to_alipay_dict'):
                params['generic_item_list'] = self.generic_item_list.to_alipay_dict()
            else:
                params['generic_item_list'] = self.generic_item_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.retail_item_list:
            if isinstance(self.retail_item_list, list):
                for i in range(0, len(self.retail_item_list)):
                    element = self.retail_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.retail_item_list[i] = element.to_alipay_dict()
            if hasattr(self.retail_item_list, 'to_alipay_dict'):
                params['retail_item_list'] = self.retail_item_list.to_alipay_dict()
            else:
                params['retail_item_list'] = self.retail_item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApedataSyncModel()
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'generic_item_list' in d:
            o.generic_item_list = d['generic_item_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'retail_item_list' in d:
            o.retail_item_list = d['retail_item_list']
        return o


