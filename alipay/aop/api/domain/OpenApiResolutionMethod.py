#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiResolutionMethod(object):

    def __init__(self):
        self._identifier = None
        self._requires_user_interaction = None
        self._type = None
        self._value = None

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = value
    @property
    def requires_user_interaction(self):
        return self._requires_user_interaction

    @requires_user_interaction.setter
    def requires_user_interaction(self, value):
        self._requires_user_interaction = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.identifier:
            if hasattr(self.identifier, 'to_alipay_dict'):
                params['identifier'] = self.identifier.to_alipay_dict()
            else:
                params['identifier'] = self.identifier
        if self.requires_user_interaction:
            if hasattr(self.requires_user_interaction, 'to_alipay_dict'):
                params['requires_user_interaction'] = self.requires_user_interaction.to_alipay_dict()
            else:
                params['requires_user_interaction'] = self.requires_user_interaction
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiResolutionMethod()
        if 'identifier' in d:
            o.identifier = d['identifier']
        if 'requires_user_interaction' in d:
            o.requires_user_interaction = d['requires_user_interaction']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


