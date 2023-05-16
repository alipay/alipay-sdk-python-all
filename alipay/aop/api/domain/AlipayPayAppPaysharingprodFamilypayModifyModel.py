#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FamilyPayQuotaInfo import FamilyPayQuotaInfo
from alipay.aop.api.domain.FamilyPayBizUserInfo import FamilyPayBizUserInfo


class AlipayPayAppPaysharingprodFamilypayModifyModel(object):

    def __init__(self):
        self._card_id = None
        self._modify_type = None
        self._quota_info = None
        self._self_role = None
        self._source = None
        self._user_info = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def quota_info(self):
        return self._quota_info

    @quota_info.setter
    def quota_info(self, value):
        if isinstance(value, FamilyPayQuotaInfo):
            self._quota_info = value
        else:
            self._quota_info = FamilyPayQuotaInfo.from_alipay_dict(value)
    @property
    def self_role(self):
        return self._self_role

    @self_role.setter
    def self_role(self, value):
        self._self_role = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, FamilyPayBizUserInfo):
            self._user_info = value
        else:
            self._user_info = FamilyPayBizUserInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.quota_info:
            if hasattr(self.quota_info, 'to_alipay_dict'):
                params['quota_info'] = self.quota_info.to_alipay_dict()
            else:
                params['quota_info'] = self.quota_info
        if self.self_role:
            if hasattr(self.self_role, 'to_alipay_dict'):
                params['self_role'] = self.self_role.to_alipay_dict()
            else:
                params['self_role'] = self.self_role
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppPaysharingprodFamilypayModifyModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'quota_info' in d:
            o.quota_info = d['quota_info']
        if 'self_role' in d:
            o.self_role = d['self_role']
        if 'source' in d:
            o.source = d['source']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


