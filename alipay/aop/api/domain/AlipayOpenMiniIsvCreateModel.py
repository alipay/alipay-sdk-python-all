#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateMiniRequest import CreateMiniRequest


class AlipayOpenMiniIsvCreateModel(object):

    def __init__(self):
        self._create_mini_request = None

    @property
    def create_mini_request(self):
        return self._create_mini_request

    @create_mini_request.setter
    def create_mini_request(self, value):
        if isinstance(value, CreateMiniRequest):
            self._create_mini_request = value
        else:
            self._create_mini_request = CreateMiniRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_mini_request:
            if hasattr(self.create_mini_request, 'to_alipay_dict'):
                params['create_mini_request'] = self.create_mini_request.to_alipay_dict()
            else:
                params['create_mini_request'] = self.create_mini_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniIsvCreateModel()
        if 'create_mini_request' in d:
            o.create_mini_request = d['create_mini_request']
        return o


