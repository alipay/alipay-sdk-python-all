#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentHouseEquipmentVO import RentHouseEquipmentVO


class RentContractViewVO(object):

    def __init__(self):
        self._contract_id = None
        self._contract_notes = None
        self._deposit_amount = None
        self._equipment_list = None
        self._landlord_id_number = None
        self._landlord_name = None
        self._landlord_phone = None
        self._pay_period_type = None
        self._rent_amount = None
        self._rent_mouth = None
        self._rent_start_date = None
        self._renter_id_number = None
        self._renter_name = None
        self._renter_phone = None
        self._room_address = None
        self._room_area = None
        self._room_notes = None
        self._room_rent_type = None
        self._support_no_deposit = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_notes(self):
        return self._contract_notes

    @contract_notes.setter
    def contract_notes(self, value):
        self._contract_notes = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def equipment_list(self):
        return self._equipment_list

    @equipment_list.setter
    def equipment_list(self, value):
        if isinstance(value, list):
            self._equipment_list = list()
            for i in value:
                if isinstance(i, RentHouseEquipmentVO):
                    self._equipment_list.append(i)
                else:
                    self._equipment_list.append(RentHouseEquipmentVO.from_alipay_dict(i))
    @property
    def landlord_id_number(self):
        return self._landlord_id_number

    @landlord_id_number.setter
    def landlord_id_number(self, value):
        self._landlord_id_number = value
    @property
    def landlord_name(self):
        return self._landlord_name

    @landlord_name.setter
    def landlord_name(self, value):
        self._landlord_name = value
    @property
    def landlord_phone(self):
        return self._landlord_phone

    @landlord_phone.setter
    def landlord_phone(self, value):
        self._landlord_phone = value
    @property
    def pay_period_type(self):
        return self._pay_period_type

    @pay_period_type.setter
    def pay_period_type(self, value):
        self._pay_period_type = value
    @property
    def rent_amount(self):
        return self._rent_amount

    @rent_amount.setter
    def rent_amount(self, value):
        self._rent_amount = value
    @property
    def rent_mouth(self):
        return self._rent_mouth

    @rent_mouth.setter
    def rent_mouth(self, value):
        self._rent_mouth = value
    @property
    def rent_start_date(self):
        return self._rent_start_date

    @rent_start_date.setter
    def rent_start_date(self, value):
        self._rent_start_date = value
    @property
    def renter_id_number(self):
        return self._renter_id_number

    @renter_id_number.setter
    def renter_id_number(self, value):
        self._renter_id_number = value
    @property
    def renter_name(self):
        return self._renter_name

    @renter_name.setter
    def renter_name(self, value):
        self._renter_name = value
    @property
    def renter_phone(self):
        return self._renter_phone

    @renter_phone.setter
    def renter_phone(self, value):
        self._renter_phone = value
    @property
    def room_address(self):
        return self._room_address

    @room_address.setter
    def room_address(self, value):
        self._room_address = value
    @property
    def room_area(self):
        return self._room_area

    @room_area.setter
    def room_area(self, value):
        self._room_area = value
    @property
    def room_notes(self):
        return self._room_notes

    @room_notes.setter
    def room_notes(self, value):
        self._room_notes = value
    @property
    def room_rent_type(self):
        return self._room_rent_type

    @room_rent_type.setter
    def room_rent_type(self, value):
        self._room_rent_type = value
    @property
    def support_no_deposit(self):
        return self._support_no_deposit

    @support_no_deposit.setter
    def support_no_deposit(self, value):
        self._support_no_deposit = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_notes:
            if hasattr(self.contract_notes, 'to_alipay_dict'):
                params['contract_notes'] = self.contract_notes.to_alipay_dict()
            else:
                params['contract_notes'] = self.contract_notes
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.equipment_list:
            if isinstance(self.equipment_list, list):
                for i in range(0, len(self.equipment_list)):
                    element = self.equipment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.equipment_list[i] = element.to_alipay_dict()
            if hasattr(self.equipment_list, 'to_alipay_dict'):
                params['equipment_list'] = self.equipment_list.to_alipay_dict()
            else:
                params['equipment_list'] = self.equipment_list
        if self.landlord_id_number:
            if hasattr(self.landlord_id_number, 'to_alipay_dict'):
                params['landlord_id_number'] = self.landlord_id_number.to_alipay_dict()
            else:
                params['landlord_id_number'] = self.landlord_id_number
        if self.landlord_name:
            if hasattr(self.landlord_name, 'to_alipay_dict'):
                params['landlord_name'] = self.landlord_name.to_alipay_dict()
            else:
                params['landlord_name'] = self.landlord_name
        if self.landlord_phone:
            if hasattr(self.landlord_phone, 'to_alipay_dict'):
                params['landlord_phone'] = self.landlord_phone.to_alipay_dict()
            else:
                params['landlord_phone'] = self.landlord_phone
        if self.pay_period_type:
            if hasattr(self.pay_period_type, 'to_alipay_dict'):
                params['pay_period_type'] = self.pay_period_type.to_alipay_dict()
            else:
                params['pay_period_type'] = self.pay_period_type
        if self.rent_amount:
            if hasattr(self.rent_amount, 'to_alipay_dict'):
                params['rent_amount'] = self.rent_amount.to_alipay_dict()
            else:
                params['rent_amount'] = self.rent_amount
        if self.rent_mouth:
            if hasattr(self.rent_mouth, 'to_alipay_dict'):
                params['rent_mouth'] = self.rent_mouth.to_alipay_dict()
            else:
                params['rent_mouth'] = self.rent_mouth
        if self.rent_start_date:
            if hasattr(self.rent_start_date, 'to_alipay_dict'):
                params['rent_start_date'] = self.rent_start_date.to_alipay_dict()
            else:
                params['rent_start_date'] = self.rent_start_date
        if self.renter_id_number:
            if hasattr(self.renter_id_number, 'to_alipay_dict'):
                params['renter_id_number'] = self.renter_id_number.to_alipay_dict()
            else:
                params['renter_id_number'] = self.renter_id_number
        if self.renter_name:
            if hasattr(self.renter_name, 'to_alipay_dict'):
                params['renter_name'] = self.renter_name.to_alipay_dict()
            else:
                params['renter_name'] = self.renter_name
        if self.renter_phone:
            if hasattr(self.renter_phone, 'to_alipay_dict'):
                params['renter_phone'] = self.renter_phone.to_alipay_dict()
            else:
                params['renter_phone'] = self.renter_phone
        if self.room_address:
            if hasattr(self.room_address, 'to_alipay_dict'):
                params['room_address'] = self.room_address.to_alipay_dict()
            else:
                params['room_address'] = self.room_address
        if self.room_area:
            if hasattr(self.room_area, 'to_alipay_dict'):
                params['room_area'] = self.room_area.to_alipay_dict()
            else:
                params['room_area'] = self.room_area
        if self.room_notes:
            if hasattr(self.room_notes, 'to_alipay_dict'):
                params['room_notes'] = self.room_notes.to_alipay_dict()
            else:
                params['room_notes'] = self.room_notes
        if self.room_rent_type:
            if hasattr(self.room_rent_type, 'to_alipay_dict'):
                params['room_rent_type'] = self.room_rent_type.to_alipay_dict()
            else:
                params['room_rent_type'] = self.room_rent_type
        if self.support_no_deposit:
            if hasattr(self.support_no_deposit, 'to_alipay_dict'):
                params['support_no_deposit'] = self.support_no_deposit.to_alipay_dict()
            else:
                params['support_no_deposit'] = self.support_no_deposit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentContractViewVO()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_notes' in d:
            o.contract_notes = d['contract_notes']
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'equipment_list' in d:
            o.equipment_list = d['equipment_list']
        if 'landlord_id_number' in d:
            o.landlord_id_number = d['landlord_id_number']
        if 'landlord_name' in d:
            o.landlord_name = d['landlord_name']
        if 'landlord_phone' in d:
            o.landlord_phone = d['landlord_phone']
        if 'pay_period_type' in d:
            o.pay_period_type = d['pay_period_type']
        if 'rent_amount' in d:
            o.rent_amount = d['rent_amount']
        if 'rent_mouth' in d:
            o.rent_mouth = d['rent_mouth']
        if 'rent_start_date' in d:
            o.rent_start_date = d['rent_start_date']
        if 'renter_id_number' in d:
            o.renter_id_number = d['renter_id_number']
        if 'renter_name' in d:
            o.renter_name = d['renter_name']
        if 'renter_phone' in d:
            o.renter_phone = d['renter_phone']
        if 'room_address' in d:
            o.room_address = d['room_address']
        if 'room_area' in d:
            o.room_area = d['room_area']
        if 'room_notes' in d:
            o.room_notes = d['room_notes']
        if 'room_rent_type' in d:
            o.room_rent_type = d['room_rent_type']
        if 'support_no_deposit' in d:
            o.support_no_deposit = d['support_no_deposit']
        return o


