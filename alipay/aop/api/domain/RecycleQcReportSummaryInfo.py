#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleQcReportSummaryInfo(object):

    def __init__(self):
        self._image_id_list = None
        self._inconsistent_text = None
        self._text = None

    @property
    def image_id_list(self):
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, value):
        if isinstance(value, list):
            self._image_id_list = list()
            for i in value:
                self._image_id_list.append(i)
    @property
    def inconsistent_text(self):
        return self._inconsistent_text

    @inconsistent_text.setter
    def inconsistent_text(self, value):
        self._inconsistent_text = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_id_list:
            if isinstance(self.image_id_list, list):
                for i in range(0, len(self.image_id_list)):
                    element = self.image_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_id_list, 'to_alipay_dict'):
                params['image_id_list'] = self.image_id_list.to_alipay_dict()
            else:
                params['image_id_list'] = self.image_id_list
        if self.inconsistent_text:
            if hasattr(self.inconsistent_text, 'to_alipay_dict'):
                params['inconsistent_text'] = self.inconsistent_text.to_alipay_dict()
            else:
                params['inconsistent_text'] = self.inconsistent_text
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
        o = RecycleQcReportSummaryInfo()
        if 'image_id_list' in d:
            o.image_id_list = d['image_id_list']
        if 'inconsistent_text' in d:
            o.inconsistent_text = d['inconsistent_text']
        if 'text' in d:
            o.text = d['text']
        return o


