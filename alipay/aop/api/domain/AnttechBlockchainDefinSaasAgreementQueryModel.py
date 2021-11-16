#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasAgreementQueryModel(object):

    def __init__(self):
        self._out_member_id = None
        self._platform_member_id = None

    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_member_id = value
        else:
            self._out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasAgreementQueryModel()
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


