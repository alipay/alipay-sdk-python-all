#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardSubAccountResult import CardSubAccountResult


class GiftCardVo(object):

    def __init__(self):
        self._available_amount = None
        self._denomination = None
        self._effective_period = None
        self._gift_card_instance_no = None
        self._gift_card_instance_status = None
        self._gift_card_name = None
        self._gift_card_no = None
        self._gift_card_status = None
        self._gmt_create = None
        self._merchant_id = None
        self._sub_account_info = None
        self._user_id = None
        self._valid_period = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        self._effective_period = value
    @property
    def gift_card_instance_no(self):
        return self._gift_card_instance_no

    @gift_card_instance_no.setter
    def gift_card_instance_no(self, value):
        self._gift_card_instance_no = value
    @property
    def gift_card_instance_status(self):
        return self._gift_card_instance_status

    @gift_card_instance_status.setter
    def gift_card_instance_status(self, value):
        self._gift_card_instance_status = value
    @property
    def gift_card_name(self):
        return self._gift_card_name

    @gift_card_name.setter
    def gift_card_name(self, value):
        self._gift_card_name = value
    @property
    def gift_card_no(self):
        return self._gift_card_no

    @gift_card_no.setter
    def gift_card_no(self, value):
        self._gift_card_no = value
    @property
    def gift_card_status(self):
        return self._gift_card_status

    @gift_card_status.setter
    def gift_card_status(self, value):
        self._gift_card_status = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def sub_account_info(self):
        return self._sub_account_info

    @sub_account_info.setter
    def sub_account_info(self, value):
        if isinstance(value, CardSubAccountResult):
            self._sub_account_info = value
        else:
            self._sub_account_info = CardSubAccountResult.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.effective_period:
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.gift_card_instance_no:
            if hasattr(self.gift_card_instance_no, 'to_alipay_dict'):
                params['gift_card_instance_no'] = self.gift_card_instance_no.to_alipay_dict()
            else:
                params['gift_card_instance_no'] = self.gift_card_instance_no
        if self.gift_card_instance_status:
            if hasattr(self.gift_card_instance_status, 'to_alipay_dict'):
                params['gift_card_instance_status'] = self.gift_card_instance_status.to_alipay_dict()
            else:
                params['gift_card_instance_status'] = self.gift_card_instance_status
        if self.gift_card_name:
            if hasattr(self.gift_card_name, 'to_alipay_dict'):
                params['gift_card_name'] = self.gift_card_name.to_alipay_dict()
            else:
                params['gift_card_name'] = self.gift_card_name
        if self.gift_card_no:
            if hasattr(self.gift_card_no, 'to_alipay_dict'):
                params['gift_card_no'] = self.gift_card_no.to_alipay_dict()
            else:
                params['gift_card_no'] = self.gift_card_no
        if self.gift_card_status:
            if hasattr(self.gift_card_status, 'to_alipay_dict'):
                params['gift_card_status'] = self.gift_card_status.to_alipay_dict()
            else:
                params['gift_card_status'] = self.gift_card_status
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.sub_account_info:
            if hasattr(self.sub_account_info, 'to_alipay_dict'):
                params['sub_account_info'] = self.sub_account_info.to_alipay_dict()
            else:
                params['sub_account_info'] = self.sub_account_info
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftCardVo()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'gift_card_instance_no' in d:
            o.gift_card_instance_no = d['gift_card_instance_no']
        if 'gift_card_instance_status' in d:
            o.gift_card_instance_status = d['gift_card_instance_status']
        if 'gift_card_name' in d:
            o.gift_card_name = d['gift_card_name']
        if 'gift_card_no' in d:
            o.gift_card_no = d['gift_card_no']
        if 'gift_card_status' in d:
            o.gift_card_status = d['gift_card_status']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'sub_account_info' in d:
            o.sub_account_info = d['sub_account_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        return o


