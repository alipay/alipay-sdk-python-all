#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateStyleDTO(object):

    def __init__(self):
        self._background_color = None

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_color:
            if hasattr(self.background_color, 'to_alipay_dict'):
                params['background_color'] = self.background_color.to_alipay_dict()
            else:
                params['background_color'] = self.background_color
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateStyleDTO()
        if 'background_color' in d:
            o.background_color = d['background_color']
        return o


