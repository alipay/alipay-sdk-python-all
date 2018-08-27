#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UseRuleInfo import UseRuleInfo
from alipay.aop.api.domain.ValidDateInfo import ValidDateInfo
from alipay.aop.api.domain.VoucherTermInfo import VoucherTermInfo


class VoucherInfo(object):

    def __init__(self):
        self._can_give_friend = None
        self._use_rule = None
        self._valid_date = None
        self._voucher_desc = None
        self._voucher_img = None
        self._voucher_logo = None
        self._voucher_name = None
        self._voucher_terms = None
        self._voucher_type = None

    @property
    def can_give_friend(self):
        return self._can_give_friend

    @can_give_friend.setter
    def can_give_friend(self, value):
        self._can_give_friend = value
    @property
    def use_rule(self):
        return self._use_rule

    @use_rule.setter
    def use_rule(self, value):
        if isinstance(value, UseRuleInfo):
            self._use_rule = value
        else:
            self._use_rule = UseRuleInfo.from_alipay_dict(value)
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        if isinstance(value, ValidDateInfo):
            self._valid_date = value
        else:
            self._valid_date = ValidDateInfo.from_alipay_dict(value)
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_img(self):
        return self._voucher_img

    @voucher_img.setter
    def voucher_img(self, value):
        self._voucher_img = value
    @property
    def voucher_logo(self):
        return self._voucher_logo

    @voucher_logo.setter
    def voucher_logo(self, value):
        self._voucher_logo = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_terms(self):
        return self._voucher_terms

    @voucher_terms.setter
    def voucher_terms(self, value):
        if isinstance(value, list):
            self._voucher_terms = list()
            for i in value:
                if isinstance(i, VoucherTermInfo):
                    self._voucher_terms.append(i)
                else:
                    self._voucher_terms.append(VoucherTermInfo.from_alipay_dict(i))
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_give_friend:
            if hasattr(self.can_give_friend, 'to_alipay_dict'):
                params['can_give_friend'] = self.can_give_friend.to_alipay_dict()
            else:
                params['can_give_friend'] = self.can_give_friend
        if self.use_rule:
            if hasattr(self.use_rule, 'to_alipay_dict'):
                params['use_rule'] = self.use_rule.to_alipay_dict()
            else:
                params['use_rule'] = self.use_rule
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_img:
            if hasattr(self.voucher_img, 'to_alipay_dict'):
                params['voucher_img'] = self.voucher_img.to_alipay_dict()
            else:
                params['voucher_img'] = self.voucher_img
        if self.voucher_logo:
            if hasattr(self.voucher_logo, 'to_alipay_dict'):
                params['voucher_logo'] = self.voucher_logo.to_alipay_dict()
            else:
                params['voucher_logo'] = self.voucher_logo
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_terms:
            if isinstance(self.voucher_terms, list):
                for i in range(0, len(self.voucher_terms)):
                    element = self.voucher_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_terms[i] = element.to_alipay_dict()
            if hasattr(self.voucher_terms, 'to_alipay_dict'):
                params['voucher_terms'] = self.voucher_terms.to_alipay_dict()
            else:
                params['voucher_terms'] = self.voucher_terms
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherInfo()
        if 'can_give_friend' in d:
            o.can_give_friend = d['can_give_friend']
        if 'use_rule' in d:
            o.use_rule = d['use_rule']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_img' in d:
            o.voucher_img = d['voucher_img']
        if 'voucher_logo' in d:
            o.voucher_logo = d['voucher_logo']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_terms' in d:
            o.voucher_terms = d['voucher_terms']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


