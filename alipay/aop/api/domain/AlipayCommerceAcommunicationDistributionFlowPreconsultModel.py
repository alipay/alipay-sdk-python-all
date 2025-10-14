#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDistributionFlowPreconsultModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._encrypted_mobile = None
        self._item_id = None
        self._mobile = None
        self._open_id = None
        self._request_id = None
        self._target_account = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def target_account(self):
        return self._target_account

    @target_account.setter
    def target_account(self, value):
        self._target_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.target_account:
            if hasattr(self.target_account, 'to_alipay_dict'):
                params['target_account'] = self.target_account.to_alipay_dict()
            else:
                params['target_account'] = self.target_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionFlowPreconsultModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'target_account' in d:
            o.target_account = d['target_account']
        return o


