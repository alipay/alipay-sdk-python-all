#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoSignFlowCancelModel(object):

    def __init__(self):
        self._flow_id = None
        self._revoke_reason = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def revoke_reason(self):
        return self._revoke_reason

    @revoke_reason.setter
    def revoke_reason(self, value):
        self._revoke_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.revoke_reason:
            if hasattr(self.revoke_reason, 'to_alipay_dict'):
                params['revoke_reason'] = self.revoke_reason.to_alipay_dict()
            else:
                params['revoke_reason'] = self.revoke_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoSignFlowCancelModel()
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'revoke_reason' in d:
            o.revoke_reason = d['revoke_reason']
        return o


