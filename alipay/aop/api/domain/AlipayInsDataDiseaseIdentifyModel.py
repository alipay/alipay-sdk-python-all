#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataDiseaseIdentifyModel(object):

    def __init__(self):
        self._action_type = None
        self._disease_name = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataDiseaseIdentifyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        return o


