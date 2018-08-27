#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalSvTpCardHeadInfo(object):

    def __init__(self):
        self._header_icon = None
        self._header_title = None

    @property
    def header_icon(self):
        return self._header_icon

    @header_icon.setter
    def header_icon(self, value):
        self._header_icon = value
    @property
    def header_title(self):
        return self._header_title

    @header_title.setter
    def header_title(self, value):
        self._header_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.header_icon:
            if hasattr(self.header_icon, 'to_alipay_dict'):
                params['header_icon'] = self.header_icon.to_alipay_dict()
            else:
                params['header_icon'] = self.header_icon
        if self.header_title:
            if hasattr(self.header_title, 'to_alipay_dict'):
                params['header_title'] = self.header_title.to_alipay_dict()
            else:
                params['header_title'] = self.header_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalSvTpCardHeadInfo()
        if 'header_icon' in d:
            o.header_icon = d['header_icon']
        if 'header_title' in d:
            o.header_title = d['header_title']
        return o


