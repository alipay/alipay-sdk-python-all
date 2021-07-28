#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceViewcallbackQueryModel(object):

    def __init__(self):
        self._service_code = None
        self._service_view_meta_id = None

    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_view_meta_id(self):
        return self._service_view_meta_id

    @service_view_meta_id.setter
    def service_view_meta_id(self, value):
        self._service_view_meta_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_view_meta_id:
            if hasattr(self.service_view_meta_id, 'to_alipay_dict'):
                params['service_view_meta_id'] = self.service_view_meta_id.to_alipay_dict()
            else:
                params['service_view_meta_id'] = self.service_view_meta_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceViewcallbackQueryModel()
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_view_meta_id' in d:
            o.service_view_meta_id = d['service_view_meta_id']
        return o


