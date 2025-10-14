#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinSignInfo import CarfinSignInfo


class AgreementFullInfo(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_version = None
        self._content = None
        self._contract_no = None
        self._file_id = None
        self._sign_info_list = None
        self._sign_status = None
        self._sign_time = None
        self._title = None
        self._type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_version(self):
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, value):
        self._agreement_version = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def sign_info_list(self):
        return self._sign_info_list

    @sign_info_list.setter
    def sign_info_list(self, value):
        if isinstance(value, list):
            self._sign_info_list = list()
            for i in value:
                if isinstance(i, CarfinSignInfo):
                    self._sign_info_list.append(i)
                else:
                    self._sign_info_list.append(CarfinSignInfo.from_alipay_dict(i))
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
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
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_version:
            if hasattr(self.agreement_version, 'to_alipay_dict'):
                params['agreement_version'] = self.agreement_version.to_alipay_dict()
            else:
                params['agreement_version'] = self.agreement_version
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.sign_info_list:
            if isinstance(self.sign_info_list, list):
                for i in range(0, len(self.sign_info_list)):
                    element = self.sign_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sign_info_list, 'to_alipay_dict'):
                params['sign_info_list'] = self.sign_info_list.to_alipay_dict()
            else:
                params['sign_info_list'] = self.sign_info_list
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
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
        o = AgreementFullInfo()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_version' in d:
            o.agreement_version = d['agreement_version']
        if 'content' in d:
            o.content = d['content']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'sign_info_list' in d:
            o.sign_info_list = d['sign_info_list']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


