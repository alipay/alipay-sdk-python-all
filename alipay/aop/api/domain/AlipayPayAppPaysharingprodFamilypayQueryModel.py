#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FamilyPayBizUserInfo import FamilyPayBizUserInfo


class AlipayPayAppPaysharingprodFamilypayQueryModel(object):

    def __init__(self):
        self._apply_no = None
        self._card_id = None
        self._source = None
        self._user_info = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
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
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
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
        o = AlipayPayAppPaysharingprodFamilypayQueryModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


