#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoContractProcessDeleteModel(object):

    def __init__(self):
        self._batch_no = None
        self._flow_ids = None
        self._sign_platform_code = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def flow_ids(self):
        return self._flow_ids

    @flow_ids.setter
    def flow_ids(self, value):
        if isinstance(value, list):
            self._flow_ids = list()
            for i in value:
                self._flow_ids.append(i)
    @property
    def sign_platform_code(self):
        return self._sign_platform_code

    @sign_platform_code.setter
    def sign_platform_code(self, value):
        self._sign_platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.flow_ids:
            if isinstance(self.flow_ids, list):
                for i in range(0, len(self.flow_ids)):
                    element = self.flow_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.flow_ids[i] = element.to_alipay_dict()
            if hasattr(self.flow_ids, 'to_alipay_dict'):
                params['flow_ids'] = self.flow_ids.to_alipay_dict()
            else:
                params['flow_ids'] = self.flow_ids
        if self.sign_platform_code:
            if hasattr(self.sign_platform_code, 'to_alipay_dict'):
                params['sign_platform_code'] = self.sign_platform_code.to_alipay_dict()
            else:
                params['sign_platform_code'] = self.sign_platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractProcessDeleteModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'flow_ids' in d:
            o.flow_ids = d['flow_ids']
        if 'sign_platform_code' in d:
            o.sign_platform_code = d['sign_platform_code']
        return o


