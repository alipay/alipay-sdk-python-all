#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateInstanceDownloadModel(object):

    def __init__(self):
        self._duration = None
        self._required_validate = None
        self._type = None
        self._voucher_id = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def required_validate(self):
        return self._required_validate

    @required_validate.setter
    def required_validate(self, value):
        self._required_validate = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.required_validate:
            if hasattr(self.required_validate, 'to_alipay_dict'):
                params['required_validate'] = self.required_validate.to_alipay_dict()
            else:
                params['required_validate'] = self.required_validate
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateInstanceDownloadModel()
        if 'duration' in d:
            o.duration = d['duration']
        if 'required_validate' in d:
            o.required_validate = d['required_validate']
        if 'type' in d:
            o.type = d['type']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


