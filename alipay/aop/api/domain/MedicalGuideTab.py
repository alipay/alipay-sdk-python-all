#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalGuideTab(object):

    def __init__(self):
        self._btn_name = None
        self._title = None
        self._type = None

    @property
    def btn_name(self):
        return self._btn_name

    @btn_name.setter
    def btn_name(self, value):
        self._btn_name = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.btn_name:
            if hasattr(self.btn_name, 'to_alipay_dict'):
                params['btn_name'] = self.btn_name.to_alipay_dict()
            else:
                params['btn_name'] = self.btn_name
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideTab()
        if 'btn_name' in d:
            o.btn_name = d['btn_name']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


