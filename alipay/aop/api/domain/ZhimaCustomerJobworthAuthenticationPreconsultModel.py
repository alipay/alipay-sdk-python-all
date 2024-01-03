#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthAuthenticationPreconsultModel(object):

    def __init__(self):
        self._identity_type = None
        self._once_token = None
        self._out_agreement_no = None
        self._query_type = None
        self._zm_service_id = None

    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def once_token(self):
        return self._once_token

    @once_token.setter
    def once_token(self, value):
        self._once_token = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.once_token:
            if hasattr(self.once_token, 'to_alipay_dict'):
                params['once_token'] = self.once_token.to_alipay_dict()
            else:
                params['once_token'] = self.once_token
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthAuthenticationPreconsultModel()
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'once_token' in d:
            o.once_token = d['once_token']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


