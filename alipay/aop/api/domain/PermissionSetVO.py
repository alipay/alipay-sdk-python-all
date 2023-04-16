#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiInfoVO import ApiInfoVO


class PermissionSetVO(object):

    def __init__(self):
        self._api_info_list = None
        self._permission_code = None
        self._permission_name = None

    @property
    def api_info_list(self):
        return self._api_info_list

    @api_info_list.setter
    def api_info_list(self, value):
        if isinstance(value, list):
            self._api_info_list = list()
            for i in value:
                if isinstance(i, ApiInfoVO):
                    self._api_info_list.append(i)
                else:
                    self._api_info_list.append(ApiInfoVO.from_alipay_dict(i))
    @property
    def permission_code(self):
        return self._permission_code

    @permission_code.setter
    def permission_code(self, value):
        self._permission_code = value
    @property
    def permission_name(self):
        return self._permission_name

    @permission_name.setter
    def permission_name(self, value):
        self._permission_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_info_list:
            if isinstance(self.api_info_list, list):
                for i in range(0, len(self.api_info_list)):
                    element = self.api_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.api_info_list[i] = element.to_alipay_dict()
            if hasattr(self.api_info_list, 'to_alipay_dict'):
                params['api_info_list'] = self.api_info_list.to_alipay_dict()
            else:
                params['api_info_list'] = self.api_info_list
        if self.permission_code:
            if hasattr(self.permission_code, 'to_alipay_dict'):
                params['permission_code'] = self.permission_code.to_alipay_dict()
            else:
                params['permission_code'] = self.permission_code
        if self.permission_name:
            if hasattr(self.permission_name, 'to_alipay_dict'):
                params['permission_name'] = self.permission_name.to_alipay_dict()
            else:
                params['permission_name'] = self.permission_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PermissionSetVO()
        if 'api_info_list' in d:
            o.api_info_list = d['api_info_list']
        if 'permission_code' in d:
            o.permission_code = d['permission_code']
        if 'permission_name' in d:
            o.permission_name = d['permission_name']
        return o


