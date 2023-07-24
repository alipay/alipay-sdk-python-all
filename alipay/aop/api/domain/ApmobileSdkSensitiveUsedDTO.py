#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppUsedApiDTO import ApmobileAppUsedApiDTO


class ApmobileSdkSensitiveUsedDTO(object):

    def __init__(self):
        self._app_used_api_dtos = None
        self._permission_id = None
        self._sdk_name = None
        self._sdk_used_num = None

    @property
    def app_used_api_dtos(self):
        return self._app_used_api_dtos

    @app_used_api_dtos.setter
    def app_used_api_dtos(self, value):
        if isinstance(value, list):
            self._app_used_api_dtos = list()
            for i in value:
                if isinstance(i, ApmobileAppUsedApiDTO):
                    self._app_used_api_dtos.append(i)
                else:
                    self._app_used_api_dtos.append(ApmobileAppUsedApiDTO.from_alipay_dict(i))
    @property
    def permission_id(self):
        return self._permission_id

    @permission_id.setter
    def permission_id(self, value):
        self._permission_id = value
    @property
    def sdk_name(self):
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, value):
        self._sdk_name = value
    @property
    def sdk_used_num(self):
        return self._sdk_used_num

    @sdk_used_num.setter
    def sdk_used_num(self, value):
        self._sdk_used_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_used_api_dtos:
            if isinstance(self.app_used_api_dtos, list):
                for i in range(0, len(self.app_used_api_dtos)):
                    element = self.app_used_api_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_used_api_dtos[i] = element.to_alipay_dict()
            if hasattr(self.app_used_api_dtos, 'to_alipay_dict'):
                params['app_used_api_dtos'] = self.app_used_api_dtos.to_alipay_dict()
            else:
                params['app_used_api_dtos'] = self.app_used_api_dtos
        if self.permission_id:
            if hasattr(self.permission_id, 'to_alipay_dict'):
                params['permission_id'] = self.permission_id.to_alipay_dict()
            else:
                params['permission_id'] = self.permission_id
        if self.sdk_name:
            if hasattr(self.sdk_name, 'to_alipay_dict'):
                params['sdk_name'] = self.sdk_name.to_alipay_dict()
            else:
                params['sdk_name'] = self.sdk_name
        if self.sdk_used_num:
            if hasattr(self.sdk_used_num, 'to_alipay_dict'):
                params['sdk_used_num'] = self.sdk_used_num.to_alipay_dict()
            else:
                params['sdk_used_num'] = self.sdk_used_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileSdkSensitiveUsedDTO()
        if 'app_used_api_dtos' in d:
            o.app_used_api_dtos = d['app_used_api_dtos']
        if 'permission_id' in d:
            o.permission_id = d['permission_id']
        if 'sdk_name' in d:
            o.sdk_name = d['sdk_name']
        if 'sdk_used_num' in d:
            o.sdk_used_num = d['sdk_used_num']
        return o


