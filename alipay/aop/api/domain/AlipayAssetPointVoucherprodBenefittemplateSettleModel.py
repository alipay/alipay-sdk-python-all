#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointVoucherprodBenefittemplateSettleModel(object):

    def __init__(self):
        self._asset_id = None
        self._biz_dt = None
        self._biz_no = None
        self._partner_settle_id = None
        self._partner_settle_id_type = None
        self._settle_amount = None
        self._settle_date = None
        self._user_id = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def partner_settle_id(self):
        return self._partner_settle_id

    @partner_settle_id.setter
    def partner_settle_id(self, value):
        self._partner_settle_id = value
    @property
    def partner_settle_id_type(self):
        return self._partner_settle_id_type

    @partner_settle_id_type.setter
    def partner_settle_id_type(self, value):
        self._partner_settle_id_type = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_date(self):
        return self._settle_date

    @settle_date.setter
    def settle_date(self, value):
        self._settle_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.partner_settle_id:
            if hasattr(self.partner_settle_id, 'to_alipay_dict'):
                params['partner_settle_id'] = self.partner_settle_id.to_alipay_dict()
            else:
                params['partner_settle_id'] = self.partner_settle_id
        if self.partner_settle_id_type:
            if hasattr(self.partner_settle_id_type, 'to_alipay_dict'):
                params['partner_settle_id_type'] = self.partner_settle_id_type.to_alipay_dict()
            else:
                params['partner_settle_id_type'] = self.partner_settle_id_type
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_date:
            if hasattr(self.settle_date, 'to_alipay_dict'):
                params['settle_date'] = self.settle_date.to_alipay_dict()
            else:
                params['settle_date'] = self.settle_date
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
        o = AlipayAssetPointVoucherprodBenefittemplateSettleModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'partner_settle_id' in d:
            o.partner_settle_id = d['partner_settle_id']
        if 'partner_settle_id_type' in d:
            o.partner_settle_id_type = d['partner_settle_id_type']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_date' in d:
            o.settle_date = d['settle_date']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


