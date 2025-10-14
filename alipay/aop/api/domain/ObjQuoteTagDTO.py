#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QuoteTagDTO import QuoteTagDTO


class ObjQuoteTagDTO(object):

    def __init__(self):
        self._obj_id = None
        self._tags = None

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                if isinstance(i, QuoteTagDTO):
                    self._tags.append(i)
                else:
                    self._tags.append(QuoteTagDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.obj_id:
            if hasattr(self.obj_id, 'to_alipay_dict'):
                params['obj_id'] = self.obj_id.to_alipay_dict()
            else:
                params['obj_id'] = self.obj_id
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjQuoteTagDTO()
        if 'obj_id' in d:
            o.obj_id = d['obj_id']
        if 'tags' in d:
            o.tags = d['tags']
        return o


