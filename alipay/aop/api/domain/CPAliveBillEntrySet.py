#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CPAliveBillEntrySet(object):

    def __init__(self):
        self._bill_entry_id = None
        self._status = None

    @property
    def bill_entry_id(self):
        return self._bill_entry_id

    @bill_entry_id.setter
    def bill_entry_id(self, value):
        self._bill_entry_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entry_id:
            if hasattr(self.bill_entry_id, 'to_alipay_dict'):
                params['bill_entry_id'] = self.bill_entry_id.to_alipay_dict()
            else:
                params['bill_entry_id'] = self.bill_entry_id
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
        o = CPAliveBillEntrySet()
        if 'bill_entry_id' in d:
            o.bill_entry_id = d['bill_entry_id']
        if 'status' in d:
            o.status = d['status']
        return o


