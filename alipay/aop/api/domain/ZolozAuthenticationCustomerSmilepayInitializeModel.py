#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationCustomerSmilepayInitializeModel(object):

    def __init__(self):
        self._service_id = None
        self._service_params = None
        self._zimmetainfo = None

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_params(self):
        return self._service_params

    @service_params.setter
    def service_params(self, value):
        self._service_params = value
    @property
    def zimmetainfo(self):
        return self._zimmetainfo

    @zimmetainfo.setter
    def zimmetainfo(self, value):
        self._zimmetainfo = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_params:
            if hasattr(self.service_params, 'to_alipay_dict'):
                params['service_params'] = self.service_params.to_alipay_dict()
            else:
                params['service_params'] = self.service_params
        if self.zimmetainfo:
            if hasattr(self.zimmetainfo, 'to_alipay_dict'):
                params['zimmetainfo'] = self.zimmetainfo.to_alipay_dict()
            else:
                params['zimmetainfo'] = self.zimmetainfo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerSmilepayInitializeModel()
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_params' in d:
            o.service_params = d['service_params']
        if 'zimmetainfo' in d:
            o.zimmetainfo = d['zimmetainfo']
        return o


