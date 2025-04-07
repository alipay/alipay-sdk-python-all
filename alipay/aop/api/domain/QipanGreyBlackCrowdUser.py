#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QipanGreyBlackCrowdUser(object):

    def __init__(self):
        self._encrypt_alipay_id = None
        self._encrypt_identity_card_id = None
        self._encrypt_mobile_id = None
        self._encrypt_type = None
        self._storage_time = None
        self._trade_no = None
        self._user_tags = None

    @property
    def encrypt_alipay_id(self):
        return self._encrypt_alipay_id

    @encrypt_alipay_id.setter
    def encrypt_alipay_id(self, value):
        self._encrypt_alipay_id = value
    @property
    def encrypt_identity_card_id(self):
        return self._encrypt_identity_card_id

    @encrypt_identity_card_id.setter
    def encrypt_identity_card_id(self, value):
        self._encrypt_identity_card_id = value
    @property
    def encrypt_mobile_id(self):
        return self._encrypt_mobile_id

    @encrypt_mobile_id.setter
    def encrypt_mobile_id(self, value):
        self._encrypt_mobile_id = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def storage_time(self):
        return self._storage_time

    @storage_time.setter
    def storage_time(self, value):
        self._storage_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_tags(self):
        return self._user_tags

    @user_tags.setter
    def user_tags(self, value):
        self._user_tags = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_alipay_id:
            if hasattr(self.encrypt_alipay_id, 'to_alipay_dict'):
                params['encrypt_alipay_id'] = self.encrypt_alipay_id.to_alipay_dict()
            else:
                params['encrypt_alipay_id'] = self.encrypt_alipay_id
        if self.encrypt_identity_card_id:
            if hasattr(self.encrypt_identity_card_id, 'to_alipay_dict'):
                params['encrypt_identity_card_id'] = self.encrypt_identity_card_id.to_alipay_dict()
            else:
                params['encrypt_identity_card_id'] = self.encrypt_identity_card_id
        if self.encrypt_mobile_id:
            if hasattr(self.encrypt_mobile_id, 'to_alipay_dict'):
                params['encrypt_mobile_id'] = self.encrypt_mobile_id.to_alipay_dict()
            else:
                params['encrypt_mobile_id'] = self.encrypt_mobile_id
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.storage_time:
            if hasattr(self.storage_time, 'to_alipay_dict'):
                params['storage_time'] = self.storage_time.to_alipay_dict()
            else:
                params['storage_time'] = self.storage_time
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_tags:
            if hasattr(self.user_tags, 'to_alipay_dict'):
                params['user_tags'] = self.user_tags.to_alipay_dict()
            else:
                params['user_tags'] = self.user_tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QipanGreyBlackCrowdUser()
        if 'encrypt_alipay_id' in d:
            o.encrypt_alipay_id = d['encrypt_alipay_id']
        if 'encrypt_identity_card_id' in d:
            o.encrypt_identity_card_id = d['encrypt_identity_card_id']
        if 'encrypt_mobile_id' in d:
            o.encrypt_mobile_id = d['encrypt_mobile_id']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'storage_time' in d:
            o.storage_time = d['storage_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_tags' in d:
            o.user_tags = d['user_tags']
        return o


