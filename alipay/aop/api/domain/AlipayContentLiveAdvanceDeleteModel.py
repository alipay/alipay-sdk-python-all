#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveAdvanceDeleteModel(object):

    def __init__(self):
        self._alipay_advance_id = None
        self._alipay_public_id = None
        self._reason = None

    @property
    def alipay_advance_id(self):
        return self._alipay_advance_id

    @alipay_advance_id.setter
    def alipay_advance_id(self, value):
        self._alipay_advance_id = value
    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_advance_id:
            if hasattr(self.alipay_advance_id, 'to_alipay_dict'):
                params['alipay_advance_id'] = self.alipay_advance_id.to_alipay_dict()
            else:
                params['alipay_advance_id'] = self.alipay_advance_id
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveAdvanceDeleteModel()
        if 'alipay_advance_id' in d:
            o.alipay_advance_id = d['alipay_advance_id']
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'reason' in d:
            o.reason = d['reason']
        return o


