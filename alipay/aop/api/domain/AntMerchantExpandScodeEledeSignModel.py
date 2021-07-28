#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddTagRequest import AddTagRequest


class AntMerchantExpandScodeEledeSignModel(object):

    def __init__(self):
        self._add_tag_request = None

    @property
    def add_tag_request(self):
        return self._add_tag_request

    @add_tag_request.setter
    def add_tag_request(self, value):
        if isinstance(value, list):
            self._add_tag_request = list()
            for i in value:
                if isinstance(i, AddTagRequest):
                    self._add_tag_request.append(i)
                else:
                    self._add_tag_request.append(AddTagRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.add_tag_request:
            if isinstance(self.add_tag_request, list):
                for i in range(0, len(self.add_tag_request)):
                    element = self.add_tag_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_tag_request[i] = element.to_alipay_dict()
            if hasattr(self.add_tag_request, 'to_alipay_dict'):
                params['add_tag_request'] = self.add_tag_request.to_alipay_dict()
            else:
                params['add_tag_request'] = self.add_tag_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandScodeEledeSignModel()
        if 'add_tag_request' in d:
            o.add_tag_request = d['add_tag_request']
        return o


