#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentBillRoyaltyDto(object):

    def __init__(self):
        self._actual_royalty_interest_price = None
        self._actual_royalty_price = None
        self._actual_royalty_principal_price = None
        self._current_buyout_price = None
        self._key_royalty_installment_no = None
        self._period = None
        self._royalty_id = None
        self._royalty_status = None
        self._stage = None
        self._type = None

    @property
    def actual_royalty_interest_price(self):
        return self._actual_royalty_interest_price

    @actual_royalty_interest_price.setter
    def actual_royalty_interest_price(self, value):
        self._actual_royalty_interest_price = value
    @property
    def actual_royalty_price(self):
        return self._actual_royalty_price

    @actual_royalty_price.setter
    def actual_royalty_price(self, value):
        self._actual_royalty_price = value
    @property
    def actual_royalty_principal_price(self):
        return self._actual_royalty_principal_price

    @actual_royalty_principal_price.setter
    def actual_royalty_principal_price(self, value):
        self._actual_royalty_principal_price = value
    @property
    def current_buyout_price(self):
        return self._current_buyout_price

    @current_buyout_price.setter
    def current_buyout_price(self, value):
        self._current_buyout_price = value
    @property
    def key_royalty_installment_no(self):
        return self._key_royalty_installment_no

    @key_royalty_installment_no.setter
    def key_royalty_installment_no(self, value):
        self._key_royalty_installment_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def royalty_id(self):
        return self._royalty_id

    @royalty_id.setter
    def royalty_id(self, value):
        self._royalty_id = value
    @property
    def royalty_status(self):
        return self._royalty_status

    @royalty_status.setter
    def royalty_status(self, value):
        self._royalty_status = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_royalty_interest_price:
            if hasattr(self.actual_royalty_interest_price, 'to_alipay_dict'):
                params['actual_royalty_interest_price'] = self.actual_royalty_interest_price.to_alipay_dict()
            else:
                params['actual_royalty_interest_price'] = self.actual_royalty_interest_price
        if self.actual_royalty_price:
            if hasattr(self.actual_royalty_price, 'to_alipay_dict'):
                params['actual_royalty_price'] = self.actual_royalty_price.to_alipay_dict()
            else:
                params['actual_royalty_price'] = self.actual_royalty_price
        if self.actual_royalty_principal_price:
            if hasattr(self.actual_royalty_principal_price, 'to_alipay_dict'):
                params['actual_royalty_principal_price'] = self.actual_royalty_principal_price.to_alipay_dict()
            else:
                params['actual_royalty_principal_price'] = self.actual_royalty_principal_price
        if self.current_buyout_price:
            if hasattr(self.current_buyout_price, 'to_alipay_dict'):
                params['current_buyout_price'] = self.current_buyout_price.to_alipay_dict()
            else:
                params['current_buyout_price'] = self.current_buyout_price
        if self.key_royalty_installment_no:
            if hasattr(self.key_royalty_installment_no, 'to_alipay_dict'):
                params['key_royalty_installment_no'] = self.key_royalty_installment_no.to_alipay_dict()
            else:
                params['key_royalty_installment_no'] = self.key_royalty_installment_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.royalty_id:
            if hasattr(self.royalty_id, 'to_alipay_dict'):
                params['royalty_id'] = self.royalty_id.to_alipay_dict()
            else:
                params['royalty_id'] = self.royalty_id
        if self.royalty_status:
            if hasattr(self.royalty_status, 'to_alipay_dict'):
                params['royalty_status'] = self.royalty_status.to_alipay_dict()
            else:
                params['royalty_status'] = self.royalty_status
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentBillRoyaltyDto()
        if 'actual_royalty_interest_price' in d:
            o.actual_royalty_interest_price = d['actual_royalty_interest_price']
        if 'actual_royalty_price' in d:
            o.actual_royalty_price = d['actual_royalty_price']
        if 'actual_royalty_principal_price' in d:
            o.actual_royalty_principal_price = d['actual_royalty_principal_price']
        if 'current_buyout_price' in d:
            o.current_buyout_price = d['current_buyout_price']
        if 'key_royalty_installment_no' in d:
            o.key_royalty_installment_no = d['key_royalty_installment_no']
        if 'period' in d:
            o.period = d['period']
        if 'royalty_id' in d:
            o.royalty_id = d['royalty_id']
        if 'royalty_status' in d:
            o.royalty_status = d['royalty_status']
        if 'stage' in d:
            o.stage = d['stage']
        if 'type' in d:
            o.type = d['type']
        return o


