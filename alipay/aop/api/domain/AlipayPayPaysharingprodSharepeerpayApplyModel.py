#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SharePeerPaySecurityInfo import SharePeerPaySecurityInfo


class AlipayPayPaysharingprodSharepeerpayApplyModel(object):

    def __init__(self):
        self._alipay_applyer_id = None
        self._alipay_trade_no = None
        self._external_user_token = None
        self._security_info = None

    @property
    def alipay_applyer_id(self):
        return self._alipay_applyer_id

    @alipay_applyer_id.setter
    def alipay_applyer_id(self, value):
        self._alipay_applyer_id = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def external_user_token(self):
        return self._external_user_token

    @external_user_token.setter
    def external_user_token(self, value):
        self._external_user_token = value
    @property
    def security_info(self):
        return self._security_info

    @security_info.setter
    def security_info(self, value):
        if isinstance(value, SharePeerPaySecurityInfo):
            self._security_info = value
        else:
            self._security_info = SharePeerPaySecurityInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_applyer_id:
            if hasattr(self.alipay_applyer_id, 'to_alipay_dict'):
                params['alipay_applyer_id'] = self.alipay_applyer_id.to_alipay_dict()
            else:
                params['alipay_applyer_id'] = self.alipay_applyer_id
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.external_user_token:
            if hasattr(self.external_user_token, 'to_alipay_dict'):
                params['external_user_token'] = self.external_user_token.to_alipay_dict()
            else:
                params['external_user_token'] = self.external_user_token
        if self.security_info:
            if hasattr(self.security_info, 'to_alipay_dict'):
                params['security_info'] = self.security_info.to_alipay_dict()
            else:
                params['security_info'] = self.security_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayPaysharingprodSharepeerpayApplyModel()
        if 'alipay_applyer_id' in d:
            o.alipay_applyer_id = d['alipay_applyer_id']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'external_user_token' in d:
            o.external_user_token = d['external_user_token']
        if 'security_info' in d:
            o.security_info = d['security_info']
        return o


