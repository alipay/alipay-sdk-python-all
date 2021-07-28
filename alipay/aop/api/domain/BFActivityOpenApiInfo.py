#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BFActivityFundInfo import BFActivityFundInfo


class BFActivityOpenApiInfo(object):

    def __init__(self):
        self._activity_fund_infos = None
        self._aggr_id = None
        self._available = None
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_expired = None
        self._id = None
        self._name = None
        self._partner_id = None
        self._pc_id = None
        self._product_id = None
        self._rate_version = None

    @property
    def activity_fund_infos(self):
        return self._activity_fund_infos

    @activity_fund_infos.setter
    def activity_fund_infos(self, value):
        if isinstance(value, list):
            self._activity_fund_infos = list()
            for i in value:
                if isinstance(i, BFActivityFundInfo):
                    self._activity_fund_infos.append(i)
                else:
                    self._activity_fund_infos.append(BFActivityFundInfo.from_alipay_dict(i))
    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pc_id(self):
        return self._pc_id

    @pc_id.setter
    def pc_id(self, value):
        self._pc_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def rate_version(self):
        return self._rate_version

    @rate_version.setter
    def rate_version(self, value):
        self._rate_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_fund_infos:
            if isinstance(self.activity_fund_infos, list):
                for i in range(0, len(self.activity_fund_infos)):
                    element = self.activity_fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.activity_fund_infos, 'to_alipay_dict'):
                params['activity_fund_infos'] = self.activity_fund_infos.to_alipay_dict()
            else:
                params['activity_fund_infos'] = self.activity_fund_infos
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.available:
            if hasattr(self.available, 'to_alipay_dict'):
                params['available'] = self.available.to_alipay_dict()
            else:
                params['available'] = self.available
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pc_id:
            if hasattr(self.pc_id, 'to_alipay_dict'):
                params['pc_id'] = self.pc_id.to_alipay_dict()
            else:
                params['pc_id'] = self.pc_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.rate_version:
            if hasattr(self.rate_version, 'to_alipay_dict'):
                params['rate_version'] = self.rate_version.to_alipay_dict()
            else:
                params['rate_version'] = self.rate_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BFActivityOpenApiInfo()
        if 'activity_fund_infos' in d:
            o.activity_fund_infos = d['activity_fund_infos']
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'available' in d:
            o.available = d['available']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pc_id' in d:
            o.pc_id = d['pc_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'rate_version' in d:
            o.rate_version = d['rate_version']
        return o


