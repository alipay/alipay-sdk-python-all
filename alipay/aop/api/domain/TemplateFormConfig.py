#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateFormFields import TemplateFormFields


class TemplateFormConfig(object):

    def __init__(self):
        self._fields = None
        self._open_card_mini_app_id = None

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, TemplateFormFields):
            self._fields = value
        else:
            self._fields = TemplateFormFields.from_alipay_dict(value)
    @property
    def open_card_mini_app_id(self):
        return self._open_card_mini_app_id

    @open_card_mini_app_id.setter
    def open_card_mini_app_id(self, value):
        self._open_card_mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fields:
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.open_card_mini_app_id:
            if hasattr(self.open_card_mini_app_id, 'to_alipay_dict'):
                params['open_card_mini_app_id'] = self.open_card_mini_app_id.to_alipay_dict()
            else:
                params['open_card_mini_app_id'] = self.open_card_mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateFormConfig()
        if 'fields' in d:
            o.fields = d['fields']
        if 'open_card_mini_app_id' in d:
            o.open_card_mini_app_id = d['open_card_mini_app_id']
        return o


