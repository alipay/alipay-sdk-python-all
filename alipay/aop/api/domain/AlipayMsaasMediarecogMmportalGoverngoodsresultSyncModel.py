#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GovernGoodsCheckMessage import GovernGoodsCheckMessage


class AlipayMsaasMediarecogMmportalGoverngoodsresultSyncModel(object):

    def __init__(self):
        self._algorithm_id = None
        self._check_message = None
        self._check_success = None
        self._req_id = None

    @property
    def algorithm_id(self):
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, value):
        self._algorithm_id = value
    @property
    def check_message(self):
        return self._check_message

    @check_message.setter
    def check_message(self, value):
        if isinstance(value, list):
            self._check_message = list()
            for i in value:
                if isinstance(i, GovernGoodsCheckMessage):
                    self._check_message.append(i)
                else:
                    self._check_message.append(GovernGoodsCheckMessage.from_alipay_dict(i))
    @property
    def check_success(self):
        return self._check_success

    @check_success.setter
    def check_success(self, value):
        self._check_success = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_id:
            if hasattr(self.algorithm_id, 'to_alipay_dict'):
                params['algorithm_id'] = self.algorithm_id.to_alipay_dict()
            else:
                params['algorithm_id'] = self.algorithm_id
        if self.check_message:
            if isinstance(self.check_message, list):
                for i in range(0, len(self.check_message)):
                    element = self.check_message[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_message[i] = element.to_alipay_dict()
            if hasattr(self.check_message, 'to_alipay_dict'):
                params['check_message'] = self.check_message.to_alipay_dict()
            else:
                params['check_message'] = self.check_message
        if self.check_success:
            if hasattr(self.check_success, 'to_alipay_dict'):
                params['check_success'] = self.check_success.to_alipay_dict()
            else:
                params['check_success'] = self.check_success
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalGoverngoodsresultSyncModel()
        if 'algorithm_id' in d:
            o.algorithm_id = d['algorithm_id']
        if 'check_message' in d:
            o.check_message = d['check_message']
        if 'check_success' in d:
            o.check_success = d['check_success']
        if 'req_id' in d:
            o.req_id = d['req_id']
        return o


