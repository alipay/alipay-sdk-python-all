#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinMortgagePreApproveFile(object):

    def __init__(self):
        self._file_path = None
        self._tag = None
        self._transfer_version = None
        self._type = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def transfer_version(self):
        return self._transfer_version

    @transfer_version.setter
    def transfer_version(self, value):
        self._transfer_version = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.transfer_version:
            if hasattr(self.transfer_version, 'to_alipay_dict'):
                params['transfer_version'] = self.transfer_version.to_alipay_dict()
            else:
                params['transfer_version'] = self.transfer_version
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
        o = CarfinMortgagePreApproveFile()
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'tag' in d:
            o.tag = d['tag']
        if 'transfer_version' in d:
            o.transfer_version = d['transfer_version']
        if 'type' in d:
            o.type = d['type']
        return o


