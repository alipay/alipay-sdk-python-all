#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FieldInfoDTO import FieldInfoDTO


class SaveRecordDTO(object):

    def __init__(self):
        self._fields = None

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                if isinstance(i, FieldInfoDTO):
                    self._fields.append(i)
                else:
                    self._fields.append(FieldInfoDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaveRecordDTO()
        if 'fields' in d:
            o.fields = d['fields']
        return o


