#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftTemplateButtonBox(object):

    def __init__(self):
        self._button_url = None
        self._invalid_button_url = None

    @property
    def button_url(self):
        return self._button_url

    @button_url.setter
    def button_url(self, value):
        self._button_url = value
    @property
    def invalid_button_url(self):
        return self._invalid_button_url

    @invalid_button_url.setter
    def invalid_button_url(self, value):
        self._invalid_button_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_url:
            if hasattr(self.button_url, 'to_alipay_dict'):
                params['button_url'] = self.button_url.to_alipay_dict()
            else:
                params['button_url'] = self.button_url
        if self.invalid_button_url:
            if hasattr(self.invalid_button_url, 'to_alipay_dict'):
                params['invalid_button_url'] = self.invalid_button_url.to_alipay_dict()
            else:
                params['invalid_button_url'] = self.invalid_button_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftTemplateButtonBox()
        if 'button_url' in d:
            o.button_url = d['button_url']
        if 'invalid_button_url' in d:
            o.invalid_button_url = d['invalid_button_url']
        return o


