#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommunityRelationshipExtendField import CommunityRelationshipExtendField


class AlipayEbppCommunityRelationshipCreateModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._allow_skip_pay = None
        self._billkey_url = None
        self._community_short_name = None
        self._daily_end = None
        self._daily_start = None
        self._extend_field = None
        self._out_bill_url = None
        self._property_short_name = None
        self._service_end = None
        self._service_start = None
        self._service_type = None
        self._smid = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def allow_skip_pay(self):
        return self._allow_skip_pay

    @allow_skip_pay.setter
    def allow_skip_pay(self, value):
        self._allow_skip_pay = value
    @property
    def billkey_url(self):
        return self._billkey_url

    @billkey_url.setter
    def billkey_url(self, value):
        self._billkey_url = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def daily_end(self):
        return self._daily_end

    @daily_end.setter
    def daily_end(self, value):
        self._daily_end = value
    @property
    def daily_start(self):
        return self._daily_start

    @daily_start.setter
    def daily_start(self, value):
        self._daily_start = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        if isinstance(value, CommunityRelationshipExtendField):
            self._extend_field = value
        else:
            self._extend_field = CommunityRelationshipExtendField.from_alipay_dict(value)
    @property
    def out_bill_url(self):
        return self._out_bill_url

    @out_bill_url.setter
    def out_bill_url(self, value):
        self._out_bill_url = value
    @property
    def property_short_name(self):
        return self._property_short_name

    @property_short_name.setter
    def property_short_name(self, value):
        self._property_short_name = value
    @property
    def service_end(self):
        return self._service_end

    @service_end.setter
    def service_end(self, value):
        self._service_end = value
    @property
    def service_start(self):
        return self._service_start

    @service_start.setter
    def service_start(self, value):
        self._service_start = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.allow_skip_pay:
            if hasattr(self.allow_skip_pay, 'to_alipay_dict'):
                params['allow_skip_pay'] = self.allow_skip_pay.to_alipay_dict()
            else:
                params['allow_skip_pay'] = self.allow_skip_pay
        if self.billkey_url:
            if hasattr(self.billkey_url, 'to_alipay_dict'):
                params['billkey_url'] = self.billkey_url.to_alipay_dict()
            else:
                params['billkey_url'] = self.billkey_url
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.daily_end:
            if hasattr(self.daily_end, 'to_alipay_dict'):
                params['daily_end'] = self.daily_end.to_alipay_dict()
            else:
                params['daily_end'] = self.daily_end
        if self.daily_start:
            if hasattr(self.daily_start, 'to_alipay_dict'):
                params['daily_start'] = self.daily_start.to_alipay_dict()
            else:
                params['daily_start'] = self.daily_start
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.out_bill_url:
            if hasattr(self.out_bill_url, 'to_alipay_dict'):
                params['out_bill_url'] = self.out_bill_url.to_alipay_dict()
            else:
                params['out_bill_url'] = self.out_bill_url
        if self.property_short_name:
            if hasattr(self.property_short_name, 'to_alipay_dict'):
                params['property_short_name'] = self.property_short_name.to_alipay_dict()
            else:
                params['property_short_name'] = self.property_short_name
        if self.service_end:
            if hasattr(self.service_end, 'to_alipay_dict'):
                params['service_end'] = self.service_end.to_alipay_dict()
            else:
                params['service_end'] = self.service_end
        if self.service_start:
            if hasattr(self.service_start, 'to_alipay_dict'):
                params['service_start'] = self.service_start.to_alipay_dict()
            else:
                params['service_start'] = self.service_start
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
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
        o = AlipayEbppCommunityRelationshipCreateModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'allow_skip_pay' in d:
            o.allow_skip_pay = d['allow_skip_pay']
        if 'billkey_url' in d:
            o.billkey_url = d['billkey_url']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'daily_end' in d:
            o.daily_end = d['daily_end']
        if 'daily_start' in d:
            o.daily_start = d['daily_start']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'out_bill_url' in d:
            o.out_bill_url = d['out_bill_url']
        if 'property_short_name' in d:
            o.property_short_name = d['property_short_name']
        if 'service_end' in d:
            o.service_end = d['service_end']
        if 'service_start' in d:
            o.service_start = d['service_start']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'smid' in d:
            o.smid = d['smid']
        return o


