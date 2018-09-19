#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppRechargeNotifySendModel(object):

    def __init__(self):
        self._face_price = None
        self._gmt_charge = None
        self._mobile = None
        self._notify_type = None
        self._out_user_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def face_price(self):
        return self._face_price

    @face_price.setter
    def face_price(self, value):
        self._face_price = value
    @property
    def gmt_charge(self):
        return self._gmt_charge

    @gmt_charge.setter
    def gmt_charge(self, value):
        self._gmt_charge = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_price:
            if hasattr(self.face_price, 'to_alipay_dict'):
                params['face_price'] = self.face_price.to_alipay_dict()
            else:
                params['face_price'] = self.face_price
        if self.gmt_charge:
            if hasattr(self.gmt_charge, 'to_alipay_dict'):
                params['gmt_charge'] = self.gmt_charge.to_alipay_dict()
            else:
                params['gmt_charge'] = self.gmt_charge
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayEbppRechargeNotifySendModel()
        if 'face_price' in d:
            o.face_price = d['face_price']
        if 'gmt_charge' in d:
            o.gmt_charge = d['gmt_charge']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


