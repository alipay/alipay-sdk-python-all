#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.DailyCarRentalFee import DailyCarRentalFee
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem
from alipay.aop.api.domain.RentCarFeeItem import RentCarFeeItem


class RentCarOrderFeeInfo(object):

    def __init__(self):
        self._basic_guarantee_fee = None
        self._daily_car_rental_fee_detail = None
        self._home_return_fee = None
        self._home_send_fee = None
        self._more_guarantee_service_fee = None
        self._nigh_return_fee = None
        self._night_send_fee = None
        self._offsite_drop_off_fee = None
        self._other_fee_list = None
        self._rent_fee = None
        self._store_service_fee = None
        self._value_added_service_fee = None

    @property
    def basic_guarantee_fee(self):
        return self._basic_guarantee_fee

    @basic_guarantee_fee.setter
    def basic_guarantee_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._basic_guarantee_fee = value
        else:
            self._basic_guarantee_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def daily_car_rental_fee_detail(self):
        return self._daily_car_rental_fee_detail

    @daily_car_rental_fee_detail.setter
    def daily_car_rental_fee_detail(self, value):
        if isinstance(value, list):
            self._daily_car_rental_fee_detail = list()
            for i in value:
                if isinstance(i, DailyCarRentalFee):
                    self._daily_car_rental_fee_detail.append(i)
                else:
                    self._daily_car_rental_fee_detail.append(DailyCarRentalFee.from_alipay_dict(i))
    @property
    def home_return_fee(self):
        return self._home_return_fee

    @home_return_fee.setter
    def home_return_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._home_return_fee = value
        else:
            self._home_return_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def home_send_fee(self):
        return self._home_send_fee

    @home_send_fee.setter
    def home_send_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._home_send_fee = value
        else:
            self._home_send_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def more_guarantee_service_fee(self):
        return self._more_guarantee_service_fee

    @more_guarantee_service_fee.setter
    def more_guarantee_service_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._more_guarantee_service_fee = value
        else:
            self._more_guarantee_service_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def nigh_return_fee(self):
        return self._nigh_return_fee

    @nigh_return_fee.setter
    def nigh_return_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._nigh_return_fee = value
        else:
            self._nigh_return_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def night_send_fee(self):
        return self._night_send_fee

    @night_send_fee.setter
    def night_send_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._night_send_fee = value
        else:
            self._night_send_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def offsite_drop_off_fee(self):
        return self._offsite_drop_off_fee

    @offsite_drop_off_fee.setter
    def offsite_drop_off_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._offsite_drop_off_fee = value
        else:
            self._offsite_drop_off_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def other_fee_list(self):
        return self._other_fee_list

    @other_fee_list.setter
    def other_fee_list(self, value):
        if isinstance(value, list):
            self._other_fee_list = list()
            for i in value:
                if isinstance(i, RentCarFeeItem):
                    self._other_fee_list.append(i)
                else:
                    self._other_fee_list.append(RentCarFeeItem.from_alipay_dict(i))
    @property
    def rent_fee(self):
        return self._rent_fee

    @rent_fee.setter
    def rent_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._rent_fee = value
        else:
            self._rent_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def store_service_fee(self):
        return self._store_service_fee

    @store_service_fee.setter
    def store_service_fee(self, value):
        if isinstance(value, RentCarFeeItem):
            self._store_service_fee = value
        else:
            self._store_service_fee = RentCarFeeItem.from_alipay_dict(value)
    @property
    def value_added_service_fee(self):
        return self._value_added_service_fee

    @value_added_service_fee.setter
    def value_added_service_fee(self, value):
        if isinstance(value, list):
            self._value_added_service_fee = list()
            for i in value:
                if isinstance(i, RentCarFeeItem):
                    self._value_added_service_fee.append(i)
                else:
                    self._value_added_service_fee.append(RentCarFeeItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.basic_guarantee_fee:
            if hasattr(self.basic_guarantee_fee, 'to_alipay_dict'):
                params['basic_guarantee_fee'] = self.basic_guarantee_fee.to_alipay_dict()
            else:
                params['basic_guarantee_fee'] = self.basic_guarantee_fee
        if self.daily_car_rental_fee_detail:
            if isinstance(self.daily_car_rental_fee_detail, list):
                for i in range(0, len(self.daily_car_rental_fee_detail)):
                    element = self.daily_car_rental_fee_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.daily_car_rental_fee_detail[i] = element.to_alipay_dict()
            if hasattr(self.daily_car_rental_fee_detail, 'to_alipay_dict'):
                params['daily_car_rental_fee_detail'] = self.daily_car_rental_fee_detail.to_alipay_dict()
            else:
                params['daily_car_rental_fee_detail'] = self.daily_car_rental_fee_detail
        if self.home_return_fee:
            if hasattr(self.home_return_fee, 'to_alipay_dict'):
                params['home_return_fee'] = self.home_return_fee.to_alipay_dict()
            else:
                params['home_return_fee'] = self.home_return_fee
        if self.home_send_fee:
            if hasattr(self.home_send_fee, 'to_alipay_dict'):
                params['home_send_fee'] = self.home_send_fee.to_alipay_dict()
            else:
                params['home_send_fee'] = self.home_send_fee
        if self.more_guarantee_service_fee:
            if hasattr(self.more_guarantee_service_fee, 'to_alipay_dict'):
                params['more_guarantee_service_fee'] = self.more_guarantee_service_fee.to_alipay_dict()
            else:
                params['more_guarantee_service_fee'] = self.more_guarantee_service_fee
        if self.nigh_return_fee:
            if hasattr(self.nigh_return_fee, 'to_alipay_dict'):
                params['nigh_return_fee'] = self.nigh_return_fee.to_alipay_dict()
            else:
                params['nigh_return_fee'] = self.nigh_return_fee
        if self.night_send_fee:
            if hasattr(self.night_send_fee, 'to_alipay_dict'):
                params['night_send_fee'] = self.night_send_fee.to_alipay_dict()
            else:
                params['night_send_fee'] = self.night_send_fee
        if self.offsite_drop_off_fee:
            if hasattr(self.offsite_drop_off_fee, 'to_alipay_dict'):
                params['offsite_drop_off_fee'] = self.offsite_drop_off_fee.to_alipay_dict()
            else:
                params['offsite_drop_off_fee'] = self.offsite_drop_off_fee
        if self.other_fee_list:
            if isinstance(self.other_fee_list, list):
                for i in range(0, len(self.other_fee_list)):
                    element = self.other_fee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_fee_list[i] = element.to_alipay_dict()
            if hasattr(self.other_fee_list, 'to_alipay_dict'):
                params['other_fee_list'] = self.other_fee_list.to_alipay_dict()
            else:
                params['other_fee_list'] = self.other_fee_list
        if self.rent_fee:
            if hasattr(self.rent_fee, 'to_alipay_dict'):
                params['rent_fee'] = self.rent_fee.to_alipay_dict()
            else:
                params['rent_fee'] = self.rent_fee
        if self.store_service_fee:
            if hasattr(self.store_service_fee, 'to_alipay_dict'):
                params['store_service_fee'] = self.store_service_fee.to_alipay_dict()
            else:
                params['store_service_fee'] = self.store_service_fee
        if self.value_added_service_fee:
            if isinstance(self.value_added_service_fee, list):
                for i in range(0, len(self.value_added_service_fee)):
                    element = self.value_added_service_fee[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value_added_service_fee[i] = element.to_alipay_dict()
            if hasattr(self.value_added_service_fee, 'to_alipay_dict'):
                params['value_added_service_fee'] = self.value_added_service_fee.to_alipay_dict()
            else:
                params['value_added_service_fee'] = self.value_added_service_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarOrderFeeInfo()
        if 'basic_guarantee_fee' in d:
            o.basic_guarantee_fee = d['basic_guarantee_fee']
        if 'daily_car_rental_fee_detail' in d:
            o.daily_car_rental_fee_detail = d['daily_car_rental_fee_detail']
        if 'home_return_fee' in d:
            o.home_return_fee = d['home_return_fee']
        if 'home_send_fee' in d:
            o.home_send_fee = d['home_send_fee']
        if 'more_guarantee_service_fee' in d:
            o.more_guarantee_service_fee = d['more_guarantee_service_fee']
        if 'nigh_return_fee' in d:
            o.nigh_return_fee = d['nigh_return_fee']
        if 'night_send_fee' in d:
            o.night_send_fee = d['night_send_fee']
        if 'offsite_drop_off_fee' in d:
            o.offsite_drop_off_fee = d['offsite_drop_off_fee']
        if 'other_fee_list' in d:
            o.other_fee_list = d['other_fee_list']
        if 'rent_fee' in d:
            o.rent_fee = d['rent_fee']
        if 'store_service_fee' in d:
            o.store_service_fee = d['store_service_fee']
        if 'value_added_service_fee' in d:
            o.value_added_service_fee = d['value_added_service_fee']
        return o


