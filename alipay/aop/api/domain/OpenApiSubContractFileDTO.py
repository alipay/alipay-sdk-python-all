#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO


class OpenApiSubContractFileDTO(object):

    def __init__(self):
        self._attachment_file_name = None
        self._attachment_path = None
        self._attachment_url = None
        self._confirm_date = None
        self._confirmer = None
        self._file_version = None
        self._sub_contract_code = None
        self._sub_contract_name = None
        self._sub_contract_status = None
        self._submitter = None
        self._up_load_time = None

    @property
    def attachment_file_name(self):
        return self._attachment_file_name

    @attachment_file_name.setter
    def attachment_file_name(self, value):
        self._attachment_file_name = value
    @property
    def attachment_path(self):
        return self._attachment_path

    @attachment_path.setter
    def attachment_path(self, value):
        self._attachment_path = value
    @property
    def attachment_url(self):
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, value):
        self._attachment_url = value
    @property
    def confirm_date(self):
        return self._confirm_date

    @confirm_date.setter
    def confirm_date(self, value):
        self._confirm_date = value
    @property
    def confirmer(self):
        return self._confirmer

    @confirmer.setter
    def confirmer(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._confirmer = value
        else:
            self._confirmer = OpenApiPersonSaDTO.from_alipay_dict(value)
    @property
    def file_version(self):
        return self._file_version

    @file_version.setter
    def file_version(self, value):
        self._file_version = value
    @property
    def sub_contract_code(self):
        return self._sub_contract_code

    @sub_contract_code.setter
    def sub_contract_code(self, value):
        self._sub_contract_code = value
    @property
    def sub_contract_name(self):
        return self._sub_contract_name

    @sub_contract_name.setter
    def sub_contract_name(self, value):
        self._sub_contract_name = value
    @property
    def sub_contract_status(self):
        return self._sub_contract_status

    @sub_contract_status.setter
    def sub_contract_status(self, value):
        self._sub_contract_status = value
    @property
    def submitter(self):
        return self._submitter

    @submitter.setter
    def submitter(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._submitter = value
        else:
            self._submitter = OpenApiPersonSaDTO.from_alipay_dict(value)
    @property
    def up_load_time(self):
        return self._up_load_time

    @up_load_time.setter
    def up_load_time(self, value):
        self._up_load_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_file_name:
            if hasattr(self.attachment_file_name, 'to_alipay_dict'):
                params['attachment_file_name'] = self.attachment_file_name.to_alipay_dict()
            else:
                params['attachment_file_name'] = self.attachment_file_name
        if self.attachment_path:
            if hasattr(self.attachment_path, 'to_alipay_dict'):
                params['attachment_path'] = self.attachment_path.to_alipay_dict()
            else:
                params['attachment_path'] = self.attachment_path
        if self.attachment_url:
            if hasattr(self.attachment_url, 'to_alipay_dict'):
                params['attachment_url'] = self.attachment_url.to_alipay_dict()
            else:
                params['attachment_url'] = self.attachment_url
        if self.confirm_date:
            if hasattr(self.confirm_date, 'to_alipay_dict'):
                params['confirm_date'] = self.confirm_date.to_alipay_dict()
            else:
                params['confirm_date'] = self.confirm_date
        if self.confirmer:
            if hasattr(self.confirmer, 'to_alipay_dict'):
                params['confirmer'] = self.confirmer.to_alipay_dict()
            else:
                params['confirmer'] = self.confirmer
        if self.file_version:
            if hasattr(self.file_version, 'to_alipay_dict'):
                params['file_version'] = self.file_version.to_alipay_dict()
            else:
                params['file_version'] = self.file_version
        if self.sub_contract_code:
            if hasattr(self.sub_contract_code, 'to_alipay_dict'):
                params['sub_contract_code'] = self.sub_contract_code.to_alipay_dict()
            else:
                params['sub_contract_code'] = self.sub_contract_code
        if self.sub_contract_name:
            if hasattr(self.sub_contract_name, 'to_alipay_dict'):
                params['sub_contract_name'] = self.sub_contract_name.to_alipay_dict()
            else:
                params['sub_contract_name'] = self.sub_contract_name
        if self.sub_contract_status:
            if hasattr(self.sub_contract_status, 'to_alipay_dict'):
                params['sub_contract_status'] = self.sub_contract_status.to_alipay_dict()
            else:
                params['sub_contract_status'] = self.sub_contract_status
        if self.submitter:
            if hasattr(self.submitter, 'to_alipay_dict'):
                params['submitter'] = self.submitter.to_alipay_dict()
            else:
                params['submitter'] = self.submitter
        if self.up_load_time:
            if hasattr(self.up_load_time, 'to_alipay_dict'):
                params['up_load_time'] = self.up_load_time.to_alipay_dict()
            else:
                params['up_load_time'] = self.up_load_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSubContractFileDTO()
        if 'attachment_file_name' in d:
            o.attachment_file_name = d['attachment_file_name']
        if 'attachment_path' in d:
            o.attachment_path = d['attachment_path']
        if 'attachment_url' in d:
            o.attachment_url = d['attachment_url']
        if 'confirm_date' in d:
            o.confirm_date = d['confirm_date']
        if 'confirmer' in d:
            o.confirmer = d['confirmer']
        if 'file_version' in d:
            o.file_version = d['file_version']
        if 'sub_contract_code' in d:
            o.sub_contract_code = d['sub_contract_code']
        if 'sub_contract_name' in d:
            o.sub_contract_name = d['sub_contract_name']
        if 'sub_contract_status' in d:
            o.sub_contract_status = d['sub_contract_status']
        if 'submitter' in d:
            o.submitter = d['submitter']
        if 'up_load_time' in d:
            o.up_load_time = d['up_load_time']
        return o


