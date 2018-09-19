#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpAssetDetail import VcpAssetDetail


class AlipayAssetVoucherprodChargeSendModel(object):

    def __init__(self):
        self._amount = None
        self._asset_amount = None
        self._asset_details = None
        self._asset_id = None
        self._asset_id_type = None
        self._asset_type = None
        self._biz_dt = None
        self._extend_info = None
        self._fund_scence = None
        self._out_biz_no = None
        self._publisher_user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def asset_amount(self):
        return self._asset_amount

    @asset_amount.setter
    def asset_amount(self, value):
        self._asset_amount = value
    @property
    def asset_details(self):
        return self._asset_details

    @asset_details.setter
    def asset_details(self, value):
        if isinstance(value, list):
            self._asset_details = list()
            for i in value:
                if isinstance(i, VcpAssetDetail):
                    self._asset_details.append(i)
                else:
                    self._asset_details.append(VcpAssetDetail.from_alipay_dict(i))
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
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.asset_amount:
            if hasattr(self.asset_amount, 'to_alipay_dict'):
                params['asset_amount'] = self.asset_amount.to_alipay_dict()
            else:
                params['asset_amount'] = self.asset_amount
        if self.asset_details:
            if isinstance(self.asset_details, list):
                for i in range(0, len(self.asset_details)):
                    element = self.asset_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_details[i] = element.to_alipay_dict()
            if hasattr(self.asset_details, 'to_alipay_dict'):
                params['asset_details'] = self.asset_details.to_alipay_dict()
            else:
                params['asset_details'] = self.asset_details
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
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetVoucherprodChargeSendModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_amount' in d:
            o.asset_amount = d['asset_amount']
        if 'asset_details' in d:
            o.asset_details = d['asset_details']
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_id_type' in d:
            o.asset_id_type = d['asset_id_type']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_scence' in d:
            o.fund_scence = d['fund_scence']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        return o


