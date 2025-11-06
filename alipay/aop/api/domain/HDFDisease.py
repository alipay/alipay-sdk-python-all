#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFDisease(object):

    def __init__(self):
        self._disease_name = None

    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value


    def to_alipay_dict(self):
        params = dict()
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
        o = HDFDisease()
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        return o


