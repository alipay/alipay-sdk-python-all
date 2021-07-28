#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportWorldVirtualcardBatchqueryModel(object):

    def __init__(self):
        self._card_no = None
        self._card_type = None
        self._include_deleted = None
        self._user_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def include_deleted(self):
        return self._include_deleted

    @include_deleted.setter
    def include_deleted(self, value):
        self._include_deleted = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.include_deleted:
            if hasattr(self.include_deleted, 'to_alipay_dict'):
                params['include_deleted'] = self.include_deleted.to_alipay_dict()
            else:
                params['include_deleted'] = self.include_deleted
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportWorldVirtualcardBatchqueryModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'include_deleted' in d:
            o.include_deleted = d['include_deleted']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


