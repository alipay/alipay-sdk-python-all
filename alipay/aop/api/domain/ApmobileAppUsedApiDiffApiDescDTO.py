#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppUsedApiDTO import ApmobileAppUsedApiDTO


class ApmobileAppUsedApiDiffApiDescDTO(object):

    def __init__(self):
        self._app_used_api_dtos = None
        self._count = None
        self._permission_name = None

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
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def permission_name(self):
        return self._permission_name

    @permission_name.setter
    def permission_name(self, value):
        self._permission_name = value


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
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
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
        o = ApmobileAppUsedApiDiffApiDescDTO()
        if 'app_used_api_dtos' in d:
            o.app_used_api_dtos = d['app_used_api_dtos']
        if 'count' in d:
            o.count = d['count']
        if 'permission_name' in d:
            o.permission_name = d['permission_name']
        return o


