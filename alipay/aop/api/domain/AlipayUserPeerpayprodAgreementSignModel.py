#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPeerpayprodAgreementSignModel(object):

    def __init__(self):
        self._alipay_related_uid = None
        self._alipay_user_id = None
        self._quota = None
        self._relation_name = None
        self._request_from = None

    @property
    def alipay_related_uid(self):
        return self._alipay_related_uid

    @alipay_related_uid.setter
    def alipay_related_uid(self, value):
        self._alipay_related_uid = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value
    @property
    def relation_name(self):
        return self._relation_name

    @relation_name.setter
    def relation_name(self, value):
        self._relation_name = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_related_uid:
            if hasattr(self.alipay_related_uid, 'to_alipay_dict'):
                params['alipay_related_uid'] = self.alipay_related_uid.to_alipay_dict()
            else:
                params['alipay_related_uid'] = self.alipay_related_uid
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        if self.relation_name:
            if hasattr(self.relation_name, 'to_alipay_dict'):
                params['relation_name'] = self.relation_name.to_alipay_dict()
            else:
                params['relation_name'] = self.relation_name
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPeerpayprodAgreementSignModel()
        if 'alipay_related_uid' in d:
            o.alipay_related_uid = d['alipay_related_uid']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'quota' in d:
            o.quota = d['quota']
        if 'relation_name' in d:
            o.relation_name = d['relation_name']
        if 'request_from' in d:
            o.request_from = d['request_from']
        return o


