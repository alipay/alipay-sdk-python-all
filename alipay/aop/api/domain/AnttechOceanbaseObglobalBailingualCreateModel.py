#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateTextRequest import CreateTextRequest


class AnttechOceanbaseObglobalBailingualCreateModel(object):

    def __init__(self):
        self._create_text_request = None

    @property
    def create_text_request(self):
        return self._create_text_request

    @create_text_request.setter
    def create_text_request(self, value):
        if isinstance(value, CreateTextRequest):
            self._create_text_request = value
        else:
            self._create_text_request = CreateTextRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_text_request:
            if hasattr(self.create_text_request, 'to_alipay_dict'):
                params['create_text_request'] = self.create_text_request.to_alipay_dict()
            else:
                params['create_text_request'] = self.create_text_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalBailingualCreateModel()
        if 'create_text_request' in d:
            o.create_text_request = d['create_text_request']
        return o


