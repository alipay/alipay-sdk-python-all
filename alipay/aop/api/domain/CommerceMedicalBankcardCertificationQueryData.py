#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommerceMedicalBankcardCertificationQueryData(object):

    def __init__(self):
        self._gmt_response = None
        self._is_bankcard_certified = None

    @property
    def gmt_response(self):
        return self._gmt_response

    @gmt_response.setter
    def gmt_response(self, value):
        self._gmt_response = value
    @property
    def is_bankcard_certified(self):
        return self._is_bankcard_certified

    @is_bankcard_certified.setter
    def is_bankcard_certified(self, value):
        self._is_bankcard_certified = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_response:
            if hasattr(self.gmt_response, 'to_alipay_dict'):
                params['gmt_response'] = self.gmt_response.to_alipay_dict()
            else:
                params['gmt_response'] = self.gmt_response
        if self.is_bankcard_certified:
            if hasattr(self.is_bankcard_certified, 'to_alipay_dict'):
                params['is_bankcard_certified'] = self.is_bankcard_certified.to_alipay_dict()
            else:
                params['is_bankcard_certified'] = self.is_bankcard_certified
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommerceMedicalBankcardCertificationQueryData()
        if 'gmt_response' in d:
            o.gmt_response = d['gmt_response']
        if 'is_bankcard_certified' in d:
            o.is_bankcard_certified = d['is_bankcard_certified']
        return o


