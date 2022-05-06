#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ListDetail import ListDetail


class MybankCreditLoanapplyUserlistUploadModel(object):

    def __init__(self):
        self._category = None
        self._dataorgid = None
        self._dataprovider = None
        self._encryption_type = None
        self._list_info = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def dataorgid(self):
        return self._dataorgid

    @dataorgid.setter
    def dataorgid(self, value):
        self._dataorgid = value
    @property
    def dataprovider(self):
        return self._dataprovider

    @dataprovider.setter
    def dataprovider(self, value):
        self._dataprovider = value
    @property
    def encryption_type(self):
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, value):
        self._encryption_type = value
    @property
    def list_info(self):
        return self._list_info

    @list_info.setter
    def list_info(self, value):
        if isinstance(value, list):
            self._list_info = list()
            for i in value:
                if isinstance(i, ListDetail):
                    self._list_info.append(i)
                else:
                    self._list_info.append(ListDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.dataorgid:
            if hasattr(self.dataorgid, 'to_alipay_dict'):
                params['dataorgid'] = self.dataorgid.to_alipay_dict()
            else:
                params['dataorgid'] = self.dataorgid
        if self.dataprovider:
            if hasattr(self.dataprovider, 'to_alipay_dict'):
                params['dataprovider'] = self.dataprovider.to_alipay_dict()
            else:
                params['dataprovider'] = self.dataprovider
        if self.encryption_type:
            if hasattr(self.encryption_type, 'to_alipay_dict'):
                params['encryption_type'] = self.encryption_type.to_alipay_dict()
            else:
                params['encryption_type'] = self.encryption_type
        if self.list_info:
            if isinstance(self.list_info, list):
                for i in range(0, len(self.list_info)):
                    element = self.list_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list_info[i] = element.to_alipay_dict()
            if hasattr(self.list_info, 'to_alipay_dict'):
                params['list_info'] = self.list_info.to_alipay_dict()
            else:
                params['list_info'] = self.list_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyUserlistUploadModel()
        if 'category' in d:
            o.category = d['category']
        if 'dataorgid' in d:
            o.dataorgid = d['dataorgid']
        if 'dataprovider' in d:
            o.dataprovider = d['dataprovider']
        if 'encryption_type' in d:
            o.encryption_type = d['encryption_type']
        if 'list_info' in d:
            o.list_info = d['list_info']
        return o


