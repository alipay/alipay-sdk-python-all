#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McardStylInfo(object):

    def __init__(self):
        self._background_id = None
        self._bg_color = None
        self._logo_id = None

    @property
    def background_id(self):
        return self._background_id

    @background_id.setter
    def background_id(self, value):
        self._background_id = value
    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
    @property
    def logo_id(self):
        return self._logo_id

    @logo_id.setter
    def logo_id(self, value):
        self._logo_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_id:
            if hasattr(self.background_id, 'to_alipay_dict'):
                params['background_id'] = self.background_id.to_alipay_dict()
            else:
                params['background_id'] = self.background_id
        if self.bg_color:
            if hasattr(self.bg_color, 'to_alipay_dict'):
                params['bg_color'] = self.bg_color.to_alipay_dict()
            else:
                params['bg_color'] = self.bg_color
        if self.logo_id:
            if hasattr(self.logo_id, 'to_alipay_dict'):
                params['logo_id'] = self.logo_id.to_alipay_dict()
            else:
                params['logo_id'] = self.logo_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McardStylInfo()
        if 'background_id' in d:
            o.background_id = d['background_id']
        if 'bg_color' in d:
            o.bg_color = d['bg_color']
        if 'logo_id' in d:
            o.logo_id = d['logo_id']
        return o


