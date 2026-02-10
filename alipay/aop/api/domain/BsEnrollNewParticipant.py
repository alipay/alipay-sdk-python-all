#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsEnrollParticipantExtInfo import BsEnrollParticipantExtInfo


class BsEnrollNewParticipant(object):

    def __init__(self):
        self._ext_info = None
        self._out_merchant_no = None
        self._type = None
        self._value = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, BsEnrollParticipantExtInfo):
            self._ext_info = value
        else:
            self._ext_info = BsEnrollParticipantExtInfo.from_alipay_dict(value)
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_merchant_no:
            if hasattr(self.out_merchant_no, 'to_alipay_dict'):
                params['out_merchant_no'] = self.out_merchant_no.to_alipay_dict()
            else:
                params['out_merchant_no'] = self.out_merchant_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsEnrollNewParticipant()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_merchant_no' in d:
            o.out_merchant_no = d['out_merchant_no']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


