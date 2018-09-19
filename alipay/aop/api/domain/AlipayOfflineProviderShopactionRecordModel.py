#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuterShopDO import OuterShopDO


class AlipayOfflineProviderShopactionRecordModel(object):

    def __init__(self):
        self._action_detail = None
        self._action_outer_id = None
        self._action_type = None
        self._date_time = None
        self._entity = None
        self._industry = None
        self._outer_shop_do = None
        self._source = None
        self._user_id = None

    @property
    def action_detail(self):
        return self._action_detail

    @action_detail.setter
    def action_detail(self, value):
        self._action_detail = value
    @property
    def action_outer_id(self):
        return self._action_outer_id

    @action_outer_id.setter
    def action_outer_id(self, value):
        self._action_outer_id = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        self._date_time = value
    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        self._entity = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def outer_shop_do(self):
        return self._outer_shop_do

    @outer_shop_do.setter
    def outer_shop_do(self, value):
        if isinstance(value, OuterShopDO):
            self._outer_shop_do = value
        else:
            self._outer_shop_do = OuterShopDO.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_detail:
            if hasattr(self.action_detail, 'to_alipay_dict'):
                params['action_detail'] = self.action_detail.to_alipay_dict()
            else:
                params['action_detail'] = self.action_detail
        if self.action_outer_id:
            if hasattr(self.action_outer_id, 'to_alipay_dict'):
                params['action_outer_id'] = self.action_outer_id.to_alipay_dict()
            else:
                params['action_outer_id'] = self.action_outer_id
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.date_time:
            if hasattr(self.date_time, 'to_alipay_dict'):
                params['date_time'] = self.date_time.to_alipay_dict()
            else:
                params['date_time'] = self.date_time
        if self.entity:
            if hasattr(self.entity, 'to_alipay_dict'):
                params['entity'] = self.entity.to_alipay_dict()
            else:
                params['entity'] = self.entity
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.outer_shop_do:
            if hasattr(self.outer_shop_do, 'to_alipay_dict'):
                params['outer_shop_do'] = self.outer_shop_do.to_alipay_dict()
            else:
                params['outer_shop_do'] = self.outer_shop_do
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayOfflineProviderShopactionRecordModel()
        if 'action_detail' in d:
            o.action_detail = d['action_detail']
        if 'action_outer_id' in d:
            o.action_outer_id = d['action_outer_id']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'date_time' in d:
            o.date_time = d['date_time']
        if 'entity' in d:
            o.entity = d['entity']
        if 'industry' in d:
            o.industry = d['industry']
        if 'outer_shop_do' in d:
            o.outer_shop_do = d['outer_shop_do']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


