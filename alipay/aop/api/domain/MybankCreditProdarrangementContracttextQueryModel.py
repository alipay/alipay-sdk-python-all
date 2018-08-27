#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditProdarrangementContracttextQueryModel(object):

    def __init__(self):
        self._bsn_no = None
        self._contract_type = None
        self._query_type = None

    @property
    def bsn_no(self):
        return self._bsn_no

    @bsn_no.setter
    def bsn_no(self, value):
        self._bsn_no = value
    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bsn_no:
            if hasattr(self.bsn_no, 'to_alipay_dict'):
                params['bsn_no'] = self.bsn_no.to_alipay_dict()
            else:
                params['bsn_no'] = self.bsn_no
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditProdarrangementContracttextQueryModel()
        if 'bsn_no' in d:
            o.bsn_no = d['bsn_no']
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


