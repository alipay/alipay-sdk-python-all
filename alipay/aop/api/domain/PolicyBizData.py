#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyBizData(object):

    def __init__(self):
        self._channel_user_tag = None
        self._effect_end_date = None
        self._effect_start_date = None
        self._entrance = None
        self._insure_status = None
        self._partner_org_id = None
        self._premium_amount = None
        self._prod_name = None
        self._prod_version = None
        self._source = None
        self._sp_no = None

    @property
    def channel_user_tag(self):
        return self._channel_user_tag

    @channel_user_tag.setter
    def channel_user_tag(self, value):
        self._channel_user_tag = value
    @property
    def effect_end_date(self):
        return self._effect_end_date

    @effect_end_date.setter
    def effect_end_date(self, value):
        self._effect_end_date = value
    @property
    def effect_start_date(self):
        return self._effect_start_date

    @effect_start_date.setter
    def effect_start_date(self, value):
        self._effect_start_date = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def insure_status(self):
        return self._insure_status

    @insure_status.setter
    def insure_status(self, value):
        self._insure_status = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def premium_amount(self):
        return self._premium_amount

    @premium_amount.setter
    def premium_amount(self, value):
        self._premium_amount = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sp_no(self):
        return self._sp_no

    @sp_no.setter
    def sp_no(self, value):
        self._sp_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_user_tag:
            if hasattr(self.channel_user_tag, 'to_alipay_dict'):
                params['channel_user_tag'] = self.channel_user_tag.to_alipay_dict()
            else:
                params['channel_user_tag'] = self.channel_user_tag
        if self.effect_end_date:
            if hasattr(self.effect_end_date, 'to_alipay_dict'):
                params['effect_end_date'] = self.effect_end_date.to_alipay_dict()
            else:
                params['effect_end_date'] = self.effect_end_date
        if self.effect_start_date:
            if hasattr(self.effect_start_date, 'to_alipay_dict'):
                params['effect_start_date'] = self.effect_start_date.to_alipay_dict()
            else:
                params['effect_start_date'] = self.effect_start_date
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.insure_status:
            if hasattr(self.insure_status, 'to_alipay_dict'):
                params['insure_status'] = self.insure_status.to_alipay_dict()
            else:
                params['insure_status'] = self.insure_status
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.premium_amount:
            if hasattr(self.premium_amount, 'to_alipay_dict'):
                params['premium_amount'] = self.premium_amount.to_alipay_dict()
            else:
                params['premium_amount'] = self.premium_amount
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sp_no:
            if hasattr(self.sp_no, 'to_alipay_dict'):
                params['sp_no'] = self.sp_no.to_alipay_dict()
            else:
                params['sp_no'] = self.sp_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyBizData()
        if 'channel_user_tag' in d:
            o.channel_user_tag = d['channel_user_tag']
        if 'effect_end_date' in d:
            o.effect_end_date = d['effect_end_date']
        if 'effect_start_date' in d:
            o.effect_start_date = d['effect_start_date']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'insure_status' in d:
            o.insure_status = d['insure_status']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'premium_amount' in d:
            o.premium_amount = d['premium_amount']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'source' in d:
            o.source = d['source']
        if 'sp_no' in d:
            o.sp_no = d['sp_no']
        return o


