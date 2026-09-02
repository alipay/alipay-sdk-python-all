#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSmsSendModel(object):

    def __init__(self):
        self._fulfill_order_id = None
        self._source = None
        self._template_id = None
        self._template_value = None

    @property
    def fulfill_order_id(self):
        return self._fulfill_order_id

    @fulfill_order_id.setter
    def fulfill_order_id(self, value):
        self._fulfill_order_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_value(self):
        return self._template_value

    @template_value.setter
    def template_value(self, value):
        self._template_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfill_order_id:
            if hasattr(self.fulfill_order_id, 'to_alipay_dict'):
                params['fulfill_order_id'] = self.fulfill_order_id.to_alipay_dict()
            else:
                params['fulfill_order_id'] = self.fulfill_order_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_value:
            if hasattr(self.template_value, 'to_alipay_dict'):
                params['template_value'] = self.template_value.to_alipay_dict()
            else:
                params['template_value'] = self.template_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSmsSendModel()
        if 'fulfill_order_id' in d:
            o.fulfill_order_id = d['fulfill_order_id']
        if 'source' in d:
            o.source = d['source']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_value' in d:
            o.template_value = d['template_value']
        return o


