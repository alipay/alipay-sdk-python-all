#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoDetailLoanInfo import EcoDetailLoanInfo


class EcoContractDetailInfo(object):

    def __init__(self):
        self._is_free_portion = None
        self._jump_url = None
        self._loan_info = None
        self._source = None

    @property
    def is_free_portion(self):
        return self._is_free_portion

    @is_free_portion.setter
    def is_free_portion(self, value):
        self._is_free_portion = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def loan_info(self):
        return self._loan_info

    @loan_info.setter
    def loan_info(self, value):
        if isinstance(value, EcoDetailLoanInfo):
            self._loan_info = value
        else:
            self._loan_info = EcoDetailLoanInfo.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_free_portion:
            if hasattr(self.is_free_portion, 'to_alipay_dict'):
                params['is_free_portion'] = self.is_free_portion.to_alipay_dict()
            else:
                params['is_free_portion'] = self.is_free_portion
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.loan_info:
            if hasattr(self.loan_info, 'to_alipay_dict'):
                params['loan_info'] = self.loan_info.to_alipay_dict()
            else:
                params['loan_info'] = self.loan_info
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoContractDetailInfo()
        if 'is_free_portion' in d:
            o.is_free_portion = d['is_free_portion']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'loan_info' in d:
            o.loan_info = d['loan_info']
        if 'source' in d:
            o.source = d['source']
        return o


