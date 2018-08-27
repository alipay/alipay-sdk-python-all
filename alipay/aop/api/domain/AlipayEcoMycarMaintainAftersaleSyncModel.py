#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainAftersaleSyncModel(object):

    def __init__(self):
        self._aftersale_no = None
        self._refuse_reason = None
        self._status = None

    @property
    def aftersale_no(self):
        return self._aftersale_no

    @aftersale_no.setter
    def aftersale_no(self, value):
        self._aftersale_no = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_no:
            if hasattr(self.aftersale_no, 'to_alipay_dict'):
                params['aftersale_no'] = self.aftersale_no.to_alipay_dict()
            else:
                params['aftersale_no'] = self.aftersale_no
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
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
        o = AlipayEcoMycarMaintainAftersaleSyncModel()
        if 'aftersale_no' in d:
            o.aftersale_no = d['aftersale_no']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'status' in d:
            o.status = d['status']
        return o


