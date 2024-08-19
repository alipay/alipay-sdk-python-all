#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiOperationAnalysisCustomerAliasDTO import OpenApiOperationAnalysisCustomerAliasDTO
from alipay.aop.api.domain.OpenApiOperationAnalysisCustomerAliasDTO import OpenApiOperationAnalysisCustomerAliasDTO
from alipay.aop.api.domain.OpenApiOperationAnalysisCustomerAliasDTO import OpenApiOperationAnalysisCustomerAliasDTO


class OpenApiCustomerAnalysisResult(object):

    def __init__(self):
        self._all_user_data = None
        self._new_user_data = None
        self._old_user_data = None

    @property
    def all_user_data(self):
        return self._all_user_data

    @all_user_data.setter
    def all_user_data(self, value):
        if isinstance(value, list):
            self._all_user_data = list()
            for i in value:
                if isinstance(i, OpenApiOperationAnalysisCustomerAliasDTO):
                    self._all_user_data.append(i)
                else:
                    self._all_user_data.append(OpenApiOperationAnalysisCustomerAliasDTO.from_alipay_dict(i))
    @property
    def new_user_data(self):
        return self._new_user_data

    @new_user_data.setter
    def new_user_data(self, value):
        if isinstance(value, list):
            self._new_user_data = list()
            for i in value:
                if isinstance(i, OpenApiOperationAnalysisCustomerAliasDTO):
                    self._new_user_data.append(i)
                else:
                    self._new_user_data.append(OpenApiOperationAnalysisCustomerAliasDTO.from_alipay_dict(i))
    @property
    def old_user_data(self):
        return self._old_user_data

    @old_user_data.setter
    def old_user_data(self, value):
        if isinstance(value, list):
            self._old_user_data = list()
            for i in value:
                if isinstance(i, OpenApiOperationAnalysisCustomerAliasDTO):
                    self._old_user_data.append(i)
                else:
                    self._old_user_data.append(OpenApiOperationAnalysisCustomerAliasDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.all_user_data:
            if isinstance(self.all_user_data, list):
                for i in range(0, len(self.all_user_data)):
                    element = self.all_user_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.all_user_data[i] = element.to_alipay_dict()
            if hasattr(self.all_user_data, 'to_alipay_dict'):
                params['all_user_data'] = self.all_user_data.to_alipay_dict()
            else:
                params['all_user_data'] = self.all_user_data
        if self.new_user_data:
            if isinstance(self.new_user_data, list):
                for i in range(0, len(self.new_user_data)):
                    element = self.new_user_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.new_user_data[i] = element.to_alipay_dict()
            if hasattr(self.new_user_data, 'to_alipay_dict'):
                params['new_user_data'] = self.new_user_data.to_alipay_dict()
            else:
                params['new_user_data'] = self.new_user_data
        if self.old_user_data:
            if isinstance(self.old_user_data, list):
                for i in range(0, len(self.old_user_data)):
                    element = self.old_user_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.old_user_data[i] = element.to_alipay_dict()
            if hasattr(self.old_user_data, 'to_alipay_dict'):
                params['old_user_data'] = self.old_user_data.to_alipay_dict()
            else:
                params['old_user_data'] = self.old_user_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiCustomerAnalysisResult()
        if 'all_user_data' in d:
            o.all_user_data = d['all_user_data']
        if 'new_user_data' in d:
            o.new_user_data = d['new_user_data']
        if 'old_user_data' in d:
            o.old_user_data = d['old_user_data']
        return o


