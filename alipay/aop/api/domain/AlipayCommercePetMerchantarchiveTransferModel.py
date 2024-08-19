#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePetMerchantarchiveTransferModel(object):

    def __init__(self):
        self._archive_id = None
        self._external_pet_id = None
        self._open_id = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def archive_id(self):
        return self._archive_id

    @archive_id.setter
    def archive_id(self, value):
        self._archive_id = value
    @property
    def external_pet_id(self):
        return self._external_pet_id

    @external_pet_id.setter
    def external_pet_id(self, value):
        self._external_pet_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_id:
            if hasattr(self.archive_id, 'to_alipay_dict'):
                params['archive_id'] = self.archive_id.to_alipay_dict()
            else:
                params['archive_id'] = self.archive_id
        if self.external_pet_id:
            if hasattr(self.external_pet_id, 'to_alipay_dict'):
                params['external_pet_id'] = self.external_pet_id.to_alipay_dict()
            else:
                params['external_pet_id'] = self.external_pet_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayCommercePetMerchantarchiveTransferModel()
        if 'archive_id' in d:
            o.archive_id = d['archive_id']
        if 'external_pet_id' in d:
            o.external_pet_id = d['external_pet_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


