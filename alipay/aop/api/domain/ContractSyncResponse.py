#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractSyncResponse(object):

    def __init__(self):
        self._accept_id = None

    @property
    def accept_id(self):
        return self._accept_id

    @accept_id.setter
    def accept_id(self, value):
        self._accept_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_id:
            if hasattr(self.accept_id, 'to_alipay_dict'):
                params['accept_id'] = self.accept_id.to_alipay_dict()
            else:
                params['accept_id'] = self.accept_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractSyncResponse()
        if 'accept_id' in d:
            o.accept_id = d['accept_id']
        return o


