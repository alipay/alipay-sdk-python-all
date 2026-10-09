#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PassAccountNameHashRecordDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_type = None
        self._conflict_type = None
        self._data_source = None
        self._modified_time = None
        self._name_hash_status = None
        self._pass_account_id = None
        self._passport_id = None
        self._related_account_names = None
        self._related_pass_account_ids = None
        self._related_passport_ids = None
        self._status = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def conflict_type(self):
        return self._conflict_type

    @conflict_type.setter
    def conflict_type(self, value):
        self._conflict_type = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def name_hash_status(self):
        return self._name_hash_status

    @name_hash_status.setter
    def name_hash_status(self, value):
        self._name_hash_status = value
    @property
    def pass_account_id(self):
        return self._pass_account_id

    @pass_account_id.setter
    def pass_account_id(self, value):
        self._pass_account_id = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def related_account_names(self):
        return self._related_account_names

    @related_account_names.setter
    def related_account_names(self, value):
        self._related_account_names = value
    @property
    def related_pass_account_ids(self):
        return self._related_pass_account_ids

    @related_pass_account_ids.setter
    def related_pass_account_ids(self, value):
        self._related_pass_account_ids = value
    @property
    def related_passport_ids(self):
        return self._related_passport_ids

    @related_passport_ids.setter
    def related_passport_ids(self, value):
        self._related_passport_ids = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.conflict_type:
            if hasattr(self.conflict_type, 'to_alipay_dict'):
                params['conflict_type'] = self.conflict_type.to_alipay_dict()
            else:
                params['conflict_type'] = self.conflict_type
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.name_hash_status:
            if hasattr(self.name_hash_status, 'to_alipay_dict'):
                params['name_hash_status'] = self.name_hash_status.to_alipay_dict()
            else:
                params['name_hash_status'] = self.name_hash_status
        if self.pass_account_id:
            if hasattr(self.pass_account_id, 'to_alipay_dict'):
                params['pass_account_id'] = self.pass_account_id.to_alipay_dict()
            else:
                params['pass_account_id'] = self.pass_account_id
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.related_account_names:
            if hasattr(self.related_account_names, 'to_alipay_dict'):
                params['related_account_names'] = self.related_account_names.to_alipay_dict()
            else:
                params['related_account_names'] = self.related_account_names
        if self.related_pass_account_ids:
            if hasattr(self.related_pass_account_ids, 'to_alipay_dict'):
                params['related_pass_account_ids'] = self.related_pass_account_ids.to_alipay_dict()
            else:
                params['related_pass_account_ids'] = self.related_pass_account_ids
        if self.related_passport_ids:
            if hasattr(self.related_passport_ids, 'to_alipay_dict'):
                params['related_passport_ids'] = self.related_passport_ids.to_alipay_dict()
            else:
                params['related_passport_ids'] = self.related_passport_ids
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassAccountNameHashRecordDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'conflict_type' in d:
            o.conflict_type = d['conflict_type']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'name_hash_status' in d:
            o.name_hash_status = d['name_hash_status']
        if 'pass_account_id' in d:
            o.pass_account_id = d['pass_account_id']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'related_account_names' in d:
            o.related_account_names = d['related_account_names']
        if 'related_pass_account_ids' in d:
            o.related_pass_account_ids = d['related_pass_account_ids']
        if 'related_passport_ids' in d:
            o.related_passport_ids = d['related_passport_ids']
        if 'status' in d:
            o.status = d['status']
        return o


