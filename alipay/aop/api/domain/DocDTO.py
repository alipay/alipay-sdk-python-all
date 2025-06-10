#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DocDTO(object):

    def __init__(self):
        self._city_code = None
        self._doc_file_id = None
        self._doc_title = None
        self._doc_type = None
        self._out_doc_id = None
        self._run_status = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def doc_file_id(self):
        return self._doc_file_id

    @doc_file_id.setter
    def doc_file_id(self, value):
        self._doc_file_id = value
    @property
    def doc_title(self):
        return self._doc_title

    @doc_title.setter
    def doc_title(self, value):
        self._doc_title = value
    @property
    def doc_type(self):
        return self._doc_type

    @doc_type.setter
    def doc_type(self, value):
        self._doc_type = value
    @property
    def out_doc_id(self):
        return self._out_doc_id

    @out_doc_id.setter
    def out_doc_id(self, value):
        self._out_doc_id = value
    @property
    def run_status(self):
        return self._run_status

    @run_status.setter
    def run_status(self, value):
        self._run_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.doc_file_id:
            if hasattr(self.doc_file_id, 'to_alipay_dict'):
                params['doc_file_id'] = self.doc_file_id.to_alipay_dict()
            else:
                params['doc_file_id'] = self.doc_file_id
        if self.doc_title:
            if hasattr(self.doc_title, 'to_alipay_dict'):
                params['doc_title'] = self.doc_title.to_alipay_dict()
            else:
                params['doc_title'] = self.doc_title
        if self.doc_type:
            if hasattr(self.doc_type, 'to_alipay_dict'):
                params['doc_type'] = self.doc_type.to_alipay_dict()
            else:
                params['doc_type'] = self.doc_type
        if self.out_doc_id:
            if hasattr(self.out_doc_id, 'to_alipay_dict'):
                params['out_doc_id'] = self.out_doc_id.to_alipay_dict()
            else:
                params['out_doc_id'] = self.out_doc_id
        if self.run_status:
            if hasattr(self.run_status, 'to_alipay_dict'):
                params['run_status'] = self.run_status.to_alipay_dict()
            else:
                params['run_status'] = self.run_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DocDTO()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'doc_file_id' in d:
            o.doc_file_id = d['doc_file_id']
        if 'doc_title' in d:
            o.doc_title = d['doc_title']
        if 'doc_type' in d:
            o.doc_type = d['doc_type']
        if 'out_doc_id' in d:
            o.out_doc_id = d['out_doc_id']
        if 'run_status' in d:
            o.run_status = d['run_status']
        return o


