#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddTagResult import AddTagResult


class AddTagResponse(object):

    def __init__(self):
        self._add_tag_result = None

    @property
    def add_tag_result(self):
        return self._add_tag_result

    @add_tag_result.setter
    def add_tag_result(self, value):
        if isinstance(value, list):
            self._add_tag_result = list()
            for i in value:
                if isinstance(i, AddTagResult):
                    self._add_tag_result.append(i)
                else:
                    self._add_tag_result.append(AddTagResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.add_tag_result:
            if isinstance(self.add_tag_result, list):
                for i in range(0, len(self.add_tag_result)):
                    element = self.add_tag_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_tag_result[i] = element.to_alipay_dict()
            if hasattr(self.add_tag_result, 'to_alipay_dict'):
                params['add_tag_result'] = self.add_tag_result.to_alipay_dict()
            else:
                params['add_tag_result'] = self.add_tag_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddTagResponse()
        if 'add_tag_result' in d:
            o.add_tag_result = d['add_tag_result']
        return o


