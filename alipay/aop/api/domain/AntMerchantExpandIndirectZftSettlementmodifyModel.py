#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleCardInfo import SettleCardInfo
from alipay.aop.api.domain.DefaultSettleRule import DefaultSettleRule


class AntMerchantExpandIndirectZftSettlementmodifyModel(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._biz_cards = None
        self._default_settle_rule = None
        self._license_auth_letter_image = None
        self._smid = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def biz_cards(self):
        return self._biz_cards

    @biz_cards.setter
    def biz_cards(self, value):
        if isinstance(value, SettleCardInfo):
            self._biz_cards = value
        else:
            self._biz_cards = SettleCardInfo.from_alipay_dict(value)
    @property
    def default_settle_rule(self):
        return self._default_settle_rule

    @default_settle_rule.setter
    def default_settle_rule(self, value):
        if isinstance(value, DefaultSettleRule):
            self._default_settle_rule = value
        else:
            self._default_settle_rule = DefaultSettleRule.from_alipay_dict(value)
    @property
    def license_auth_letter_image(self):
        return self._license_auth_letter_image

    @license_auth_letter_image.setter
    def license_auth_letter_image(self, value):
        self._license_auth_letter_image = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.biz_cards:
            if hasattr(self.biz_cards, 'to_alipay_dict'):
                params['biz_cards'] = self.biz_cards.to_alipay_dict()
            else:
                params['biz_cards'] = self.biz_cards
        if self.default_settle_rule:
            if hasattr(self.default_settle_rule, 'to_alipay_dict'):
                params['default_settle_rule'] = self.default_settle_rule.to_alipay_dict()
            else:
                params['default_settle_rule'] = self.default_settle_rule
        if self.license_auth_letter_image:
            if hasattr(self.license_auth_letter_image, 'to_alipay_dict'):
                params['license_auth_letter_image'] = self.license_auth_letter_image.to_alipay_dict()
            else:
                params['license_auth_letter_image'] = self.license_auth_letter_image
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftSettlementmodifyModel()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'biz_cards' in d:
            o.biz_cards = d['biz_cards']
        if 'default_settle_rule' in d:
            o.default_settle_rule = d['default_settle_rule']
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'smid' in d:
            o.smid = d['smid']
        return o


