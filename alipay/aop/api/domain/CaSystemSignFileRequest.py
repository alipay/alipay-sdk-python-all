#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSystemSignAreaRequest import CaSystemSignAreaRequest


class CaSystemSignFileRequest(object):

    def __init__(self):
        self._ca_system_sign_area_request_list = None
        self._file_id = None

    @property
    def ca_system_sign_area_request_list(self):
        return self._ca_system_sign_area_request_list

    @ca_system_sign_area_request_list.setter
    def ca_system_sign_area_request_list(self, value):
        if isinstance(value, list):
            self._ca_system_sign_area_request_list = list()
            for i in value:
                if isinstance(i, CaSystemSignAreaRequest):
                    self._ca_system_sign_area_request_list.append(i)
                else:
                    self._ca_system_sign_area_request_list.append(CaSystemSignAreaRequest.from_alipay_dict(i))
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ca_system_sign_area_request_list:
            if isinstance(self.ca_system_sign_area_request_list, list):
                for i in range(0, len(self.ca_system_sign_area_request_list)):
                    element = self.ca_system_sign_area_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ca_system_sign_area_request_list[i] = element.to_alipay_dict()
            if hasattr(self.ca_system_sign_area_request_list, 'to_alipay_dict'):
                params['ca_system_sign_area_request_list'] = self.ca_system_sign_area_request_list.to_alipay_dict()
            else:
                params['ca_system_sign_area_request_list'] = self.ca_system_sign_area_request_list
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaSystemSignFileRequest()
        if 'ca_system_sign_area_request_list' in d:
            o.ca_system_sign_area_request_list = d['ca_system_sign_area_request_list']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


