#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassportBatchqueryModel(object):

    def __init__(self):
        self._passport_ids = None

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
        o = AnttechOceanbasePassportBatchqueryModel()
        if 'passport_ids' in d:
            o.passport_ids = d['passport_ids']
        return o


