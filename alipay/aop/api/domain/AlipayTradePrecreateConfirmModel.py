#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradePrecreateConfirmExtendParam import TradePrecreateConfirmExtendParam


class AlipayTradePrecreateConfirmModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_id_type = None
        self._confirm_id = None
        self._confirm_type = None
        self._extend_params = None
        self._issuer_id = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_id_type(self):
        return self._buyer_id_type

    @buyer_id_type.setter
    def buyer_id_type(self, value):
        self._buyer_id_type = value
    @property
    def confirm_id(self):
        return self._confirm_id

    @confirm_id.setter
    def confirm_id(self, value):
        self._confirm_id = value
    @property
    def confirm_type(self):
        return self._confirm_type

    @confirm_type.setter
    def confirm_type(self, value):
        self._confirm_type = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, TradePrecreateConfirmExtendParam):
            self._extend_params = value
        else:
            self._extend_params = TradePrecreateConfirmExtendParam.from_alipay_dict(value)
    @property
    def issuer_id(self):
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, value):
        self._issuer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_id_type:
            if hasattr(self.buyer_id_type, 'to_alipay_dict'):
                params['buyer_id_type'] = self.buyer_id_type.to_alipay_dict()
            else:
                params['buyer_id_type'] = self.buyer_id_type
        if self.confirm_id:
            if hasattr(self.confirm_id, 'to_alipay_dict'):
                params['confirm_id'] = self.confirm_id.to_alipay_dict()
            else:
                params['confirm_id'] = self.confirm_id
        if self.confirm_type:
            if hasattr(self.confirm_type, 'to_alipay_dict'):
                params['confirm_type'] = self.confirm_type.to_alipay_dict()
            else:
                params['confirm_type'] = self.confirm_type
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.issuer_id:
            if hasattr(self.issuer_id, 'to_alipay_dict'):
                params['issuer_id'] = self.issuer_id.to_alipay_dict()
            else:
                params['issuer_id'] = self.issuer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePrecreateConfirmModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_id_type' in d:
            o.buyer_id_type = d['buyer_id_type']
        if 'confirm_id' in d:
            o.confirm_id = d['confirm_id']
        if 'confirm_type' in d:
            o.confirm_type = d['confirm_type']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'issuer_id' in d:
            o.issuer_id = d['issuer_id']
        return o


