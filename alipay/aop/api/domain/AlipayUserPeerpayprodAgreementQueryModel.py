#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPeerpayprodAgreementQueryModel(object):

    def __init__(self):
        self._alipay_related_uid = None
        self._alipay_user_id = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPeerpayprodAgreementQueryModel()
        if 'alipay_related_uid' in d:
            o.alipay_related_uid = d['alipay_related_uid']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        return o


