#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BFActivityFundInfo(object):

    def __init__(self):
        self._activity = None
        self._aggr_id = None
        self._agreement_id = None
        self._charge_code = None
        self._key = None
        self._platform_subsidy_id = None
        self._ratio = None
        self._seller_rate = None
        self._subsidy_mode = None
        self._subsidy_user = None
        self._term = None
        self._type = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        self._activity = value
    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def charge_code(self):
        return self._charge_code

    @charge_code.setter
    def charge_code(self, value):
        self._charge_code = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def platform_subsidy_id(self):
        return self._platform_subsidy_id

    @platform_subsidy_id.setter
    def platform_subsidy_id(self, value):
        self._platform_subsidy_id = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    @property
    def seller_rate(self):
        return self._seller_rate

    @seller_rate.setter
    def seller_rate(self, value):
        self._seller_rate = value
    @property
    def subsidy_mode(self):
        return self._subsidy_mode

    @subsidy_mode.setter
    def subsidy_mode(self, value):
        self._subsidy_mode = value
    @property
    def subsidy_user(self):
        return self._subsidy_user

    @subsidy_user.setter
    def subsidy_user(self, value):
        self._subsidy_user = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.charge_code:
            if hasattr(self.charge_code, 'to_alipay_dict'):
                params['charge_code'] = self.charge_code.to_alipay_dict()
            else:
                params['charge_code'] = self.charge_code
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.platform_subsidy_id:
            if hasattr(self.platform_subsidy_id, 'to_alipay_dict'):
                params['platform_subsidy_id'] = self.platform_subsidy_id.to_alipay_dict()
            else:
                params['platform_subsidy_id'] = self.platform_subsidy_id
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        if self.seller_rate:
            if hasattr(self.seller_rate, 'to_alipay_dict'):
                params['seller_rate'] = self.seller_rate.to_alipay_dict()
            else:
                params['seller_rate'] = self.seller_rate
        if self.subsidy_mode:
            if hasattr(self.subsidy_mode, 'to_alipay_dict'):
                params['subsidy_mode'] = self.subsidy_mode.to_alipay_dict()
            else:
                params['subsidy_mode'] = self.subsidy_mode
        if self.subsidy_user:
            if hasattr(self.subsidy_user, 'to_alipay_dict'):
                params['subsidy_user'] = self.subsidy_user.to_alipay_dict()
            else:
                params['subsidy_user'] = self.subsidy_user
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BFActivityFundInfo()
        if 'activity' in d:
            o.activity = d['activity']
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'charge_code' in d:
            o.charge_code = d['charge_code']
        if 'key' in d:
            o.key = d['key']
        if 'platform_subsidy_id' in d:
            o.platform_subsidy_id = d['platform_subsidy_id']
        if 'ratio' in d:
            o.ratio = d['ratio']
        if 'seller_rate' in d:
            o.seller_rate = d['seller_rate']
        if 'subsidy_mode' in d:
            o.subsidy_mode = d['subsidy_mode']
        if 'subsidy_user' in d:
            o.subsidy_user = d['subsidy_user']
        if 'term' in d:
            o.term = d['term']
        if 'type' in d:
            o.type = d['type']
        return o


