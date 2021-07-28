#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossContractManagementQueryModel(object):

    def __init__(self):
        self._biz_source = None
        self._contract_batch_no = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def contract_batch_no(self):
        return self._contract_batch_no

    @contract_batch_no.setter
    def contract_batch_no(self, value):
        self._contract_batch_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.contract_batch_no:
            if hasattr(self.contract_batch_no, 'to_alipay_dict'):
                params['contract_batch_no'] = self.contract_batch_no.to_alipay_dict()
            else:
                params['contract_batch_no'] = self.contract_batch_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossContractManagementQueryModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'contract_batch_no' in d:
            o.contract_batch_no = d['contract_batch_no']
        return o


