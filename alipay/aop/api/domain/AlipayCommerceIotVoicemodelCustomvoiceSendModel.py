#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceModelContext import ServiceModelContext
from alipay.aop.api.domain.CustomVoiceVO import CustomVoiceVO


class AlipayCommerceIotVoicemodelCustomvoiceSendModel(object):

    def __init__(self):
        self._context = None
        self._custom_voice = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, ServiceModelContext):
            self._context = value
        else:
            self._context = ServiceModelContext.from_alipay_dict(value)
    @property
    def custom_voice(self):
        return self._custom_voice

    @custom_voice.setter
    def custom_voice(self, value):
        if isinstance(value, CustomVoiceVO):
            self._custom_voice = value
        else:
            self._custom_voice = CustomVoiceVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.custom_voice:
            if hasattr(self.custom_voice, 'to_alipay_dict'):
                params['custom_voice'] = self.custom_voice.to_alipay_dict()
            else:
                params['custom_voice'] = self.custom_voice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotVoicemodelCustomvoiceSendModel()
        if 'context' in d:
            o.context = d['context']
        if 'custom_voice' in d:
            o.custom_voice = d['custom_voice']
        return o


