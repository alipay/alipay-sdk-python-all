#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcPointRefreshShowText(object):

    def __init__(self):
        self._bottom_text = None
        self._middle_smart_text = None
        self._title_text = None

    @property
    def bottom_text(self):
        return self._bottom_text

    @bottom_text.setter
    def bottom_text(self, value):
        self._bottom_text = value
    @property
    def middle_smart_text(self):
        return self._middle_smart_text

    @middle_smart_text.setter
    def middle_smart_text(self, value):
        self._middle_smart_text = value
    @property
    def title_text(self):
        return self._title_text

    @title_text.setter
    def title_text(self, value):
        self._title_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.bottom_text:
            if hasattr(self.bottom_text, 'to_alipay_dict'):
                params['bottom_text'] = self.bottom_text.to_alipay_dict()
            else:
                params['bottom_text'] = self.bottom_text
        if self.middle_smart_text:
            if hasattr(self.middle_smart_text, 'to_alipay_dict'):
                params['middle_smart_text'] = self.middle_smart_text.to_alipay_dict()
            else:
                params['middle_smart_text'] = self.middle_smart_text
        if self.title_text:
            if hasattr(self.title_text, 'to_alipay_dict'):
                params['title_text'] = self.title_text.to_alipay_dict()
            else:
                params['title_text'] = self.title_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshShowText()
        if 'bottom_text' in d:
            o.bottom_text = d['bottom_text']
        if 'middle_smart_text' in d:
            o.middle_smart_text = d['middle_smart_text']
        if 'title_text' in d:
            o.title_text = d['title_text']
        return o


