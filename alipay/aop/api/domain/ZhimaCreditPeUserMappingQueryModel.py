#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUserMappingQueryModel(object):

    def __init__(self):
        self._credit_agreement_id = None
        self._is_new_open = None
        self._mapping_type = None
        self._open_id = None
        self._out_request_no = None
        self._service_id = None
        self._user_id = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def is_new_open(self):
        return self._is_new_open

    @is_new_open.setter
    def is_new_open(self, value):
        self._is_new_open = value
    @property
    def mapping_type(self):
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, value):
        self._mapping_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_agreement_id:
            if hasattr(self.credit_agreement_id, 'to_alipay_dict'):
                params['credit_agreement_id'] = self.credit_agreement_id.to_alipay_dict()
            else:
                params['credit_agreement_id'] = self.credit_agreement_id
        if self.is_new_open:
            if hasattr(self.is_new_open, 'to_alipay_dict'):
                params['is_new_open'] = self.is_new_open.to_alipay_dict()
            else:
                params['is_new_open'] = self.is_new_open
        if self.mapping_type:
            if hasattr(self.mapping_type, 'to_alipay_dict'):
                params['mapping_type'] = self.mapping_type.to_alipay_dict()
            else:
                params['mapping_type'] = self.mapping_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUserMappingQueryModel()
        if 'credit_agreement_id' in d:
            o.credit_agreement_id = d['credit_agreement_id']
        if 'is_new_open' in d:
            o.is_new_open = d['is_new_open']
        if 'mapping_type' in d:
            o.mapping_type = d['mapping_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


