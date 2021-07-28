#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardTypeVO import CardTypeVO
from alipay.aop.api.domain.CardDomainVO import CardDomainVO


class CardBinVO(object):

    def __init__(self):
        self._card_alias = None
        self._card_bin_value = None
        self._card_type_vo = None
        self._domain_vo = None
        self._inst_id = None
        self._inst_len = None
        self._memo = None
        self._operator = None
        self._version = None

    @property
    def card_alias(self):
        return self._card_alias

    @card_alias.setter
    def card_alias(self, value):
        self._card_alias = value
    @property
    def card_bin_value(self):
        return self._card_bin_value

    @card_bin_value.setter
    def card_bin_value(self, value):
        self._card_bin_value = value
    @property
    def card_type_vo(self):
        return self._card_type_vo

    @card_type_vo.setter
    def card_type_vo(self, value):
        if isinstance(value, CardTypeVO):
            self._card_type_vo = value
        else:
            self._card_type_vo = CardTypeVO.from_alipay_dict(value)
    @property
    def domain_vo(self):
        return self._domain_vo

    @domain_vo.setter
    def domain_vo(self, value):
        if isinstance(value, CardDomainVO):
            self._domain_vo = value
        else:
            self._domain_vo = CardDomainVO.from_alipay_dict(value)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_len(self):
        return self._inst_len

    @inst_len.setter
    def inst_len(self, value):
        self._inst_len = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_alias:
            if hasattr(self.card_alias, 'to_alipay_dict'):
                params['card_alias'] = self.card_alias.to_alipay_dict()
            else:
                params['card_alias'] = self.card_alias
        if self.card_bin_value:
            if hasattr(self.card_bin_value, 'to_alipay_dict'):
                params['card_bin_value'] = self.card_bin_value.to_alipay_dict()
            else:
                params['card_bin_value'] = self.card_bin_value
        if self.card_type_vo:
            if hasattr(self.card_type_vo, 'to_alipay_dict'):
                params['card_type_vo'] = self.card_type_vo.to_alipay_dict()
            else:
                params['card_type_vo'] = self.card_type_vo
        if self.domain_vo:
            if hasattr(self.domain_vo, 'to_alipay_dict'):
                params['domain_vo'] = self.domain_vo.to_alipay_dict()
            else:
                params['domain_vo'] = self.domain_vo
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_len:
            if hasattr(self.inst_len, 'to_alipay_dict'):
                params['inst_len'] = self.inst_len.to_alipay_dict()
            else:
                params['inst_len'] = self.inst_len
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardBinVO()
        if 'card_alias' in d:
            o.card_alias = d['card_alias']
        if 'card_bin_value' in d:
            o.card_bin_value = d['card_bin_value']
        if 'card_type_vo' in d:
            o.card_type_vo = d['card_type_vo']
        if 'domain_vo' in d:
            o.domain_vo = d['domain_vo']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_len' in d:
            o.inst_len = d['inst_len']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'version' in d:
            o.version = d['version']
        return o


