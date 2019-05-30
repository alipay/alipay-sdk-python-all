#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceAbilityExtInfo(object):

    def __init__(self):
        self._age = None
        self._algfactors = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._channel = None
        self._choose_face_rule = None
        self._face_data_type = None
        self._feature = None
        self._hasrisk = None
        self._quality = None
        self._rect = None
        self._sex = None
        self._source = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def algfactors(self):
        return self._algfactors

    @algfactors.setter
    def algfactors(self, value):
        self._algfactors = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def choose_face_rule(self):
        return self._choose_face_rule

    @choose_face_rule.setter
    def choose_face_rule(self, value):
        self._choose_face_rule = value
    @property
    def face_data_type(self):
        return self._face_data_type

    @face_data_type.setter
    def face_data_type(self, value):
        self._face_data_type = value
    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value
    @property
    def hasrisk(self):
        return self._hasrisk

    @hasrisk.setter
    def hasrisk(self, value):
        self._hasrisk = value
    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.algfactors:
            if hasattr(self.algfactors, 'to_alipay_dict'):
                params['algfactors'] = self.algfactors.to_alipay_dict()
            else:
                params['algfactors'] = self.algfactors
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.choose_face_rule:
            if hasattr(self.choose_face_rule, 'to_alipay_dict'):
                params['choose_face_rule'] = self.choose_face_rule.to_alipay_dict()
            else:
                params['choose_face_rule'] = self.choose_face_rule
        if self.face_data_type:
            if hasattr(self.face_data_type, 'to_alipay_dict'):
                params['face_data_type'] = self.face_data_type.to_alipay_dict()
            else:
                params['face_data_type'] = self.face_data_type
        if self.feature:
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.hasrisk:
            if hasattr(self.hasrisk, 'to_alipay_dict'):
                params['hasrisk'] = self.hasrisk.to_alipay_dict()
            else:
                params['hasrisk'] = self.hasrisk
        if self.quality:
            if hasattr(self.quality, 'to_alipay_dict'):
                params['quality'] = self.quality.to_alipay_dict()
            else:
                params['quality'] = self.quality
        if self.rect:
            if hasattr(self.rect, 'to_alipay_dict'):
                params['rect'] = self.rect.to_alipay_dict()
            else:
                params['rect'] = self.rect
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceAbilityExtInfo()
        if 'age' in d:
            o.age = d['age']
        if 'algfactors' in d:
            o.algfactors = d['algfactors']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'choose_face_rule' in d:
            o.choose_face_rule = d['choose_face_rule']
        if 'face_data_type' in d:
            o.face_data_type = d['face_data_type']
        if 'feature' in d:
            o.feature = d['feature']
        if 'hasrisk' in d:
            o.hasrisk = d['hasrisk']
        if 'quality' in d:
            o.quality = d['quality']
        if 'rect' in d:
            o.rect = d['rect']
        if 'sex' in d:
            o.sex = d['sex']
        if 'source' in d:
            o.source = d['source']
        return o


