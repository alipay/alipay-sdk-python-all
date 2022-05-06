#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUseGuide(object):

    def __init__(self):
        self._mini_app_id = None
        self._mini_app_path = None
        self._mini_app_use_guide = None
        self._offline_code_use_guide = None
        self._service_codes = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_path(self):
        return self._mini_app_path

    @mini_app_path.setter
    def mini_app_path(self, value):
        self._mini_app_path = value
    @property
    def mini_app_use_guide(self):
        return self._mini_app_use_guide

    @mini_app_use_guide.setter
    def mini_app_use_guide(self, value):
        self._mini_app_use_guide = value
    @property
    def offline_code_use_guide(self):
        return self._offline_code_use_guide

    @offline_code_use_guide.setter
    def offline_code_use_guide(self, value):
        self._offline_code_use_guide = value
    @property
    def service_codes(self):
        return self._service_codes

    @service_codes.setter
    def service_codes(self, value):
        if isinstance(value, list):
            self._service_codes = list()
            for i in value:
                self._service_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_path:
            if hasattr(self.mini_app_path, 'to_alipay_dict'):
                params['mini_app_path'] = self.mini_app_path.to_alipay_dict()
            else:
                params['mini_app_path'] = self.mini_app_path
        if self.mini_app_use_guide:
            if hasattr(self.mini_app_use_guide, 'to_alipay_dict'):
                params['mini_app_use_guide'] = self.mini_app_use_guide.to_alipay_dict()
            else:
                params['mini_app_use_guide'] = self.mini_app_use_guide
        if self.offline_code_use_guide:
            if hasattr(self.offline_code_use_guide, 'to_alipay_dict'):
                params['offline_code_use_guide'] = self.offline_code_use_guide.to_alipay_dict()
            else:
                params['offline_code_use_guide'] = self.offline_code_use_guide
        if self.service_codes:
            if isinstance(self.service_codes, list):
                for i in range(0, len(self.service_codes)):
                    element = self.service_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_codes[i] = element.to_alipay_dict()
            if hasattr(self.service_codes, 'to_alipay_dict'):
                params['service_codes'] = self.service_codes.to_alipay_dict()
            else:
                params['service_codes'] = self.service_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseGuide()
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_path' in d:
            o.mini_app_path = d['mini_app_path']
        if 'mini_app_use_guide' in d:
            o.mini_app_use_guide = d['mini_app_use_guide']
        if 'offline_code_use_guide' in d:
            o.offline_code_use_guide = d['offline_code_use_guide']
        if 'service_codes' in d:
            o.service_codes = d['service_codes']
        return o


