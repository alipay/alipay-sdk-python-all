#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileApiDetailDTO import ApmobileApiDetailDTO


class ApmobileApiDetailDiffByApiNameDTO(object):

    def __init__(self):
        self._api_name = None
        self._api_type = None
        self._app_used_api_dto_list = None
        self._count = None

    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def api_type(self):
        return self._api_type

    @api_type.setter
    def api_type(self, value):
        self._api_type = value
    @property
    def app_used_api_dto_list(self):
        return self._app_used_api_dto_list

    @app_used_api_dto_list.setter
    def app_used_api_dto_list(self, value):
        if isinstance(value, ApmobileApiDetailDTO):
            self._app_used_api_dto_list = value
        else:
            self._app_used_api_dto_list = ApmobileApiDetailDTO.from_alipay_dict(value)
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.api_type:
            if hasattr(self.api_type, 'to_alipay_dict'):
                params['api_type'] = self.api_type.to_alipay_dict()
            else:
                params['api_type'] = self.api_type
        if self.app_used_api_dto_list:
            if hasattr(self.app_used_api_dto_list, 'to_alipay_dict'):
                params['app_used_api_dto_list'] = self.app_used_api_dto_list.to_alipay_dict()
            else:
                params['app_used_api_dto_list'] = self.app_used_api_dto_list
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileApiDetailDiffByApiNameDTO()
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'api_type' in d:
            o.api_type = d['api_type']
        if 'app_used_api_dto_list' in d:
            o.app_used_api_dto_list = d['app_used_api_dto_list']
        if 'count' in d:
            o.count = d['count']
        return o


