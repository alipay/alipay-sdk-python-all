#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseUsercenterBaseinfoQueryModel(object):

    def __init__(self):
        self._authorization = None

    @property
    def authorization(self):
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        self._authorization = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization:
            if hasattr(self.authorization, 'to_alipay_dict'):
                params['authorization'] = self.authorization.to_alipay_dict()
            else:
                params['authorization'] = self.authorization
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseUsercenterBaseinfoQueryModel()
        if 'authorization' in d:
            o.authorization = d['authorization']
        return o


