#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderBroadcastCoilBindModel(object):

    def __init__(self):
        self._nfc_url = None
        self._operator_id = None
        self._route_url = None
        self._smid = None
        self._tag_sn = None

    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        self._nfc_url = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        self._route_url = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def tag_sn(self):
        return self._tag_sn

    @tag_sn.setter
    def tag_sn(self, value):
        self._tag_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.nfc_url:
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.route_url:
            if hasattr(self.route_url, 'to_alipay_dict'):
                params['route_url'] = self.route_url.to_alipay_dict()
            else:
                params['route_url'] = self.route_url
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.tag_sn:
            if hasattr(self.tag_sn, 'to_alipay_dict'):
                params['tag_sn'] = self.tag_sn.to_alipay_dict()
            else:
                params['tag_sn'] = self.tag_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderBroadcastCoilBindModel()
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'route_url' in d:
            o.route_url = d['route_url']
        if 'smid' in d:
            o.smid = d['smid']
        if 'tag_sn' in d:
            o.tag_sn = d['tag_sn']
        return o


