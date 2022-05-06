#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SiteStrategy import SiteStrategy
from alipay.aop.api.domain.OuterTargetingItem import OuterTargetingItem


class AlipayDataDataserviceAdOrderCreateModel(object):

    def __init__(self):
        self._biz_token = None
        self._charge_type = None
        self._end_date = None
        self._order_name = None
        self._order_outer_id = None
        self._principal_id = None
        self._profile_id = None
        self._sell_mode = None
        self._site_strategy = None
        self._start_date = None
        self._store_id = None
        self._targeting_list = None
        self._user_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def order_name(self):
        return self._order_name

    @order_name.setter
    def order_name(self, value):
        self._order_name = value
    @property
    def order_outer_id(self):
        return self._order_outer_id

    @order_outer_id.setter
    def order_outer_id(self, value):
        self._order_outer_id = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value
    @property
    def sell_mode(self):
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, value):
        self._sell_mode = value
    @property
    def site_strategy(self):
        return self._site_strategy

    @site_strategy.setter
    def site_strategy(self, value):
        if isinstance(value, SiteStrategy):
            self._site_strategy = value
        else:
            self._site_strategy = SiteStrategy.from_alipay_dict(value)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def targeting_list(self):
        return self._targeting_list

    @targeting_list.setter
    def targeting_list(self, value):
        if isinstance(value, list):
            self._targeting_list = list()
            for i in value:
                if isinstance(i, OuterTargetingItem):
                    self._targeting_list.append(i)
                else:
                    self._targeting_list.append(OuterTargetingItem.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.order_name:
            if hasattr(self.order_name, 'to_alipay_dict'):
                params['order_name'] = self.order_name.to_alipay_dict()
            else:
                params['order_name'] = self.order_name
        if self.order_outer_id:
            if hasattr(self.order_outer_id, 'to_alipay_dict'):
                params['order_outer_id'] = self.order_outer_id.to_alipay_dict()
            else:
                params['order_outer_id'] = self.order_outer_id
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        if self.sell_mode:
            if hasattr(self.sell_mode, 'to_alipay_dict'):
                params['sell_mode'] = self.sell_mode.to_alipay_dict()
            else:
                params['sell_mode'] = self.sell_mode
        if self.site_strategy:
            if hasattr(self.site_strategy, 'to_alipay_dict'):
                params['site_strategy'] = self.site_strategy.to_alipay_dict()
            else:
                params['site_strategy'] = self.site_strategy
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.targeting_list:
            if isinstance(self.targeting_list, list):
                for i in range(0, len(self.targeting_list)):
                    element = self.targeting_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.targeting_list[i] = element.to_alipay_dict()
            if hasattr(self.targeting_list, 'to_alipay_dict'):
                params['targeting_list'] = self.targeting_list.to_alipay_dict()
            else:
                params['targeting_list'] = self.targeting_list
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
        o = AlipayDataDataserviceAdOrderCreateModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'order_name' in d:
            o.order_name = d['order_name']
        if 'order_outer_id' in d:
            o.order_outer_id = d['order_outer_id']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        if 'sell_mode' in d:
            o.sell_mode = d['sell_mode']
        if 'site_strategy' in d:
            o.site_strategy = d['site_strategy']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'targeting_list' in d:
            o.targeting_list = d['targeting_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


