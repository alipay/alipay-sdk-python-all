#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpAssistantServiceSubtitleStyle import EpAssistantServiceSubtitleStyle


class EpAssistantServiceSubtitleSegment(object):

    def __init__(self):
        self._style = None
        self._text = None

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        if isinstance(value, EpAssistantServiceSubtitleStyle):
            self._style = value
        else:
            self._style = EpAssistantServiceSubtitleStyle.from_alipay_dict(value)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.style:
            if hasattr(self.style, 'to_alipay_dict'):
                params['style'] = self.style.to_alipay_dict()
            else:
                params['style'] = self.style
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAssistantServiceSubtitleSegment()
        if 'style' in d:
            o.style = d['style']
        if 'text' in d:
            o.text = d['text']
        return o


