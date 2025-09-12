#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorContractDTO(object):

    def __init__(self):
        self._contract_content = None
        self._contract_id = None
        self._contract_name = None
        self._default_checked = None
        self._force_read = None
        self._read_all = None
        self._read_time = None
        self._text_type = None

    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def default_checked(self):
        return self._default_checked

    @default_checked.setter
    def default_checked(self, value):
        self._default_checked = value
    @property
    def force_read(self):
        return self._force_read

    @force_read.setter
    def force_read(self, value):
        self._force_read = value
    @property
    def read_all(self):
        return self._read_all

    @read_all.setter
    def read_all(self, value):
        self._read_all = value
    @property
    def read_time(self):
        return self._read_time

    @read_time.setter
    def read_time(self, value):
        self._read_time = value
    @property
    def text_type(self):
        return self._text_type

    @text_type.setter
    def text_type(self, value):
        self._text_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_content:
            if hasattr(self.contract_content, 'to_alipay_dict'):
                params['contract_content'] = self.contract_content.to_alipay_dict()
            else:
                params['contract_content'] = self.contract_content
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.default_checked:
            if hasattr(self.default_checked, 'to_alipay_dict'):
                params['default_checked'] = self.default_checked.to_alipay_dict()
            else:
                params['default_checked'] = self.default_checked
        if self.force_read:
            if hasattr(self.force_read, 'to_alipay_dict'):
                params['force_read'] = self.force_read.to_alipay_dict()
            else:
                params['force_read'] = self.force_read
        if self.read_all:
            if hasattr(self.read_all, 'to_alipay_dict'):
                params['read_all'] = self.read_all.to_alipay_dict()
            else:
                params['read_all'] = self.read_all
        if self.read_time:
            if hasattr(self.read_time, 'to_alipay_dict'):
                params['read_time'] = self.read_time.to_alipay_dict()
            else:
                params['read_time'] = self.read_time
        if self.text_type:
            if hasattr(self.text_type, 'to_alipay_dict'):
                params['text_type'] = self.text_type.to_alipay_dict()
            else:
                params['text_type'] = self.text_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorContractDTO()
        if 'contract_content' in d:
            o.contract_content = d['contract_content']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'default_checked' in d:
            o.default_checked = d['default_checked']
        if 'force_read' in d:
            o.force_read = d['force_read']
        if 'read_all' in d:
            o.read_all = d['read_all']
        if 'read_time' in d:
            o.read_time = d['read_time']
        if 'text_type' in d:
            o.text_type = d['text_type']
        return o


