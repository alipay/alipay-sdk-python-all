#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicineTagInfo(object):

    def __init__(self):
        self._tag_text = None
        self._tag_type = None

    @property
    def tag_text(self):
        return self._tag_text

    @tag_text.setter
    def tag_text(self, value):
        if isinstance(value, list):
            self._tag_text = list()
            for i in value:
                self._tag_text.append(i)
    @property
    def tag_type(self):
        return self._tag_type

    @tag_type.setter
    def tag_type(self, value):
        self._tag_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_text:
            if isinstance(self.tag_text, list):
                for i in range(0, len(self.tag_text)):
                    element = self.tag_text[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_text[i] = element.to_alipay_dict()
            if hasattr(self.tag_text, 'to_alipay_dict'):
                params['tag_text'] = self.tag_text.to_alipay_dict()
            else:
                params['tag_text'] = self.tag_text
        if self.tag_type:
            if hasattr(self.tag_type, 'to_alipay_dict'):
                params['tag_type'] = self.tag_type.to_alipay_dict()
            else:
                params['tag_type'] = self.tag_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineTagInfo()
        if 'tag_text' in d:
            o.tag_text = d['tag_text']
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        return o


