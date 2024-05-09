#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupEntryCreateModel(object):

    def __init__(self):
        self._external_id = None
        self._have_business = None
        self._jump_link = None

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def have_business(self):
        return self._have_business

    @have_business.setter
    def have_business(self, value):
        self._have_business = value
    @property
    def jump_link(self):
        return self._jump_link

    @jump_link.setter
    def jump_link(self, value):
        self._jump_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.have_business:
            if hasattr(self.have_business, 'to_alipay_dict'):
                params['have_business'] = self.have_business.to_alipay_dict()
            else:
                params['have_business'] = self.have_business
        if self.jump_link:
            if hasattr(self.jump_link, 'to_alipay_dict'):
                params['jump_link'] = self.jump_link.to_alipay_dict()
            else:
                params['jump_link'] = self.jump_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupEntryCreateModel()
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'have_business' in d:
            o.have_business = d['have_business']
        if 'jump_link' in d:
            o.jump_link = d['jump_link']
        return o


