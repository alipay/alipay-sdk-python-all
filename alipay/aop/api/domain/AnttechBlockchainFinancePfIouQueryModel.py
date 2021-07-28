#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinancePfIouQueryModel(object):

    def __init__(self):
        self._client_no = None
        self._debit_id = None
        self._financing_id = None
        self._parm = None
        self._platform_id = None

    @property
    def client_no(self):
        return self._client_no

    @client_no.setter
    def client_no(self, value):
        self._client_no = value
    @property
    def debit_id(self):
        return self._debit_id

    @debit_id.setter
    def debit_id(self, value):
        self._debit_id = value
    @property
    def financing_id(self):
        return self._financing_id

    @financing_id.setter
    def financing_id(self, value):
        self._financing_id = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_no:
            if hasattr(self.client_no, 'to_alipay_dict'):
                params['client_no'] = self.client_no.to_alipay_dict()
            else:
                params['client_no'] = self.client_no
        if self.debit_id:
            if hasattr(self.debit_id, 'to_alipay_dict'):
                params['debit_id'] = self.debit_id.to_alipay_dict()
            else:
                params['debit_id'] = self.debit_id
        if self.financing_id:
            if hasattr(self.financing_id, 'to_alipay_dict'):
                params['financing_id'] = self.financing_id.to_alipay_dict()
            else:
                params['financing_id'] = self.financing_id
        if self.parm:
            if hasattr(self.parm, 'to_alipay_dict'):
                params['parm'] = self.parm.to_alipay_dict()
            else:
                params['parm'] = self.parm
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinancePfIouQueryModel()
        if 'client_no' in d:
            o.client_no = d['client_no']
        if 'debit_id' in d:
            o.debit_id = d['debit_id']
        if 'financing_id' in d:
            o.financing_id = d['financing_id']
        if 'parm' in d:
            o.parm = d['parm']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


