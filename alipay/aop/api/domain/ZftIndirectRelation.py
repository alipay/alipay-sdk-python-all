#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZftIndirectRelation(object):

    def __init__(self):
        self._memo = None
        self._relation_openid = None
        self._relation_uid = None
        self._status = None
        self._sub_confirm = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    @property
    def sub_confirm(self):
        return self._sub_confirm

    @sub_confirm.setter
    def sub_confirm(self, value):
        self._sub_confirm = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.sub_confirm:
            if hasattr(self.sub_confirm, 'to_alipay_dict'):
                params['sub_confirm'] = self.sub_confirm.to_alipay_dict()
            else:
                params['sub_confirm'] = self.sub_confirm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZftIndirectRelation()
        if 'memo' in d:
            o.memo = d['memo']
        if 'relation_openid' in d:
            o.relation_openid = d['relation_openid']
        if 'relation_uid' in d:
            o.relation_uid = d['relation_uid']
        if 'status' in d:
            o.status = d['status']
        if 'sub_confirm' in d:
            o.sub_confirm = d['sub_confirm']
        return o


