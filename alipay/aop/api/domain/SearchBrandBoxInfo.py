#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BoxExclusiveBase import BoxExclusiveBase
from alipay.aop.api.domain.BoxOrderStatusInfo import BoxOrderStatusInfo
from alipay.aop.api.domain.BoxExclusiveKeyword import BoxExclusiveKeyword
from alipay.aop.api.domain.BoxExclusiveService import BoxExclusiveService
from alipay.aop.api.domain.BoxExclusiveService import BoxExclusiveService


class SearchBrandBoxInfo(object):

    def __init__(self):
        self._base_info = None
        self._box_status = None
        self._box_type = None
        self._brand_id = None
        self._channel = None
        self._ext_info = None
        self._functions_order_info = None
        self._keywords = None
        self._operator_id = None
        self._operator_type = None
        self._related_accounts = None
        self._related_functions = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, BoxExclusiveBase):
            self._base_info = value
        else:
            self._base_info = BoxExclusiveBase.from_alipay_dict(value)
    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def box_type(self):
        return self._box_type

    @box_type.setter
    def box_type(self, value):
        self._box_type = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def functions_order_info(self):
        return self._functions_order_info

    @functions_order_info.setter
    def functions_order_info(self, value):
        if isinstance(value, BoxOrderStatusInfo):
            self._functions_order_info = value
        else:
            self._functions_order_info = BoxOrderStatusInfo.from_alipay_dict(value)
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, BoxExclusiveKeyword):
            self._keywords = value
        else:
            self._keywords = BoxExclusiveKeyword.from_alipay_dict(value)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def related_accounts(self):
        return self._related_accounts

    @related_accounts.setter
    def related_accounts(self, value):
        if isinstance(value, list):
            self._related_accounts = list()
            for i in value:
                if isinstance(i, BoxExclusiveService):
                    self._related_accounts.append(i)
                else:
                    self._related_accounts.append(BoxExclusiveService.from_alipay_dict(i))
    @property
    def related_functions(self):
        return self._related_functions

    @related_functions.setter
    def related_functions(self, value):
        if isinstance(value, list):
            self._related_functions = list()
            for i in value:
                if isinstance(i, BoxExclusiveService):
                    self._related_functions.append(i)
                else:
                    self._related_functions.append(BoxExclusiveService.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.box_status:
            if hasattr(self.box_status, 'to_alipay_dict'):
                params['box_status'] = self.box_status.to_alipay_dict()
            else:
                params['box_status'] = self.box_status
        if self.box_type:
            if hasattr(self.box_type, 'to_alipay_dict'):
                params['box_type'] = self.box_type.to_alipay_dict()
            else:
                params['box_type'] = self.box_type
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.functions_order_info:
            if hasattr(self.functions_order_info, 'to_alipay_dict'):
                params['functions_order_info'] = self.functions_order_info.to_alipay_dict()
            else:
                params['functions_order_info'] = self.functions_order_info
        if self.keywords:
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.related_accounts:
            if isinstance(self.related_accounts, list):
                for i in range(0, len(self.related_accounts)):
                    element = self.related_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_accounts[i] = element.to_alipay_dict()
            if hasattr(self.related_accounts, 'to_alipay_dict'):
                params['related_accounts'] = self.related_accounts.to_alipay_dict()
            else:
                params['related_accounts'] = self.related_accounts
        if self.related_functions:
            if isinstance(self.related_functions, list):
                for i in range(0, len(self.related_functions)):
                    element = self.related_functions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_functions[i] = element.to_alipay_dict()
            if hasattr(self.related_functions, 'to_alipay_dict'):
                params['related_functions'] = self.related_functions.to_alipay_dict()
            else:
                params['related_functions'] = self.related_functions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBrandBoxInfo()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'box_status' in d:
            o.box_status = d['box_status']
        if 'box_type' in d:
            o.box_type = d['box_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'functions_order_info' in d:
            o.functions_order_info = d['functions_order_info']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'related_accounts' in d:
            o.related_accounts = d['related_accounts']
        if 'related_functions' in d:
            o.related_functions = d['related_functions']
        return o


