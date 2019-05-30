#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceSgxGatewayQueryModel(object):

    def __init__(self):
        self._biz_handler = None
        self._biz_handler_input = None
        self._institution_uuid = None
        self._request_uuid = None

    @property
    def biz_handler(self):
        return self._biz_handler

    @biz_handler.setter
    def biz_handler(self, value):
        self._biz_handler = value
    @property
    def biz_handler_input(self):
        return self._biz_handler_input

    @biz_handler_input.setter
    def biz_handler_input(self, value):
        self._biz_handler_input = value
    @property
    def institution_uuid(self):
        return self._institution_uuid

    @institution_uuid.setter
    def institution_uuid(self, value):
        self._institution_uuid = value
    @property
    def request_uuid(self):
        return self._request_uuid

    @request_uuid.setter
    def request_uuid(self, value):
        self._request_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_handler:
            if hasattr(self.biz_handler, 'to_alipay_dict'):
                params['biz_handler'] = self.biz_handler.to_alipay_dict()
            else:
                params['biz_handler'] = self.biz_handler
        if self.biz_handler_input:
            if hasattr(self.biz_handler_input, 'to_alipay_dict'):
                params['biz_handler_input'] = self.biz_handler_input.to_alipay_dict()
            else:
                params['biz_handler_input'] = self.biz_handler_input
        if self.institution_uuid:
            if hasattr(self.institution_uuid, 'to_alipay_dict'):
                params['institution_uuid'] = self.institution_uuid.to_alipay_dict()
            else:
                params['institution_uuid'] = self.institution_uuid
        if self.request_uuid:
            if hasattr(self.request_uuid, 'to_alipay_dict'):
                params['request_uuid'] = self.request_uuid.to_alipay_dict()
            else:
                params['request_uuid'] = self.request_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceSgxGatewayQueryModel()
        if 'biz_handler' in d:
            o.biz_handler = d['biz_handler']
        if 'biz_handler_input' in d:
            o.biz_handler_input = d['biz_handler_input']
        if 'institution_uuid' in d:
            o.institution_uuid = d['institution_uuid']
        if 'request_uuid' in d:
            o.request_uuid = d['request_uuid']
        return o


