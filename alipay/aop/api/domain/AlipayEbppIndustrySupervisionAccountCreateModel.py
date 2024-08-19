#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionAccountCreateModel(object):

    def __init__(self):
        self._auto_refund = None
        self._biz_scene = None
        self._merchant_alipay_open_id = None
        self._merchant_alipay_uid = None
        self._out_user_id = None
        self._parent_ext_account_name = None
        self._parent_ext_account_no = None
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
        self._sub_account_type = None

    @property
    def auto_refund(self):
        return self._auto_refund

    @auto_refund.setter
    def auto_refund(self, value):
        self._auto_refund = value
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
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def parent_ext_account_name(self):
        return self._parent_ext_account_name

    @parent_ext_account_name.setter
    def parent_ext_account_name(self, value):
        self._parent_ext_account_name = value
    @property
    def parent_ext_account_no(self):
        return self._parent_ext_account_no

    @parent_ext_account_no.setter
    def parent_ext_account_no(self, value):
        self._parent_ext_account_no = value
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
    @property
    def sub_account_type(self):
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, value):
        self._sub_account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_refund:
            if hasattr(self.auto_refund, 'to_alipay_dict'):
                params['auto_refund'] = self.auto_refund.to_alipay_dict()
            else:
                params['auto_refund'] = self.auto_refund
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
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.parent_ext_account_name:
            if hasattr(self.parent_ext_account_name, 'to_alipay_dict'):
                params['parent_ext_account_name'] = self.parent_ext_account_name.to_alipay_dict()
            else:
                params['parent_ext_account_name'] = self.parent_ext_account_name
        if self.parent_ext_account_no:
            if hasattr(self.parent_ext_account_no, 'to_alipay_dict'):
                params['parent_ext_account_no'] = self.parent_ext_account_no.to_alipay_dict()
            else:
                params['parent_ext_account_no'] = self.parent_ext_account_no
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
        if self.sub_account_type:
            if hasattr(self.sub_account_type, 'to_alipay_dict'):
                params['sub_account_type'] = self.sub_account_type.to_alipay_dict()
            else:
                params['sub_account_type'] = self.sub_account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionAccountCreateModel()
        if 'auto_refund' in d:
            o.auto_refund = d['auto_refund']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_alipay_open_id' in d:
            o.merchant_alipay_open_id = d['merchant_alipay_open_id']
        if 'merchant_alipay_uid' in d:
            o.merchant_alipay_uid = d['merchant_alipay_uid']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'parent_ext_account_name' in d:
            o.parent_ext_account_name = d['parent_ext_account_name']
        if 'parent_ext_account_no' in d:
            o.parent_ext_account_no = d['parent_ext_account_no']
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
        if 'sub_account_type' in d:
            o.sub_account_type = d['sub_account_type']
        return o


