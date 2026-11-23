#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportPaymentLabelQueryModel(object):

    def __init__(self):
        self._label_type = None
        self._target_uid = None

    @property
    def label_type(self):
        return self._label_type

    @label_type.setter
    def label_type(self, value):
        self._label_type = value
    @property
    def target_uid(self):
        return self._target_uid

    @target_uid.setter
    def target_uid(self, value):
        self._target_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_type:
            if hasattr(self.label_type, 'to_alipay_dict'):
                params['label_type'] = self.label_type.to_alipay_dict()
            else:
                params['label_type'] = self.label_type
        if self.target_uid:
            if hasattr(self.target_uid, 'to_alipay_dict'):
                params['target_uid'] = self.target_uid.to_alipay_dict()
            else:
                params['target_uid'] = self.target_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportPaymentLabelQueryModel()
        if 'label_type' in d:
            o.label_type = d['label_type']
        if 'target_uid' in d:
            o.target_uid = d['target_uid']
        return o


