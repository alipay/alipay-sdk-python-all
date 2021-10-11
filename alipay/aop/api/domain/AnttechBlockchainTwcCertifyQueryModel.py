#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainTwcCertifyQueryModel(object):

    def __init__(self):
        self._certify_id = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_id:
            if hasattr(self.certify_id, 'to_alipay_dict'):
                params['certify_id'] = self.certify_id.to_alipay_dict()
            else:
                params['certify_id'] = self.certify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainTwcCertifyQueryModel()
        if 'certify_id' in d:
            o.certify_id = d['certify_id']
        return o


