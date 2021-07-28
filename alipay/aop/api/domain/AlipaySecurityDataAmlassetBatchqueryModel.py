#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataAmlassetBatchqueryModel(object):

    def __init__(self):
        self._asset_type = None
        self._client = None
        self._lid = None
        self._uids = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value
    @property
    def lid(self):
        return self._lid

    @lid.setter
    def lid(self, value):
        self._lid = value
    @property
    def uids(self):
        return self._uids

    @uids.setter
    def uids(self, value):
        if isinstance(value, list):
            self._uids = list()
            for i in value:
                self._uids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.client:
            if hasattr(self.client, 'to_alipay_dict'):
                params['client'] = self.client.to_alipay_dict()
            else:
                params['client'] = self.client
        if self.lid:
            if hasattr(self.lid, 'to_alipay_dict'):
                params['lid'] = self.lid.to_alipay_dict()
            else:
                params['lid'] = self.lid
        if self.uids:
            if isinstance(self.uids, list):
                for i in range(0, len(self.uids)):
                    element = self.uids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uids[i] = element.to_alipay_dict()
            if hasattr(self.uids, 'to_alipay_dict'):
                params['uids'] = self.uids.to_alipay_dict()
            else:
                params['uids'] = self.uids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataAmlassetBatchqueryModel()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'client' in d:
            o.client = d['client']
        if 'lid' in d:
            o.lid = d['lid']
        if 'uids' in d:
            o.uids = d['uids']
        return o


