#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleStartAppVO(object):

    def __init__(self):
        self._protocol = None
        self._start_app_model = None

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value
    @property
    def start_app_model(self):
        return self._start_app_model

    @start_app_model.setter
    def start_app_model(self, value):
        self._start_app_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.protocol:
            if hasattr(self.protocol, 'to_alipay_dict'):
                params['protocol'] = self.protocol.to_alipay_dict()
            else:
                params['protocol'] = self.protocol
        if self.start_app_model:
            if hasattr(self.start_app_model, 'to_alipay_dict'):
                params['start_app_model'] = self.start_app_model.to_alipay_dict()
            else:
                params['start_app_model'] = self.start_app_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleStartAppVO()
        if 'protocol' in d:
            o.protocol = d['protocol']
        if 'start_app_model' in d:
            o.start_app_model = d['start_app_model']
        return o


