#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetFundInfo import AssetFundInfo
from alipay.aop.api.domain.AssetValidPeriod import AssetValidPeriod


class AlipayAssetPointVoucherprodBenefittemplateCreateModel(object):

    def __init__(self):
        self._asset_type = None
        self._auto_recharge = None
        self._biz_dt = None
        self._biz_from = None
        self._biz_no = None
        self._camp_id = None
        self._fund_infos = None
        self._name = None
        self._partner_id = None
        self._product_code = None
        self._publish_end_time = None
        self._valid_period = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def auto_recharge(self):
        return self._auto_recharge

    @auto_recharge.setter
    def auto_recharge(self, value):
        self._auto_recharge = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, AssetFundInfo):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(AssetFundInfo.from_alipay_dict(i))
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        if isinstance(value, AssetValidPeriod):
            self._valid_period = value
        else:
            self._valid_period = AssetValidPeriod.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.auto_recharge:
            if hasattr(self.auto_recharge, 'to_alipay_dict'):
                params['auto_recharge'] = self.auto_recharge.to_alipay_dict()
            else:
                params['auto_recharge'] = self.auto_recharge
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.fund_infos:
            if isinstance(self.fund_infos, list):
                for i in range(0, len(self.fund_infos)):
                    element = self.fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.fund_infos, 'to_alipay_dict'):
                params['fund_infos'] = self.fund_infos.to_alipay_dict()
            else:
                params['fund_infos'] = self.fund_infos
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
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointVoucherprodBenefittemplateCreateModel()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'auto_recharge' in d:
            o.auto_recharge = d['auto_recharge']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'fund_infos' in d:
            o.fund_infos = d['fund_infos']
        if 'name' in d:
            o.name = d['name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        return o


