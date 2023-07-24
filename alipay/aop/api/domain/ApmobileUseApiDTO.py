#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileApiDetailDTO import ApmobileApiDetailDTO


class ApmobileUseApiDTO(object):

    def __init__(self):
        self._api_used_num = None
        self._app_used_api_dto_list = None
        self._sdk_api_name = None

    @property
    def api_used_num(self):
        return self._api_used_num

    @api_used_num.setter
    def api_used_num(self, value):
        self._api_used_num = value
    @property
    def app_used_api_dto_list(self):
        return self._app_used_api_dto_list

    @app_used_api_dto_list.setter
    def app_used_api_dto_list(self, value):
        if isinstance(value, list):
            self._app_used_api_dto_list = list()
            for i in value:
                if isinstance(i, ApmobileApiDetailDTO):
                    self._app_used_api_dto_list.append(i)
                else:
                    self._app_used_api_dto_list.append(ApmobileApiDetailDTO.from_alipay_dict(i))
    @property
    def sdk_api_name(self):
        return self._sdk_api_name

    @sdk_api_name.setter
    def sdk_api_name(self, value):
        self._sdk_api_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_used_num:
            if hasattr(self.api_used_num, 'to_alipay_dict'):
                params['api_used_num'] = self.api_used_num.to_alipay_dict()
            else:
                params['api_used_num'] = self.api_used_num
        if self.app_used_api_dto_list:
            if isinstance(self.app_used_api_dto_list, list):
                for i in range(0, len(self.app_used_api_dto_list)):
                    element = self.app_used_api_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_used_api_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.app_used_api_dto_list, 'to_alipay_dict'):
                params['app_used_api_dto_list'] = self.app_used_api_dto_list.to_alipay_dict()
            else:
                params['app_used_api_dto_list'] = self.app_used_api_dto_list
        if self.sdk_api_name:
            if hasattr(self.sdk_api_name, 'to_alipay_dict'):
                params['sdk_api_name'] = self.sdk_api_name.to_alipay_dict()
            else:
                params['sdk_api_name'] = self.sdk_api_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileUseApiDTO()
        if 'api_used_num' in d:
            o.api_used_num = d['api_used_num']
        if 'app_used_api_dto_list' in d:
            o.app_used_api_dto_list = d['app_used_api_dto_list']
        if 'sdk_api_name' in d:
            o.sdk_api_name = d['sdk_api_name']
        return o


