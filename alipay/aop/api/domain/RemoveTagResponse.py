#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemoveTagResult import RemoveTagResult


class RemoveTagResponse(object):

    def __init__(self):
        self._remove_tag_result = None

    @property
    def remove_tag_result(self):
        return self._remove_tag_result

    @remove_tag_result.setter
    def remove_tag_result(self, value):
        if isinstance(value, list):
            self._remove_tag_result = list()
            for i in value:
                if isinstance(i, RemoveTagResult):
                    self._remove_tag_result.append(i)
                else:
                    self._remove_tag_result.append(RemoveTagResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.remove_tag_result:
            if isinstance(self.remove_tag_result, list):
                for i in range(0, len(self.remove_tag_result)):
                    element = self.remove_tag_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_tag_result[i] = element.to_alipay_dict()
            if hasattr(self.remove_tag_result, 'to_alipay_dict'):
                params['remove_tag_result'] = self.remove_tag_result.to_alipay_dict()
            else:
                params['remove_tag_result'] = self.remove_tag_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RemoveTagResponse()
        if 'remove_tag_result' in d:
            o.remove_tag_result = d['remove_tag_result']
        return o


