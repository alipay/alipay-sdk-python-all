#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtraInfo import ExtraInfo


class AlipayCommerceIndustryServiceSubmitModel(object):

    def __init__(self):
        self._extra_info = None
        self._industry_info = None
        self._out_service_code = None
        self._service_action = None
        self._service_description = None
        self._service_name = None
        self._service_type = None
        self._service_url = None

    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        if isinstance(value, list):
            self._extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._extra_info.append(i)
                else:
                    self._extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def industry_info(self):
        return self._industry_info

    @industry_info.setter
    def industry_info(self, value):
        self._industry_info = value
    @property
    def out_service_code(self):
        return self._out_service_code

    @out_service_code.setter
    def out_service_code(self, value):
        self._out_service_code = value
    @property
    def service_action(self):
        return self._service_action

    @service_action.setter
    def service_action(self, value):
        self._service_action = value
    @property
    def service_description(self):
        return self._service_description

    @service_description.setter
    def service_description(self, value):
        self._service_description = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_info:
            if isinstance(self.extra_info, list):
                for i in range(0, len(self.extra_info)):
                    element = self.extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extra_info[i] = element.to_alipay_dict()
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
        if self.industry_info:
            if hasattr(self.industry_info, 'to_alipay_dict'):
                params['industry_info'] = self.industry_info.to_alipay_dict()
            else:
                params['industry_info'] = self.industry_info
        if self.out_service_code:
            if hasattr(self.out_service_code, 'to_alipay_dict'):
                params['out_service_code'] = self.out_service_code.to_alipay_dict()
            else:
                params['out_service_code'] = self.out_service_code
        if self.service_action:
            if hasattr(self.service_action, 'to_alipay_dict'):
                params['service_action'] = self.service_action.to_alipay_dict()
            else:
                params['service_action'] = self.service_action
        if self.service_description:
            if hasattr(self.service_description, 'to_alipay_dict'):
                params['service_description'] = self.service_description.to_alipay_dict()
            else:
                params['service_description'] = self.service_description
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIndustryServiceSubmitModel()
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'industry_info' in d:
            o.industry_info = d['industry_info']
        if 'out_service_code' in d:
            o.out_service_code = d['out_service_code']
        if 'service_action' in d:
            o.service_action = d['service_action']
        if 'service_description' in d:
            o.service_description = d['service_description']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


