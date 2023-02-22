#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBoxKeywordInfo import SearchBoxKeywordInfo
from alipay.aop.api.domain.SearchBoxKeywordInfo import SearchBoxKeywordInfo


class SearchBoxAreaKeyWordModule(object):

    def __init__(self):
        self._latest_audit_area_keyword_info = None
        self._module_id = None
        self._module_type = None
        self._valid_area_keyword_info = None

    @property
    def latest_audit_area_keyword_info(self):
        return self._latest_audit_area_keyword_info

    @latest_audit_area_keyword_info.setter
    def latest_audit_area_keyword_info(self, value):
        if isinstance(value, SearchBoxKeywordInfo):
            self._latest_audit_area_keyword_info = value
        else:
            self._latest_audit_area_keyword_info = SearchBoxKeywordInfo.from_alipay_dict(value)
    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def module_type(self):
        return self._module_type

    @module_type.setter
    def module_type(self, value):
        self._module_type = value
    @property
    def valid_area_keyword_info(self):
        return self._valid_area_keyword_info

    @valid_area_keyword_info.setter
    def valid_area_keyword_info(self, value):
        if isinstance(value, SearchBoxKeywordInfo):
            self._valid_area_keyword_info = value
        else:
            self._valid_area_keyword_info = SearchBoxKeywordInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.latest_audit_area_keyword_info:
            if hasattr(self.latest_audit_area_keyword_info, 'to_alipay_dict'):
                params['latest_audit_area_keyword_info'] = self.latest_audit_area_keyword_info.to_alipay_dict()
            else:
                params['latest_audit_area_keyword_info'] = self.latest_audit_area_keyword_info
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.module_type:
            if hasattr(self.module_type, 'to_alipay_dict'):
                params['module_type'] = self.module_type.to_alipay_dict()
            else:
                params['module_type'] = self.module_type
        if self.valid_area_keyword_info:
            if hasattr(self.valid_area_keyword_info, 'to_alipay_dict'):
                params['valid_area_keyword_info'] = self.valid_area_keyword_info.to_alipay_dict()
            else:
                params['valid_area_keyword_info'] = self.valid_area_keyword_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxAreaKeyWordModule()
        if 'latest_audit_area_keyword_info' in d:
            o.latest_audit_area_keyword_info = d['latest_audit_area_keyword_info']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        if 'valid_area_keyword_info' in d:
            o.valid_area_keyword_info = d['valid_area_keyword_info']
        return o


