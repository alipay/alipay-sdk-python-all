#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionAccountModifyModel(object):

    def __init__(self):
        self._account_no = None
        self._biz_scene = None
        self._merchant_alipay_open_id = None
        self._merchant_alipay_uid = None
        self._payee_account_type = None
        self._payee_contact_line = None
        self._payee_participant_id = None
        self._payee_participant_name = None
        self._payee_participant_type = None
        self._payer_participant_id = None
        self._payer_participant_name = None
        self._payer_participant_type = None
        self._special_funds_amount = None
        self._special_funds_currency = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_alipay_open_id(self):
        return self._merchant_alipay_open_id

    @merchant_alipay_open_id.setter
    def merchant_alipay_open_id(self, value):
        self._merchant_alipay_open_id = value
    @property
    def merchant_alipay_uid(self):
        return self._merchant_alipay_uid

    @merchant_alipay_uid.setter
    def merchant_alipay_uid(self, value):
        self._merchant_alipay_uid = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_contact_line(self):
        return self._payee_contact_line

    @payee_contact_line.setter
    def payee_contact_line(self, value):
        self._payee_contact_line = value
    @property
    def payee_participant_id(self):
        return self._payee_participant_id

    @payee_participant_id.setter
    def payee_participant_id(self, value):
        self._payee_participant_id = value
    @property
    def payee_participant_name(self):
        return self._payee_participant_name

    @payee_participant_name.setter
    def payee_participant_name(self, value):
        self._payee_participant_name = value
    @property
    def payee_participant_type(self):
        return self._payee_participant_type

    @payee_participant_type.setter
    def payee_participant_type(self, value):
        self._payee_participant_type = value
    @property
    def payer_participant_id(self):
        return self._payer_participant_id

    @payer_participant_id.setter
    def payer_participant_id(self, value):
        self._payer_participant_id = value
    @property
    def payer_participant_name(self):
        return self._payer_participant_name

    @payer_participant_name.setter
    def payer_participant_name(self, value):
        self._payer_participant_name = value
    @property
    def payer_participant_type(self):
        return self._payer_participant_type

    @payer_participant_type.setter
    def payer_participant_type(self, value):
        self._payer_participant_type = value
    @property
    def special_funds_amount(self):
        return self._special_funds_amount

    @special_funds_amount.setter
    def special_funds_amount(self, value):
        self._special_funds_amount = value
    @property
    def special_funds_currency(self):
        return self._special_funds_currency

    @special_funds_currency.setter
    def special_funds_currency(self, value):
        self._special_funds_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_alipay_open_id:
            if hasattr(self.merchant_alipay_open_id, 'to_alipay_dict'):
                params['merchant_alipay_open_id'] = self.merchant_alipay_open_id.to_alipay_dict()
            else:
                params['merchant_alipay_open_id'] = self.merchant_alipay_open_id
        if self.merchant_alipay_uid:
            if hasattr(self.merchant_alipay_uid, 'to_alipay_dict'):
                params['merchant_alipay_uid'] = self.merchant_alipay_uid.to_alipay_dict()
            else:
                params['merchant_alipay_uid'] = self.merchant_alipay_uid
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_contact_line:
            if hasattr(self.payee_contact_line, 'to_alipay_dict'):
                params['payee_contact_line'] = self.payee_contact_line.to_alipay_dict()
            else:
                params['payee_contact_line'] = self.payee_contact_line
        if self.payee_participant_id:
            if hasattr(self.payee_participant_id, 'to_alipay_dict'):
                params['payee_participant_id'] = self.payee_participant_id.to_alipay_dict()
            else:
                params['payee_participant_id'] = self.payee_participant_id
        if self.payee_participant_name:
            if hasattr(self.payee_participant_name, 'to_alipay_dict'):
                params['payee_participant_name'] = self.payee_participant_name.to_alipay_dict()
            else:
                params['payee_participant_name'] = self.payee_participant_name
        if self.payee_participant_type:
            if hasattr(self.payee_participant_type, 'to_alipay_dict'):
                params['payee_participant_type'] = self.payee_participant_type.to_alipay_dict()
            else:
                params['payee_participant_type'] = self.payee_participant_type
        if self.payer_participant_id:
            if hasattr(self.payer_participant_id, 'to_alipay_dict'):
                params['payer_participant_id'] = self.payer_participant_id.to_alipay_dict()
            else:
                params['payer_participant_id'] = self.payer_participant_id
        if self.payer_participant_name:
            if hasattr(self.payer_participant_name, 'to_alipay_dict'):
                params['payer_participant_name'] = self.payer_participant_name.to_alipay_dict()
            else:
                params['payer_participant_name'] = self.payer_participant_name
        if self.payer_participant_type:
            if hasattr(self.payer_participant_type, 'to_alipay_dict'):
                params['payer_participant_type'] = self.payer_participant_type.to_alipay_dict()
            else:
                params['payer_participant_type'] = self.payer_participant_type
        if self.special_funds_amount:
            if hasattr(self.special_funds_amount, 'to_alipay_dict'):
                params['special_funds_amount'] = self.special_funds_amount.to_alipay_dict()
            else:
                params['special_funds_amount'] = self.special_funds_amount
        if self.special_funds_currency:
            if hasattr(self.special_funds_currency, 'to_alipay_dict'):
                params['special_funds_currency'] = self.special_funds_currency.to_alipay_dict()
            else:
                params['special_funds_currency'] = self.special_funds_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionAccountModifyModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_alipay_open_id' in d:
            o.merchant_alipay_open_id = d['merchant_alipay_open_id']
        if 'merchant_alipay_uid' in d:
            o.merchant_alipay_uid = d['merchant_alipay_uid']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_contact_line' in d:
            o.payee_contact_line = d['payee_contact_line']
        if 'payee_participant_id' in d:
            o.payee_participant_id = d['payee_participant_id']
        if 'payee_participant_name' in d:
            o.payee_participant_name = d['payee_participant_name']
        if 'payee_participant_type' in d:
            o.payee_participant_type = d['payee_participant_type']
        if 'payer_participant_id' in d:
            o.payer_participant_id = d['payer_participant_id']
        if 'payer_participant_name' in d:
            o.payer_participant_name = d['payer_participant_name']
        if 'payer_participant_type' in d:
            o.payer_participant_type = d['payer_participant_type']
        if 'special_funds_amount' in d:
            o.special_funds_amount = d['special_funds_amount']
        if 'special_funds_currency' in d:
            o.special_funds_currency = d['special_funds_currency']
        return o


