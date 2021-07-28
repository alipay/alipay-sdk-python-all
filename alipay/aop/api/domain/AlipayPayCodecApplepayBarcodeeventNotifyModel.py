#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayCodecApplepayBarcodeeventNotifyModel(object):

    def __init__(self):
        self._barcode_identifier = None
        self._event = None
        self._signature = None

    @property
    def barcode_identifier(self):
        return self._barcode_identifier

    @barcode_identifier.setter
    def barcode_identifier(self, value):
        self._barcode_identifier = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode_identifier:
            if hasattr(self.barcode_identifier, 'to_alipay_dict'):
                params['barcode_identifier'] = self.barcode_identifier.to_alipay_dict()
            else:
                params['barcode_identifier'] = self.barcode_identifier
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecApplepayBarcodeeventNotifyModel()
        if 'barcode_identifier' in d:
            o.barcode_identifier = d['barcode_identifier']
        if 'event' in d:
            o.event = d['event']
        if 'signature' in d:
            o.signature = d['signature']
        return o


