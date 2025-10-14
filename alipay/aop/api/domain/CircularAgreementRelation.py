#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CircularAgreementRelation(object):

    def __init__(self):
        self._bind_wallet_id = None
        self._bind_wallet_type = None
        self._relation_openid = None
        self._relation_uid = None
        self._status = None

    @property
    def bind_wallet_id(self):
        return self._bind_wallet_id

    @bind_wallet_id.setter
    def bind_wallet_id(self, value):
        self._bind_wallet_id = value
    @property
    def bind_wallet_type(self):
        return self._bind_wallet_type

    @bind_wallet_type.setter
    def bind_wallet_type(self, value):
        self._bind_wallet_type = value
    @property
    def relation_openid(self):
        return self._relation_openid

    @relation_openid.setter
    def relation_openid(self, value):
        self._relation_openid = value
    @property
    def relation_uid(self):
        return self._relation_uid

    @relation_uid.setter
    def relation_uid(self, value):
        self._relation_uid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_wallet_id:
            if hasattr(self.bind_wallet_id, 'to_alipay_dict'):
                params['bind_wallet_id'] = self.bind_wallet_id.to_alipay_dict()
            else:
                params['bind_wallet_id'] = self.bind_wallet_id
        if self.bind_wallet_type:
            if hasattr(self.bind_wallet_type, 'to_alipay_dict'):
                params['bind_wallet_type'] = self.bind_wallet_type.to_alipay_dict()
            else:
                params['bind_wallet_type'] = self.bind_wallet_type
        if self.relation_openid:
            if hasattr(self.relation_openid, 'to_alipay_dict'):
                params['relation_openid'] = self.relation_openid.to_alipay_dict()
            else:
                params['relation_openid'] = self.relation_openid
        if self.relation_uid:
            if hasattr(self.relation_uid, 'to_alipay_dict'):
                params['relation_uid'] = self.relation_uid.to_alipay_dict()
            else:
                params['relation_uid'] = self.relation_uid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CircularAgreementRelation()
        if 'bind_wallet_id' in d:
            o.bind_wallet_id = d['bind_wallet_id']
        if 'bind_wallet_type' in d:
            o.bind_wallet_type = d['bind_wallet_type']
        if 'relation_openid' in d:
            o.relation_openid = d['relation_openid']
        if 'relation_uid' in d:
            o.relation_uid = d['relation_uid']
        if 'status' in d:
            o.status = d['status']
        return o


