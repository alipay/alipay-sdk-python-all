#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvInnermanualinfoNotifyModel(object):

    def __init__(self):
        self._external_reason = None
        self._manual_type = None
        self._transaction_id = None

    @property
    def external_reason(self):
        return self._external_reason

    @external_reason.setter
    def external_reason(self, value):
        self._external_reason = value
    @property
    def manual_type(self):
        return self._manual_type

    @manual_type.setter
    def manual_type(self, value):
        self._manual_type = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_reason:
            if hasattr(self.external_reason, 'to_alipay_dict'):
                params['external_reason'] = self.external_reason.to_alipay_dict()
            else:
                params['external_reason'] = self.external_reason
        if self.manual_type:
            if hasattr(self.manual_type, 'to_alipay_dict'):
                params['manual_type'] = self.manual_type.to_alipay_dict()
            else:
                params['manual_type'] = self.manual_type
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvInnermanualinfoNotifyModel()
        if 'external_reason' in d:
            o.external_reason = d['external_reason']
        if 'manual_type' in d:
            o.manual_type = d['manual_type']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


