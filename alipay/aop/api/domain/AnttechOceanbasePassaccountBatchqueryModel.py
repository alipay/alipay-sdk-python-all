#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassaccountBatchqueryModel(object):

    def __init__(self):
        self._account_names = None
        self._passport_ids = None

    @property
    def account_names(self):
        return self._account_names

    @account_names.setter
    def account_names(self, value):
        if isinstance(value, list):
            self._account_names = list()
            for i in value:
                self._account_names.append(i)
    @property
    def passport_ids(self):
        return self._passport_ids

    @passport_ids.setter
    def passport_ids(self, value):
        if isinstance(value, list):
            self._passport_ids = list()
            for i in value:
                self._passport_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_names:
            if isinstance(self.account_names, list):
                for i in range(0, len(self.account_names)):
                    element = self.account_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_names[i] = element.to_alipay_dict()
            if hasattr(self.account_names, 'to_alipay_dict'):
                params['account_names'] = self.account_names.to_alipay_dict()
            else:
                params['account_names'] = self.account_names
        if self.passport_ids:
            if isinstance(self.passport_ids, list):
                for i in range(0, len(self.passport_ids)):
                    element = self.passport_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passport_ids[i] = element.to_alipay_dict()
            if hasattr(self.passport_ids, 'to_alipay_dict'):
                params['passport_ids'] = self.passport_ids.to_alipay_dict()
            else:
                params['passport_ids'] = self.passport_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePassaccountBatchqueryModel()
        if 'account_names' in d:
            o.account_names = d['account_names']
        if 'passport_ids' in d:
            o.passport_ids = d['passport_ids']
        return o


