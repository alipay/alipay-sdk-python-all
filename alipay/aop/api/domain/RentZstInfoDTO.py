#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentZstInfoDTO(object):

    def __init__(self):
        self._service_provider_model = None

    @property
    def service_provider_model(self):
        return self._service_provider_model

    @service_provider_model.setter
    def service_provider_model(self, value):
        self._service_provider_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_provider_model:
            if hasattr(self.service_provider_model, 'to_alipay_dict'):
                params['service_provider_model'] = self.service_provider_model.to_alipay_dict()
            else:
                params['service_provider_model'] = self.service_provider_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentZstInfoDTO()
        if 'service_provider_model' in d:
            o.service_provider_model = d['service_provider_model']
        return o


