#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetBillInfo(object):

    def __init__(self):
        self._amount = None
        self._asset_amount = None
        self._asset_id = None
        self._asset_type = None
        self._bill_no = None
        self._biz_dt = None
        self._biz_from = None
        self._biz_no = None
        self._biz_type = None
        self._camp_id = None
        self._out_bill_no = None
        self._partner_settle_id = None
        self._partner_settle_id_type = None
        self._status = None
        self._trans_dt = None
        self._user_id = None

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
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
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
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
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
        o = AssetBillInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_amount' in d:
            o.asset_amount = d['asset_amount']
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'partner_settle_id' in d:
            o.partner_settle_id = d['partner_settle_id']
        if 'partner_settle_id_type' in d:
            o.partner_settle_id_type = d['partner_settle_id_type']
        if 'status' in d:
            o.status = d['status']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


