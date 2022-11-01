#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommonKeyword import CommonKeyword


class AlipayEbppIndustryGovFastmodeSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._desensitization = None
        self._keyword_list = None
        self._open_id = None
        self._org_code = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def desensitization(self):
        return self._desensitization

    @desensitization.setter
    def desensitization(self, value):
        self._desensitization = value
    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                if isinstance(i, CommonKeyword):
                    self._keyword_list.append(i)
                else:
                    self._keyword_list.append(CommonKeyword.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.desensitization:
            if hasattr(self.desensitization, 'to_alipay_dict'):
                params['desensitization'] = self.desensitization.to_alipay_dict()
            else:
                params['desensitization'] = self.desensitization
        if self.keyword_list:
            if isinstance(self.keyword_list, list):
                for i in range(0, len(self.keyword_list)):
                    element = self.keyword_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_list[i] = element.to_alipay_dict()
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryGovFastmodeSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'desensitization' in d:
            o.desensitization = d['desensitization']
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


