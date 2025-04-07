#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocTransferApplyModel(object):

    def __init__(self):
        self._asset_on_sale_time = None
        self._from_id_no = None
        self._from_id_type = None
        self._from_user_register_time = None
        self._nft_id = None
        self._order_no = None
        self._pay_channel = None
        self._to_id_no = None
        self._to_id_type = None
        self._to_user_register_time = None
        self._trade_cent = None
        self._trade_order_no = None
        self._transfer_operate = None
        self._transfer_type = None

    @property
    def asset_on_sale_time(self):
        return self._asset_on_sale_time

    @asset_on_sale_time.setter
    def asset_on_sale_time(self, value):
        self._asset_on_sale_time = value
    @property
    def from_id_no(self):
        return self._from_id_no

    @from_id_no.setter
    def from_id_no(self, value):
        self._from_id_no = value
    @property
    def from_id_type(self):
        return self._from_id_type

    @from_id_type.setter
    def from_id_type(self, value):
        self._from_id_type = value
    @property
    def from_user_register_time(self):
        return self._from_user_register_time

    @from_user_register_time.setter
    def from_user_register_time(self, value):
        self._from_user_register_time = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def to_id_no(self):
        return self._to_id_no

    @to_id_no.setter
    def to_id_no(self, value):
        self._to_id_no = value
    @property
    def to_id_type(self):
        return self._to_id_type

    @to_id_type.setter
    def to_id_type(self, value):
        self._to_id_type = value
    @property
    def to_user_register_time(self):
        return self._to_user_register_time

    @to_user_register_time.setter
    def to_user_register_time(self, value):
        self._to_user_register_time = value
    @property
    def trade_cent(self):
        return self._trade_cent

    @trade_cent.setter
    def trade_cent(self, value):
        self._trade_cent = value
    @property
    def trade_order_no(self):
        return self._trade_order_no

    @trade_order_no.setter
    def trade_order_no(self, value):
        self._trade_order_no = value
    @property
    def transfer_operate(self):
        return self._transfer_operate

    @transfer_operate.setter
    def transfer_operate(self, value):
        self._transfer_operate = value
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_on_sale_time:
            if hasattr(self.asset_on_sale_time, 'to_alipay_dict'):
                params['asset_on_sale_time'] = self.asset_on_sale_time.to_alipay_dict()
            else:
                params['asset_on_sale_time'] = self.asset_on_sale_time
        if self.from_id_no:
            if hasattr(self.from_id_no, 'to_alipay_dict'):
                params['from_id_no'] = self.from_id_no.to_alipay_dict()
            else:
                params['from_id_no'] = self.from_id_no
        if self.from_id_type:
            if hasattr(self.from_id_type, 'to_alipay_dict'):
                params['from_id_type'] = self.from_id_type.to_alipay_dict()
            else:
                params['from_id_type'] = self.from_id_type
        if self.from_user_register_time:
            if hasattr(self.from_user_register_time, 'to_alipay_dict'):
                params['from_user_register_time'] = self.from_user_register_time.to_alipay_dict()
            else:
                params['from_user_register_time'] = self.from_user_register_time
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.to_id_no:
            if hasattr(self.to_id_no, 'to_alipay_dict'):
                params['to_id_no'] = self.to_id_no.to_alipay_dict()
            else:
                params['to_id_no'] = self.to_id_no
        if self.to_id_type:
            if hasattr(self.to_id_type, 'to_alipay_dict'):
                params['to_id_type'] = self.to_id_type.to_alipay_dict()
            else:
                params['to_id_type'] = self.to_id_type
        if self.to_user_register_time:
            if hasattr(self.to_user_register_time, 'to_alipay_dict'):
                params['to_user_register_time'] = self.to_user_register_time.to_alipay_dict()
            else:
                params['to_user_register_time'] = self.to_user_register_time
        if self.trade_cent:
            if hasattr(self.trade_cent, 'to_alipay_dict'):
                params['trade_cent'] = self.trade_cent.to_alipay_dict()
            else:
                params['trade_cent'] = self.trade_cent
        if self.trade_order_no:
            if hasattr(self.trade_order_no, 'to_alipay_dict'):
                params['trade_order_no'] = self.trade_order_no.to_alipay_dict()
            else:
                params['trade_order_no'] = self.trade_order_no
        if self.transfer_operate:
            if hasattr(self.transfer_operate, 'to_alipay_dict'):
                params['transfer_operate'] = self.transfer_operate.to_alipay_dict()
            else:
                params['transfer_operate'] = self.transfer_operate
        if self.transfer_type:
            if hasattr(self.transfer_type, 'to_alipay_dict'):
                params['transfer_type'] = self.transfer_type.to_alipay_dict()
            else:
                params['transfer_type'] = self.transfer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocTransferApplyModel()
        if 'asset_on_sale_time' in d:
            o.asset_on_sale_time = d['asset_on_sale_time']
        if 'from_id_no' in d:
            o.from_id_no = d['from_id_no']
        if 'from_id_type' in d:
            o.from_id_type = d['from_id_type']
        if 'from_user_register_time' in d:
            o.from_user_register_time = d['from_user_register_time']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'to_id_no' in d:
            o.to_id_no = d['to_id_no']
        if 'to_id_type' in d:
            o.to_id_type = d['to_id_type']
        if 'to_user_register_time' in d:
            o.to_user_register_time = d['to_user_register_time']
        if 'trade_cent' in d:
            o.trade_cent = d['trade_cent']
        if 'trade_order_no' in d:
            o.trade_order_no = d['trade_order_no']
        if 'transfer_operate' in d:
            o.transfer_operate = d['transfer_operate']
        if 'transfer_type' in d:
            o.transfer_type = d['transfer_type']
        return o


