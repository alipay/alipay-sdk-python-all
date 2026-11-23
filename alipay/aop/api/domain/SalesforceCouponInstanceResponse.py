#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SalesforceCouponInstanceAttributes import SalesforceCouponInstanceAttributes


class SalesforceCouponInstanceResponse(object):

    def __init__(self):
        self._attributes = None
        self._label = None
        self._value = None

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, SalesforceCouponInstanceAttributes):
            self._attributes = value
        else:
            self._attributes = SalesforceCouponInstanceAttributes.from_alipay_dict(value)
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.attributes:
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
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
        o = SalesforceCouponInstanceResponse()
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'label' in d:
            o.label = d['label']
        if 'value' in d:
            o.value = d['value']
        return o


