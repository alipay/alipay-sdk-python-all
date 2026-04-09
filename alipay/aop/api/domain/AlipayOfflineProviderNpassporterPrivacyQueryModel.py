#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterPrivacyQueryModel(object):

    def __init__(self):
        self._alipay_id = None
        self._open_id = None
        self._out_encrypt_cert_no_list = None
        self._project_id = None
        self._solution_type = None
        self._sub_project_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_encrypt_cert_no_list(self):
        return self._out_encrypt_cert_no_list

    @out_encrypt_cert_no_list.setter
    def out_encrypt_cert_no_list(self, value):
        if isinstance(value, list):
            self._out_encrypt_cert_no_list = list()
            for i in value:
                self._out_encrypt_cert_no_list.append(i)
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def solution_type(self):
        return self._solution_type

    @solution_type.setter
    def solution_type(self, value):
        self._solution_type = value
    @property
    def sub_project_id(self):
        return self._sub_project_id

    @sub_project_id.setter
    def sub_project_id(self, value):
        self._sub_project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_encrypt_cert_no_list:
            if isinstance(self.out_encrypt_cert_no_list, list):
                for i in range(0, len(self.out_encrypt_cert_no_list)):
                    element = self.out_encrypt_cert_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_encrypt_cert_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_encrypt_cert_no_list, 'to_alipay_dict'):
                params['out_encrypt_cert_no_list'] = self.out_encrypt_cert_no_list.to_alipay_dict()
            else:
                params['out_encrypt_cert_no_list'] = self.out_encrypt_cert_no_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.solution_type:
            if hasattr(self.solution_type, 'to_alipay_dict'):
                params['solution_type'] = self.solution_type.to_alipay_dict()
            else:
                params['solution_type'] = self.solution_type
        if self.sub_project_id:
            if hasattr(self.sub_project_id, 'to_alipay_dict'):
                params['sub_project_id'] = self.sub_project_id.to_alipay_dict()
            else:
                params['sub_project_id'] = self.sub_project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterPrivacyQueryModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_encrypt_cert_no_list' in d:
            o.out_encrypt_cert_no_list = d['out_encrypt_cert_no_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'solution_type' in d:
            o.solution_type = d['solution_type']
        if 'sub_project_id' in d:
            o.sub_project_id = d['sub_project_id']
        return o


