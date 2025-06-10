#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsExpressmanCertifyQueryModel(object):

    def __init__(self):
        self._expressman_open_id = None
        self._expressman_user_id = None
        self._logistics_code = None

    @property
    def expressman_open_id(self):
        return self._expressman_open_id

    @expressman_open_id.setter
    def expressman_open_id(self, value):
        self._expressman_open_id = value
    @property
    def expressman_user_id(self):
        return self._expressman_user_id

    @expressman_user_id.setter
    def expressman_user_id(self, value):
        self._expressman_user_id = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.expressman_open_id:
            if hasattr(self.expressman_open_id, 'to_alipay_dict'):
                params['expressman_open_id'] = self.expressman_open_id.to_alipay_dict()
            else:
                params['expressman_open_id'] = self.expressman_open_id
        if self.expressman_user_id:
            if hasattr(self.expressman_user_id, 'to_alipay_dict'):
                params['expressman_user_id'] = self.expressman_user_id.to_alipay_dict()
            else:
                params['expressman_user_id'] = self.expressman_user_id
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsExpressmanCertifyQueryModel()
        if 'expressman_open_id' in d:
            o.expressman_open_id = d['expressman_open_id']
        if 'expressman_user_id' in d:
            o.expressman_user_id = d['expressman_user_id']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        return o


