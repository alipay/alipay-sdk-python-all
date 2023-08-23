#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PropertyOutDTO(object):

    def __init__(self):
        self._disabled = None
        self._required = None
        self._show = None

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        self._disabled = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value


    def to_alipay_dict(self):
        params = dict()
        if self.disabled:
            if hasattr(self.disabled, 'to_alipay_dict'):
                params['disabled'] = self.disabled.to_alipay_dict()
            else:
                params['disabled'] = self.disabled
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.show:
            if hasattr(self.show, 'to_alipay_dict'):
                params['show'] = self.show.to_alipay_dict()
            else:
                params['show'] = self.show
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PropertyOutDTO()
        if 'disabled' in d:
            o.disabled = d['disabled']
        if 'required' in d:
            o.required = d['required']
        if 'show' in d:
            o.show = d['show']
        return o


