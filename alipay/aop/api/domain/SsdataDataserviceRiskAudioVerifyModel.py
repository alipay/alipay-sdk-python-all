#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAudioVerifyModel(object):

    def __init__(self):
        self._audio_content = None
        self._audio_type = None
        self._checker = None
        self._risk_type = None
        self._sample_rate = None

    @property
    def audio_content(self):
        return self._audio_content

    @audio_content.setter
    def audio_content(self, value):
        self._audio_content = value
    @property
    def audio_type(self):
        return self._audio_type

    @audio_type.setter
    def audio_type(self, value):
        self._audio_type = value
    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        if isinstance(value, list):
            self._risk_type = list()
            for i in value:
                self._risk_type.append(i)
    @property
    def sample_rate(self):
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value):
        self._sample_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_content:
            if hasattr(self.audio_content, 'to_alipay_dict'):
                params['audio_content'] = self.audio_content.to_alipay_dict()
            else:
                params['audio_content'] = self.audio_content
        if self.audio_type:
            if hasattr(self.audio_type, 'to_alipay_dict'):
                params['audio_type'] = self.audio_type.to_alipay_dict()
            else:
                params['audio_type'] = self.audio_type
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.risk_type:
            if isinstance(self.risk_type, list):
                for i in range(0, len(self.risk_type)):
                    element = self.risk_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_type[i] = element.to_alipay_dict()
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.sample_rate:
            if hasattr(self.sample_rate, 'to_alipay_dict'):
                params['sample_rate'] = self.sample_rate.to_alipay_dict()
            else:
                params['sample_rate'] = self.sample_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAudioVerifyModel()
        if 'audio_content' in d:
            o.audio_content = d['audio_content']
        if 'audio_type' in d:
            o.audio_type = d['audio_type']
        if 'checker' in d:
            o.checker = d['checker']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'sample_rate' in d:
            o.sample_rate = d['sample_rate']
        return o


