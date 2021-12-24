#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplatePlaceholderDTO import TemplatePlaceholderDTO


class AnttechOceanbaseNotifySendModel(object):

    def __init__(self):
        self._passport_id = None
        self._scene = None
        self._template_placeholder_list = None

    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def template_placeholder_list(self):
        return self._template_placeholder_list

    @template_placeholder_list.setter
    def template_placeholder_list(self, value):
        if isinstance(value, list):
            self._template_placeholder_list = list()
            for i in value:
                if isinstance(i, TemplatePlaceholderDTO):
                    self._template_placeholder_list.append(i)
                else:
                    self._template_placeholder_list.append(TemplatePlaceholderDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.template_placeholder_list:
            if isinstance(self.template_placeholder_list, list):
                for i in range(0, len(self.template_placeholder_list)):
                    element = self.template_placeholder_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_placeholder_list[i] = element.to_alipay_dict()
            if hasattr(self.template_placeholder_list, 'to_alipay_dict'):
                params['template_placeholder_list'] = self.template_placeholder_list.to_alipay_dict()
            else:
                params['template_placeholder_list'] = self.template_placeholder_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseNotifySendModel()
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'template_placeholder_list' in d:
            o.template_placeholder_list = d['template_placeholder_list']
        return o


