#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniProgramExtraInfo import MiniProgramExtraInfo


class AlipayMerchantLifeMiniprogramModifyModel(object):

    def __init__(self):
        self._extra = None
        self._reason = None
        self._request_id = None
        self._status = None

    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        if isinstance(value, MiniProgramExtraInfo):
            self._extra = value
        else:
            self._extra = MiniProgramExtraInfo.from_alipay_dict(value)
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantLifeMiniprogramModifyModel()
        if 'extra' in d:
            o.extra = d['extra']
        if 'reason' in d:
            o.reason = d['reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'status' in d:
            o.status = d['status']
        return o


