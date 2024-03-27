#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalServiceDTO(object):

    def __init__(self):
        self._service_introduce = None
        self._service_key_words = None
        self._service_name = None

    @property
    def service_introduce(self):
        return self._service_introduce

    @service_introduce.setter
    def service_introduce(self, value):
        self._service_introduce = value
    @property
    def service_key_words(self):
        return self._service_key_words

    @service_key_words.setter
    def service_key_words(self, value):
        self._service_key_words = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_introduce:
            if hasattr(self.service_introduce, 'to_alipay_dict'):
                params['service_introduce'] = self.service_introduce.to_alipay_dict()
            else:
                params['service_introduce'] = self.service_introduce
        if self.service_key_words:
            if hasattr(self.service_key_words, 'to_alipay_dict'):
                params['service_key_words'] = self.service_key_words.to_alipay_dict()
            else:
                params['service_key_words'] = self.service_key_words
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalServiceDTO()
        if 'service_introduce' in d:
            o.service_introduce = d['service_introduce']
        if 'service_key_words' in d:
            o.service_key_words = d['service_key_words']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o


