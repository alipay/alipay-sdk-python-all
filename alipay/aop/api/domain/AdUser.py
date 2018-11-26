#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdUser(object):

    def __init__(self):
        self._company_license = None
        self._company_name = None
        self._company_trade = None
        self._first_trade_id = None
        self._icp_license = None
        self._icp_license_url = None
        self._register_place = None
        self._second_trade_id = None
        self._telephone = None
        self._third_user_id = None
        self._user_mail = None
        self._user_name = None

    @property
    def company_license(self):
        return self._company_license

    @company_license.setter
    def company_license(self, value):
        self._company_license = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_trade(self):
        return self._company_trade

    @company_trade.setter
    def company_trade(self, value):
        self._company_trade = value
    @property
    def first_trade_id(self):
        return self._first_trade_id

    @first_trade_id.setter
    def first_trade_id(self, value):
        self._first_trade_id = value
    @property
    def icp_license(self):
        return self._icp_license

    @icp_license.setter
    def icp_license(self, value):
        self._icp_license = value
    @property
    def icp_license_url(self):
        return self._icp_license_url

    @icp_license_url.setter
    def icp_license_url(self, value):
        self._icp_license_url = value
    @property
    def register_place(self):
        return self._register_place

    @register_place.setter
    def register_place(self, value):
        self._register_place = value
    @property
    def second_trade_id(self):
        return self._second_trade_id

    @second_trade_id.setter
    def second_trade_id(self, value):
        self._second_trade_id = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def third_user_id(self):
        return self._third_user_id

    @third_user_id.setter
    def third_user_id(self, value):
        self._third_user_id = value
    @property
    def user_mail(self):
        return self._user_mail

    @user_mail.setter
    def user_mail(self, value):
        self._user_mail = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_license:
            if hasattr(self.company_license, 'to_alipay_dict'):
                params['company_license'] = self.company_license.to_alipay_dict()
            else:
                params['company_license'] = self.company_license
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_trade:
            if hasattr(self.company_trade, 'to_alipay_dict'):
                params['company_trade'] = self.company_trade.to_alipay_dict()
            else:
                params['company_trade'] = self.company_trade
        if self.first_trade_id:
            if hasattr(self.first_trade_id, 'to_alipay_dict'):
                params['first_trade_id'] = self.first_trade_id.to_alipay_dict()
            else:
                params['first_trade_id'] = self.first_trade_id
        if self.icp_license:
            if hasattr(self.icp_license, 'to_alipay_dict'):
                params['icp_license'] = self.icp_license.to_alipay_dict()
            else:
                params['icp_license'] = self.icp_license
        if self.icp_license_url:
            if hasattr(self.icp_license_url, 'to_alipay_dict'):
                params['icp_license_url'] = self.icp_license_url.to_alipay_dict()
            else:
                params['icp_license_url'] = self.icp_license_url
        if self.register_place:
            if hasattr(self.register_place, 'to_alipay_dict'):
                params['register_place'] = self.register_place.to_alipay_dict()
            else:
                params['register_place'] = self.register_place
        if self.second_trade_id:
            if hasattr(self.second_trade_id, 'to_alipay_dict'):
                params['second_trade_id'] = self.second_trade_id.to_alipay_dict()
            else:
                params['second_trade_id'] = self.second_trade_id
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.third_user_id:
            if hasattr(self.third_user_id, 'to_alipay_dict'):
                params['third_user_id'] = self.third_user_id.to_alipay_dict()
            else:
                params['third_user_id'] = self.third_user_id
        if self.user_mail:
            if hasattr(self.user_mail, 'to_alipay_dict'):
                params['user_mail'] = self.user_mail.to_alipay_dict()
            else:
                params['user_mail'] = self.user_mail
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdUser()
        if 'company_license' in d:
            o.company_license = d['company_license']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_trade' in d:
            o.company_trade = d['company_trade']
        if 'first_trade_id' in d:
            o.first_trade_id = d['first_trade_id']
        if 'icp_license' in d:
            o.icp_license = d['icp_license']
        if 'icp_license_url' in d:
            o.icp_license_url = d['icp_license_url']
        if 'register_place' in d:
            o.register_place = d['register_place']
        if 'second_trade_id' in d:
            o.second_trade_id = d['second_trade_id']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'third_user_id' in d:
            o.third_user_id = d['third_user_id']
        if 'user_mail' in d:
            o.user_mail = d['user_mail']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


