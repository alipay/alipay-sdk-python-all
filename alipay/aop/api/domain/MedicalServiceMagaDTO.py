#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalServiceMagaTemplateDTO import MedicalServiceMagaTemplateDTO


class MedicalServiceMagaDTO(object):

    def __init__(self):
        self._template_list = None

    @property
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, MedicalServiceMagaTemplateDTO):
                    self._template_list.append(i)
                else:
                    self._template_list.append(MedicalServiceMagaTemplateDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.template_list:
            if isinstance(self.template_list, list):
                for i in range(0, len(self.template_list)):
                    element = self.template_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_list[i] = element.to_alipay_dict()
            if hasattr(self.template_list, 'to_alipay_dict'):
                params['template_list'] = self.template_list.to_alipay_dict()
            else:
                params['template_list'] = self.template_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalServiceMagaDTO()
        if 'template_list' in d:
            o.template_list = d['template_list']
        return o


