#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderSettleTargetDTO(object):

    def __init__(self):
        self._settle_target = None
        self._settle_target_openid = None
        self._settle_target_uid = None
        self._settle_type = None

    @property
    def settle_target(self):
        return self._settle_target

    @settle_target.setter
    def settle_target(self, value):
        self._settle_target = value
    @property
    def settle_target_openid(self):
        return self._settle_target_openid

    @settle_target_openid.setter
    def settle_target_openid(self, value):
        self._settle_target_openid = value
    @property
    def settle_target_uid(self):
        return self._settle_target_uid

    @settle_target_uid.setter
    def settle_target_uid(self, value):
        self._settle_target_uid = value
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_target:
            if hasattr(self.settle_target, 'to_alipay_dict'):
                params['settle_target'] = self.settle_target.to_alipay_dict()
            else:
                params['settle_target'] = self.settle_target
        if self.settle_target_openid:
            if hasattr(self.settle_target_openid, 'to_alipay_dict'):
                params['settle_target_openid'] = self.settle_target_openid.to_alipay_dict()
            else:
                params['settle_target_openid'] = self.settle_target_openid
        if self.settle_target_uid:
            if hasattr(self.settle_target_uid, 'to_alipay_dict'):
                params['settle_target_uid'] = self.settle_target_uid.to_alipay_dict()
            else:
                params['settle_target_uid'] = self.settle_target_uid
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderSettleTargetDTO()
        if 'settle_target' in d:
            o.settle_target = d['settle_target']
        if 'settle_target_openid' in d:
            o.settle_target_openid = d['settle_target_openid']
        if 'settle_target_uid' in d:
            o.settle_target_uid = d['settle_target_uid']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        return o


