#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppUsedApiDiffApiDescDTO import ApmobileAppUsedApiDiffApiDescDTO
from alipay.aop.api.domain.ApmobileSdkSensitiveUsedDTO import ApmobileSdkSensitiveUsedDTO


class ApmobileAppPermissionUsedDTO(object):

    def __init__(self):
        self._app_used_api_diff_api_desc_dtos = None
        self._app_used_num = None
        self._is_applied = None
        self._is_used = None
        self._permission_code = None
        self._permission_name = None
        self._sdk_sensitive_used_list = None

    @property
    def app_used_api_diff_api_desc_dtos(self):
        return self._app_used_api_diff_api_desc_dtos

    @app_used_api_diff_api_desc_dtos.setter
    def app_used_api_diff_api_desc_dtos(self, value):
        if isinstance(value, list):
            self._app_used_api_diff_api_desc_dtos = list()
            for i in value:
                if isinstance(i, ApmobileAppUsedApiDiffApiDescDTO):
                    self._app_used_api_diff_api_desc_dtos.append(i)
                else:
                    self._app_used_api_diff_api_desc_dtos.append(ApmobileAppUsedApiDiffApiDescDTO.from_alipay_dict(i))
    @property
    def app_used_num(self):
        return self._app_used_num

    @app_used_num.setter
    def app_used_num(self, value):
        self._app_used_num = value
    @property
    def is_applied(self):
        return self._is_applied

    @is_applied.setter
    def is_applied(self, value):
        self._is_applied = value
    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value
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
    @property
    def sdk_sensitive_used_list(self):
        return self._sdk_sensitive_used_list

    @sdk_sensitive_used_list.setter
    def sdk_sensitive_used_list(self, value):
        if isinstance(value, list):
            self._sdk_sensitive_used_list = list()
            for i in value:
                if isinstance(i, ApmobileSdkSensitiveUsedDTO):
                    self._sdk_sensitive_used_list.append(i)
                else:
                    self._sdk_sensitive_used_list.append(ApmobileSdkSensitiveUsedDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_used_api_diff_api_desc_dtos:
            if isinstance(self.app_used_api_diff_api_desc_dtos, list):
                for i in range(0, len(self.app_used_api_diff_api_desc_dtos)):
                    element = self.app_used_api_diff_api_desc_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_used_api_diff_api_desc_dtos[i] = element.to_alipay_dict()
            if hasattr(self.app_used_api_diff_api_desc_dtos, 'to_alipay_dict'):
                params['app_used_api_diff_api_desc_dtos'] = self.app_used_api_diff_api_desc_dtos.to_alipay_dict()
            else:
                params['app_used_api_diff_api_desc_dtos'] = self.app_used_api_diff_api_desc_dtos
        if self.app_used_num:
            if hasattr(self.app_used_num, 'to_alipay_dict'):
                params['app_used_num'] = self.app_used_num.to_alipay_dict()
            else:
                params['app_used_num'] = self.app_used_num
        if self.is_applied:
            if hasattr(self.is_applied, 'to_alipay_dict'):
                params['is_applied'] = self.is_applied.to_alipay_dict()
            else:
                params['is_applied'] = self.is_applied
        if self.is_used:
            if hasattr(self.is_used, 'to_alipay_dict'):
                params['is_used'] = self.is_used.to_alipay_dict()
            else:
                params['is_used'] = self.is_used
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
        if self.sdk_sensitive_used_list:
            if isinstance(self.sdk_sensitive_used_list, list):
                for i in range(0, len(self.sdk_sensitive_used_list)):
                    element = self.sdk_sensitive_used_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sdk_sensitive_used_list[i] = element.to_alipay_dict()
            if hasattr(self.sdk_sensitive_used_list, 'to_alipay_dict'):
                params['sdk_sensitive_used_list'] = self.sdk_sensitive_used_list.to_alipay_dict()
            else:
                params['sdk_sensitive_used_list'] = self.sdk_sensitive_used_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionUsedDTO()
        if 'app_used_api_diff_api_desc_dtos' in d:
            o.app_used_api_diff_api_desc_dtos = d['app_used_api_diff_api_desc_dtos']
        if 'app_used_num' in d:
            o.app_used_num = d['app_used_num']
        if 'is_applied' in d:
            o.is_applied = d['is_applied']
        if 'is_used' in d:
            o.is_used = d['is_used']
        if 'permission_code' in d:
            o.permission_code = d['permission_code']
        if 'permission_name' in d:
            o.permission_name = d['permission_name']
        if 'sdk_sensitive_used_list' in d:
            o.sdk_sensitive_used_list = d['sdk_sensitive_used_list']
        return o


