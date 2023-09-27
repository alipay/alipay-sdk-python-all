#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasOpenIndraccountCreateModel(object):

    def __init__(self):
        self._beneficiary_detail = None
        self._beneficiary_receipt_method = None
        self._request_id = None
        self._scene_type = None

    @property
    def beneficiary_detail(self):
        return self._beneficiary_detail

    @beneficiary_detail.setter
    def beneficiary_detail(self, value):
        self._beneficiary_detail = value
    @property
    def beneficiary_receipt_method(self):
        return self._beneficiary_receipt_method

    @beneficiary_receipt_method.setter
    def beneficiary_receipt_method(self, value):
        self._beneficiary_receipt_method = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_detail:
            if hasattr(self.beneficiary_detail, 'to_alipay_dict'):
                params['beneficiary_detail'] = self.beneficiary_detail.to_alipay_dict()
            else:
                params['beneficiary_detail'] = self.beneficiary_detail
        if self.beneficiary_receipt_method:
            if hasattr(self.beneficiary_receipt_method, 'to_alipay_dict'):
                params['beneficiary_receipt_method'] = self.beneficiary_receipt_method.to_alipay_dict()
            else:
                params['beneficiary_receipt_method'] = self.beneficiary_receipt_method
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndraccountCreateModel()
        if 'beneficiary_detail' in d:
            o.beneficiary_detail = d['beneficiary_detail']
        if 'beneficiary_receipt_method' in d:
            o.beneficiary_receipt_method = d['beneficiary_receipt_method']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


