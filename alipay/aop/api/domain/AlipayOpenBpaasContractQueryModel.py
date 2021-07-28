#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBpaasContractQueryModel(object):

    def __init__(self):
        self._bpaas_app_id = None
        self._service_id = None

    @property
    def bpaas_app_id(self):
        return self._bpaas_app_id

    @bpaas_app_id.setter
    def bpaas_app_id(self, value):
        self._bpaas_app_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bpaas_app_id:
            if hasattr(self.bpaas_app_id, 'to_alipay_dict'):
                params['bpaas_app_id'] = self.bpaas_app_id.to_alipay_dict()
            else:
                params['bpaas_app_id'] = self.bpaas_app_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBpaasContractQueryModel()
        if 'bpaas_app_id' in d:
            o.bpaas_app_id = d['bpaas_app_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


