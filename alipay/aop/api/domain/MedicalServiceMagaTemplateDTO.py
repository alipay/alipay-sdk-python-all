#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalServiceMagaCardDTO import MedicalServiceMagaCardDTO


class MedicalServiceMagaTemplateDTO(object):

    def __init__(self):
        self._card_count = None
        self._card_list = None
        self._template_id = None
        self._template_name = None

    @property
    def card_count(self):
        return self._card_count

    @card_count.setter
    def card_count(self, value):
        self._card_count = value
    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, value):
        if isinstance(value, list):
            self._card_list = list()
            for i in value:
                if isinstance(i, MedicalServiceMagaCardDTO):
                    self._card_list.append(i)
                else:
                    self._card_list.append(MedicalServiceMagaCardDTO.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_count:
            if hasattr(self.card_count, 'to_alipay_dict'):
                params['card_count'] = self.card_count.to_alipay_dict()
            else:
                params['card_count'] = self.card_count
        if self.card_list:
            if isinstance(self.card_list, list):
                for i in range(0, len(self.card_list)):
                    element = self.card_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_list[i] = element.to_alipay_dict()
            if hasattr(self.card_list, 'to_alipay_dict'):
                params['card_list'] = self.card_list.to_alipay_dict()
            else:
                params['card_list'] = self.card_list
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalServiceMagaTemplateDTO()
        if 'card_count' in d:
            o.card_count = d['card_count']
        if 'card_list' in d:
            o.card_list = d['card_list']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


