#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehicleownerTransdataSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._trans_data = None
        self._uid = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def trans_data(self):
        return self._trans_data

    @trans_data.setter
    def trans_data(self, value):
        self._trans_data = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.trans_data:
            if hasattr(self.trans_data, 'to_alipay_dict'):
                params['trans_data'] = self.trans_data.to_alipay_dict()
            else:
                params['trans_data'] = self.trans_data
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerTransdataSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'trans_data' in d:
            o.trans_data = d['trans_data']
        if 'uid' in d:
            o.uid = d['uid']
        return o


