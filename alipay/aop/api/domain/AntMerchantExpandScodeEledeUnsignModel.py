#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemoveTagRequest import RemoveTagRequest


class AntMerchantExpandScodeEledeUnsignModel(object):

    def __init__(self):
        self._remove_tag_request = None

    @property
    def remove_tag_request(self):
        return self._remove_tag_request

    @remove_tag_request.setter
    def remove_tag_request(self, value):
        if isinstance(value, list):
            self._remove_tag_request = list()
            for i in value:
                if isinstance(i, RemoveTagRequest):
                    self._remove_tag_request.append(i)
                else:
                    self._remove_tag_request.append(RemoveTagRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.remove_tag_request:
            if isinstance(self.remove_tag_request, list):
                for i in range(0, len(self.remove_tag_request)):
                    element = self.remove_tag_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_tag_request[i] = element.to_alipay_dict()
            if hasattr(self.remove_tag_request, 'to_alipay_dict'):
                params['remove_tag_request'] = self.remove_tag_request.to_alipay_dict()
            else:
                params['remove_tag_request'] = self.remove_tag_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandScodeEledeUnsignModel()
        if 'remove_tag_request' in d:
            o.remove_tag_request = d['remove_tag_request']
        return o


