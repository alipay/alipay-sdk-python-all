#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FindTextDTO import FindTextDTO


class FindTextResponse(object):

    def __init__(self):
        self._text_list = None

    @property
    def text_list(self):
        return self._text_list

    @text_list.setter
    def text_list(self, value):
        if isinstance(value, list):
            self._text_list = list()
            for i in value:
                if isinstance(i, FindTextDTO):
                    self._text_list.append(i)
                else:
                    self._text_list.append(FindTextDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.text_list:
            if isinstance(self.text_list, list):
                for i in range(0, len(self.text_list)):
                    element = self.text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text_list[i] = element.to_alipay_dict()
            if hasattr(self.text_list, 'to_alipay_dict'):
                params['text_list'] = self.text_list.to_alipay_dict()
            else:
                params['text_list'] = self.text_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FindTextResponse()
        if 'text_list' in d:
            o.text_list = d['text_list']
        return o


