#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsCbddoctorDiagnosisFinishModel(object):

    def __init__(self):
        self._service_order_id = None

    @property
    def service_order_id(self):
        return self._service_order_id

    @service_order_id.setter
    def service_order_id(self, value):
        self._service_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_order_id:
            if hasattr(self.service_order_id, 'to_alipay_dict'):
                params['service_order_id'] = self.service_order_id.to_alipay_dict()
            else:
                params['service_order_id'] = self.service_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsCbddoctorDiagnosisFinishModel()
        if 'service_order_id' in d:
            o.service_order_id = d['service_order_id']
        return o


