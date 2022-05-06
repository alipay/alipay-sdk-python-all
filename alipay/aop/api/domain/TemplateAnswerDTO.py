#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnswerSelectDTO import AnswerSelectDTO


class TemplateAnswerDTO(object):

    def __init__(self):
        self._exp = None
        self._initial_value = None
        self._label_name = None
        self._placeholder = None
        self._selects = None
        self._type = None
        self._voucher_id = None

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value
    @property
    def initial_value(self):
        return self._initial_value

    @initial_value.setter
    def initial_value(self, value):
        self._initial_value = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        self._placeholder = value
    @property
    def selects(self):
        return self._selects

    @selects.setter
    def selects(self, value):
        if isinstance(value, list):
            self._selects = list()
            for i in value:
                if isinstance(i, AnswerSelectDTO):
                    self._selects.append(i)
                else:
                    self._selects.append(AnswerSelectDTO.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exp:
            if hasattr(self.exp, 'to_alipay_dict'):
                params['exp'] = self.exp.to_alipay_dict()
            else:
                params['exp'] = self.exp
        if self.initial_value:
            if hasattr(self.initial_value, 'to_alipay_dict'):
                params['initial_value'] = self.initial_value.to_alipay_dict()
            else:
                params['initial_value'] = self.initial_value
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.placeholder:
            if hasattr(self.placeholder, 'to_alipay_dict'):
                params['placeholder'] = self.placeholder.to_alipay_dict()
            else:
                params['placeholder'] = self.placeholder
        if self.selects:
            if isinstance(self.selects, list):
                for i in range(0, len(self.selects)):
                    element = self.selects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selects[i] = element.to_alipay_dict()
            if hasattr(self.selects, 'to_alipay_dict'):
                params['selects'] = self.selects.to_alipay_dict()
            else:
                params['selects'] = self.selects
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateAnswerDTO()
        if 'exp' in d:
            o.exp = d['exp']
        if 'initial_value' in d:
            o.initial_value = d['initial_value']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'placeholder' in d:
            o.placeholder = d['placeholder']
        if 'selects' in d:
            o.selects = d['selects']
        if 'type' in d:
            o.type = d['type']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


