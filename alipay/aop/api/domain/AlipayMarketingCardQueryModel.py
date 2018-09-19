#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardUserInfo import CardUserInfo


class AlipayMarketingCardQueryModel(object):

    def __init__(self):
        self._card_user_info = None
        self._ext_info = None
        self._target_card_no = None
        self._target_card_no_type = None

    @property
    def card_user_info(self):
        return self._card_user_info

    @card_user_info.setter
    def card_user_info(self, value):
        if isinstance(value, CardUserInfo):
            self._card_user_info = value
        else:
            self._card_user_info = CardUserInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_user_info:
            if hasattr(self.card_user_info, 'to_alipay_dict'):
                params['card_user_info'] = self.card_user_info.to_alipay_dict()
            else:
                params['card_user_info'] = self.card_user_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardQueryModel()
        if 'card_user_info' in d:
            o.card_user_info = d['card_user_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        return o


