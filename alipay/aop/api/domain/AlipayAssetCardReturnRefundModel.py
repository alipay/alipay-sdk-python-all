#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RechargeDetail import RechargeDetail


class AlipayAssetCardReturnRefundModel(object):

    def __init__(self):
        self._asset_id = None
        self._asset_id_type = None
        self._biz_dt = None
        self._biz_from = None
        self._extend_info = None
        self._fund_scence = None
        self._is_cancel = None
        self._operator = None
        self._out_biz_no = None
        self._recharge_details = None
        self._return_amount = None
        self._return_asset_amount = None
        self._return_fee_amount = None
        self._return_fee_asset_amount = None
        self._user_id = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_id_type(self):
        return self._asset_id_type

    @asset_id_type.setter
    def asset_id_type(self, value):
        self._asset_id_type = value
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
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fund_scence(self):
        return self._fund_scence

    @fund_scence.setter
    def fund_scence(self, value):
        self._fund_scence = value
    @property
    def is_cancel(self):
        return self._is_cancel

    @is_cancel.setter
    def is_cancel(self, value):
        self._is_cancel = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def recharge_details(self):
        return self._recharge_details

    @recharge_details.setter
    def recharge_details(self, value):
        if isinstance(value, list):
            self._recharge_details = list()
            for i in value:
                if isinstance(i, RechargeDetail):
                    self._recharge_details.append(i)
                else:
                    self._recharge_details.append(RechargeDetail.from_alipay_dict(i))
    @property
    def return_amount(self):
        return self._return_amount

    @return_amount.setter
    def return_amount(self, value):
        self._return_amount = value
    @property
    def return_asset_amount(self):
        return self._return_asset_amount

    @return_asset_amount.setter
    def return_asset_amount(self, value):
        self._return_asset_amount = value
    @property
    def return_fee_amount(self):
        return self._return_fee_amount

    @return_fee_amount.setter
    def return_fee_amount(self, value):
        self._return_fee_amount = value
    @property
    def return_fee_asset_amount(self):
        return self._return_fee_asset_amount

    @return_fee_asset_amount.setter
    def return_fee_asset_amount(self, value):
        self._return_fee_asset_amount = value
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
        if self.asset_id_type:
            if hasattr(self.asset_id_type, 'to_alipay_dict'):
                params['asset_id_type'] = self.asset_id_type.to_alipay_dict()
            else:
                params['asset_id_type'] = self.asset_id_type
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
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fund_scence:
            if hasattr(self.fund_scence, 'to_alipay_dict'):
                params['fund_scence'] = self.fund_scence.to_alipay_dict()
            else:
                params['fund_scence'] = self.fund_scence
        if self.is_cancel:
            if hasattr(self.is_cancel, 'to_alipay_dict'):
                params['is_cancel'] = self.is_cancel.to_alipay_dict()
            else:
                params['is_cancel'] = self.is_cancel
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.recharge_details:
            if isinstance(self.recharge_details, list):
                for i in range(0, len(self.recharge_details)):
                    element = self.recharge_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recharge_details[i] = element.to_alipay_dict()
            if hasattr(self.recharge_details, 'to_alipay_dict'):
                params['recharge_details'] = self.recharge_details.to_alipay_dict()
            else:
                params['recharge_details'] = self.recharge_details
        if self.return_amount:
            if hasattr(self.return_amount, 'to_alipay_dict'):
                params['return_amount'] = self.return_amount.to_alipay_dict()
            else:
                params['return_amount'] = self.return_amount
        if self.return_asset_amount:
            if hasattr(self.return_asset_amount, 'to_alipay_dict'):
                params['return_asset_amount'] = self.return_asset_amount.to_alipay_dict()
            else:
                params['return_asset_amount'] = self.return_asset_amount
        if self.return_fee_amount:
            if hasattr(self.return_fee_amount, 'to_alipay_dict'):
                params['return_fee_amount'] = self.return_fee_amount.to_alipay_dict()
            else:
                params['return_fee_amount'] = self.return_fee_amount
        if self.return_fee_asset_amount:
            if hasattr(self.return_fee_asset_amount, 'to_alipay_dict'):
                params['return_fee_asset_amount'] = self.return_fee_asset_amount.to_alipay_dict()
            else:
                params['return_fee_asset_amount'] = self.return_fee_asset_amount
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
        o = AlipayAssetCardReturnRefundModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_id_type' in d:
            o.asset_id_type = d['asset_id_type']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_scence' in d:
            o.fund_scence = d['fund_scence']
        if 'is_cancel' in d:
            o.is_cancel = d['is_cancel']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'recharge_details' in d:
            o.recharge_details = d['recharge_details']
        if 'return_amount' in d:
            o.return_amount = d['return_amount']
        if 'return_asset_amount' in d:
            o.return_asset_amount = d['return_asset_amount']
        if 'return_fee_amount' in d:
            o.return_fee_amount = d['return_fee_amount']
        if 'return_fee_asset_amount' in d:
            o.return_fee_asset_amount = d['return_fee_asset_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


