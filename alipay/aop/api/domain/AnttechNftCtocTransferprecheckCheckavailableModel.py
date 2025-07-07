#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocTransferprecheckCheckavailableModel(object):

    def __init__(self):
        self._asset_on_sale_time = None
        self._from_id_no = None
        self._from_id_type = None
        self._from_partner_id_no = None
        self._from_partner_phone_no = None
        self._from_partner_register_time = None
        self._nft_id = None
        self._order_no = None
        self._out_client_ip = None
        self._to_id_no = None
        self._to_id_type = None
        self._to_partner_id_no = None
        self._to_partner_phone_no = None
        self._to_partner_register_time = None
        self._trade_cent = None
        self._verify_confirm_id = None

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
    def from_partner_id_no(self):
        return self._from_partner_id_no

    @from_partner_id_no.setter
    def from_partner_id_no(self, value):
        self._from_partner_id_no = value
    @property
    def from_partner_phone_no(self):
        return self._from_partner_phone_no

    @from_partner_phone_no.setter
    def from_partner_phone_no(self, value):
        self._from_partner_phone_no = value
    @property
    def from_partner_register_time(self):
        return self._from_partner_register_time

    @from_partner_register_time.setter
    def from_partner_register_time(self, value):
        self._from_partner_register_time = value
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
    def out_client_ip(self):
        return self._out_client_ip

    @out_client_ip.setter
    def out_client_ip(self, value):
        self._out_client_ip = value
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
    def to_partner_id_no(self):
        return self._to_partner_id_no

    @to_partner_id_no.setter
    def to_partner_id_no(self, value):
        self._to_partner_id_no = value
    @property
    def to_partner_phone_no(self):
        return self._to_partner_phone_no

    @to_partner_phone_no.setter
    def to_partner_phone_no(self, value):
        self._to_partner_phone_no = value
    @property
    def to_partner_register_time(self):
        return self._to_partner_register_time

    @to_partner_register_time.setter
    def to_partner_register_time(self, value):
        self._to_partner_register_time = value
    @property
    def trade_cent(self):
        return self._trade_cent

    @trade_cent.setter
    def trade_cent(self, value):
        self._trade_cent = value
    @property
    def verify_confirm_id(self):
        return self._verify_confirm_id

    @verify_confirm_id.setter
    def verify_confirm_id(self, value):
        self._verify_confirm_id = value


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
        if self.from_partner_id_no:
            if hasattr(self.from_partner_id_no, 'to_alipay_dict'):
                params['from_partner_id_no'] = self.from_partner_id_no.to_alipay_dict()
            else:
                params['from_partner_id_no'] = self.from_partner_id_no
        if self.from_partner_phone_no:
            if hasattr(self.from_partner_phone_no, 'to_alipay_dict'):
                params['from_partner_phone_no'] = self.from_partner_phone_no.to_alipay_dict()
            else:
                params['from_partner_phone_no'] = self.from_partner_phone_no
        if self.from_partner_register_time:
            if hasattr(self.from_partner_register_time, 'to_alipay_dict'):
                params['from_partner_register_time'] = self.from_partner_register_time.to_alipay_dict()
            else:
                params['from_partner_register_time'] = self.from_partner_register_time
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
        if self.out_client_ip:
            if hasattr(self.out_client_ip, 'to_alipay_dict'):
                params['out_client_ip'] = self.out_client_ip.to_alipay_dict()
            else:
                params['out_client_ip'] = self.out_client_ip
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
        if self.to_partner_id_no:
            if hasattr(self.to_partner_id_no, 'to_alipay_dict'):
                params['to_partner_id_no'] = self.to_partner_id_no.to_alipay_dict()
            else:
                params['to_partner_id_no'] = self.to_partner_id_no
        if self.to_partner_phone_no:
            if hasattr(self.to_partner_phone_no, 'to_alipay_dict'):
                params['to_partner_phone_no'] = self.to_partner_phone_no.to_alipay_dict()
            else:
                params['to_partner_phone_no'] = self.to_partner_phone_no
        if self.to_partner_register_time:
            if hasattr(self.to_partner_register_time, 'to_alipay_dict'):
                params['to_partner_register_time'] = self.to_partner_register_time.to_alipay_dict()
            else:
                params['to_partner_register_time'] = self.to_partner_register_time
        if self.trade_cent:
            if hasattr(self.trade_cent, 'to_alipay_dict'):
                params['trade_cent'] = self.trade_cent.to_alipay_dict()
            else:
                params['trade_cent'] = self.trade_cent
        if self.verify_confirm_id:
            if hasattr(self.verify_confirm_id, 'to_alipay_dict'):
                params['verify_confirm_id'] = self.verify_confirm_id.to_alipay_dict()
            else:
                params['verify_confirm_id'] = self.verify_confirm_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocTransferprecheckCheckavailableModel()
        if 'asset_on_sale_time' in d:
            o.asset_on_sale_time = d['asset_on_sale_time']
        if 'from_id_no' in d:
            o.from_id_no = d['from_id_no']
        if 'from_id_type' in d:
            o.from_id_type = d['from_id_type']
        if 'from_partner_id_no' in d:
            o.from_partner_id_no = d['from_partner_id_no']
        if 'from_partner_phone_no' in d:
            o.from_partner_phone_no = d['from_partner_phone_no']
        if 'from_partner_register_time' in d:
            o.from_partner_register_time = d['from_partner_register_time']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_client_ip' in d:
            o.out_client_ip = d['out_client_ip']
        if 'to_id_no' in d:
            o.to_id_no = d['to_id_no']
        if 'to_id_type' in d:
            o.to_id_type = d['to_id_type']
        if 'to_partner_id_no' in d:
            o.to_partner_id_no = d['to_partner_id_no']
        if 'to_partner_phone_no' in d:
            o.to_partner_phone_no = d['to_partner_phone_no']
        if 'to_partner_register_time' in d:
            o.to_partner_register_time = d['to_partner_register_time']
        if 'trade_cent' in d:
            o.trade_cent = d['trade_cent']
        if 'verify_confirm_id' in d:
            o.verify_confirm_id = d['verify_confirm_id']
        return o


