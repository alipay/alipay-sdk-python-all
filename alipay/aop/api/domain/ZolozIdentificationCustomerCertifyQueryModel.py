#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozIdentificationCustomerCertifyQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._zim_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.zim_id:
            if hasattr(self.zim_id, 'to_alipay_dict'):
                params['zim_id'] = self.zim_id.to_alipay_dict()
            else:
                params['zim_id'] = self.zim_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationCustomerCertifyQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'zim_id' in d:
            o.zim_id = d['zim_id']
        return o


