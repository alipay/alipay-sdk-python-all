#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentRiskDetail(object):

    def __init__(self):
        self._code = None
        self._ext_properties = None
        self._generated_file = None
        self._name = None
        self._notice = None
        self._origin_file = None
        self._risk_infos = None
        self._risk_level = None
        self._type = None
        self._viola_words = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def ext_properties(self):
        return self._ext_properties

    @ext_properties.setter
    def ext_properties(self, value):
        self._ext_properties = value
    @property
    def generated_file(self):
        return self._generated_file

    @generated_file.setter
    def generated_file(self, value):
        self._generated_file = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def origin_file(self):
        return self._origin_file

    @origin_file.setter
    def origin_file(self, value):
        self._origin_file = value
    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        self._risk_infos = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def viola_words(self):
        return self._viola_words

    @viola_words.setter
    def viola_words(self, value):
        self._viola_words = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.ext_properties:
            if hasattr(self.ext_properties, 'to_alipay_dict'):
                params['ext_properties'] = self.ext_properties.to_alipay_dict()
            else:
                params['ext_properties'] = self.ext_properties
        if self.generated_file:
            if hasattr(self.generated_file, 'to_alipay_dict'):
                params['generated_file'] = self.generated_file.to_alipay_dict()
            else:
                params['generated_file'] = self.generated_file
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.origin_file:
            if hasattr(self.origin_file, 'to_alipay_dict'):
                params['origin_file'] = self.origin_file.to_alipay_dict()
            else:
                params['origin_file'] = self.origin_file
        if self.risk_infos:
            if hasattr(self.risk_infos, 'to_alipay_dict'):
                params['risk_infos'] = self.risk_infos.to_alipay_dict()
            else:
                params['risk_infos'] = self.risk_infos
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.viola_words:
            if hasattr(self.viola_words, 'to_alipay_dict'):
                params['viola_words'] = self.viola_words.to_alipay_dict()
            else:
                params['viola_words'] = self.viola_words
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentRiskDetail()
        if 'code' in d:
            o.code = d['code']
        if 'ext_properties' in d:
            o.ext_properties = d['ext_properties']
        if 'generated_file' in d:
            o.generated_file = d['generated_file']
        if 'name' in d:
            o.name = d['name']
        if 'notice' in d:
            o.notice = d['notice']
        if 'origin_file' in d:
            o.origin_file = d['origin_file']
        if 'risk_infos' in d:
            o.risk_infos = d['risk_infos']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'type' in d:
            o.type = d['type']
        if 'viola_words' in d:
            o.viola_words = d['viola_words']
        return o


