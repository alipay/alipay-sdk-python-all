#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoDocTemplateCreateModel(object):

    def __init__(self):
        self._content_md_5 = None
        self._content_type = None
        self._convert_to_pdf = None
        self._file_name = None

    @property
    def content_md_5(self):
        return self._content_md_5

    @content_md_5.setter
    def content_md_5(self, value):
        self._content_md_5 = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def convert_to_pdf(self):
        return self._convert_to_pdf

    @convert_to_pdf.setter
    def convert_to_pdf(self, value):
        self._convert_to_pdf = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_md_5:
            if hasattr(self.content_md_5, 'to_alipay_dict'):
                params['content_md_5'] = self.content_md_5.to_alipay_dict()
            else:
                params['content_md_5'] = self.content_md_5
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.convert_to_pdf:
            if hasattr(self.convert_to_pdf, 'to_alipay_dict'):
                params['convert_to_pdf'] = self.convert_to_pdf.to_alipay_dict()
            else:
                params['convert_to_pdf'] = self.convert_to_pdf
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoDocTemplateCreateModel()
        if 'content_md_5' in d:
            o.content_md_5 = d['content_md_5']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'convert_to_pdf' in d:
            o.convert_to_pdf = d['convert_to_pdf']
        if 'file_name' in d:
            o.file_name = d['file_name']
        return o


