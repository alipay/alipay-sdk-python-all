#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressBean import AddressBean
from alipay.aop.api.domain.AddressBean import AddressBean


class AlipayOfflineSmddShopJoinNotifyModel(object):

    def __init__(self):
        self._audit_memo = None
        self._audit_status = None
        self._bank_account_type = None
        self._bank_address = None
        self._bank_branch_name = None
        self._bank_card_front_pic = None
        self._bank_card_number = None
        self._bank_name = None
        self._business_entity_type = None
        self._business_environment_pic = None
        self._business_license_end_date = None
        self._business_license_pic = None
        self._business_license_start_date = None
        self._cashier_desk_pic = None
        self._company_address = None
        self._company_code = None
        self._company_code_type = None
        self._company_full_name = None
        self._emergency_contact_phone = None
        self._establishment_date = None
        self._id_card_address = None
        self._id_card_back_pic = None
        self._id_card_end_date = None
        self._id_card_front_pic = None
        self._id_card_start_date = None
        self._legal_person_id_number = None
        self._legal_person_name = None
        self._legal_person_phone = None
        self._merchant_id = None
        self._merchant_short_name = None
        self._out_door_pic = None
        self._out_order_id = None
        self._thirdpay_mer_id = None
        self._thirdpay_org = None

    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def bank_account_type(self):
        return self._bank_account_type

    @bank_account_type.setter
    def bank_account_type(self, value):
        self._bank_account_type = value
    @property
    def bank_address(self):
        return self._bank_address

    @bank_address.setter
    def bank_address(self, value):
        if isinstance(value, AddressBean):
            self._bank_address = value
        else:
            self._bank_address = AddressBean.from_alipay_dict(value)
    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def bank_card_front_pic(self):
        return self._bank_card_front_pic

    @bank_card_front_pic.setter
    def bank_card_front_pic(self, value):
        self._bank_card_front_pic = value
    @property
    def bank_card_number(self):
        return self._bank_card_number

    @bank_card_number.setter
    def bank_card_number(self, value):
        self._bank_card_number = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def business_entity_type(self):
        return self._business_entity_type

    @business_entity_type.setter
    def business_entity_type(self, value):
        self._business_entity_type = value
    @property
    def business_environment_pic(self):
        return self._business_environment_pic

    @business_environment_pic.setter
    def business_environment_pic(self, value):
        self._business_environment_pic = value
    @property
    def business_license_end_date(self):
        return self._business_license_end_date

    @business_license_end_date.setter
    def business_license_end_date(self, value):
        self._business_license_end_date = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def business_license_start_date(self):
        return self._business_license_start_date

    @business_license_start_date.setter
    def business_license_start_date(self, value):
        self._business_license_start_date = value
    @property
    def cashier_desk_pic(self):
        return self._cashier_desk_pic

    @cashier_desk_pic.setter
    def cashier_desk_pic(self, value):
        self._cashier_desk_pic = value
    @property
    def company_address(self):
        return self._company_address

    @company_address.setter
    def company_address(self, value):
        if isinstance(value, AddressBean):
            self._company_address = value
        else:
            self._company_address = AddressBean.from_alipay_dict(value)
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_code_type(self):
        return self._company_code_type

    @company_code_type.setter
    def company_code_type(self, value):
        self._company_code_type = value
    @property
    def company_full_name(self):
        return self._company_full_name

    @company_full_name.setter
    def company_full_name(self, value):
        self._company_full_name = value
    @property
    def emergency_contact_phone(self):
        return self._emergency_contact_phone

    @emergency_contact_phone.setter
    def emergency_contact_phone(self, value):
        self._emergency_contact_phone = value
    @property
    def establishment_date(self):
        return self._establishment_date

    @establishment_date.setter
    def establishment_date(self, value):
        self._establishment_date = value
    @property
    def id_card_address(self):
        return self._id_card_address

    @id_card_address.setter
    def id_card_address(self, value):
        self._id_card_address = value
    @property
    def id_card_back_pic(self):
        return self._id_card_back_pic

    @id_card_back_pic.setter
    def id_card_back_pic(self, value):
        self._id_card_back_pic = value
    @property
    def id_card_end_date(self):
        return self._id_card_end_date

    @id_card_end_date.setter
    def id_card_end_date(self, value):
        self._id_card_end_date = value
    @property
    def id_card_front_pic(self):
        return self._id_card_front_pic

    @id_card_front_pic.setter
    def id_card_front_pic(self, value):
        self._id_card_front_pic = value
    @property
    def id_card_start_date(self):
        return self._id_card_start_date

    @id_card_start_date.setter
    def id_card_start_date(self, value):
        self._id_card_start_date = value
    @property
    def legal_person_id_number(self):
        return self._legal_person_id_number

    @legal_person_id_number.setter
    def legal_person_id_number(self, value):
        self._legal_person_id_number = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def legal_person_phone(self):
        return self._legal_person_phone

    @legal_person_phone.setter
    def legal_person_phone(self, value):
        self._legal_person_phone = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_short_name(self):
        return self._merchant_short_name

    @merchant_short_name.setter
    def merchant_short_name(self, value):
        self._merchant_short_name = value
    @property
    def out_door_pic(self):
        return self._out_door_pic

    @out_door_pic.setter
    def out_door_pic(self, value):
        self._out_door_pic = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def thirdpay_mer_id(self):
        return self._thirdpay_mer_id

    @thirdpay_mer_id.setter
    def thirdpay_mer_id(self, value):
        self._thirdpay_mer_id = value
    @property
    def thirdpay_org(self):
        return self._thirdpay_org

    @thirdpay_org.setter
    def thirdpay_org(self, value):
        self._thirdpay_org = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_memo:
            if hasattr(self.audit_memo, 'to_alipay_dict'):
                params['audit_memo'] = self.audit_memo.to_alipay_dict()
            else:
                params['audit_memo'] = self.audit_memo
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.bank_account_type:
            if hasattr(self.bank_account_type, 'to_alipay_dict'):
                params['bank_account_type'] = self.bank_account_type.to_alipay_dict()
            else:
                params['bank_account_type'] = self.bank_account_type
        if self.bank_address:
            if hasattr(self.bank_address, 'to_alipay_dict'):
                params['bank_address'] = self.bank_address.to_alipay_dict()
            else:
                params['bank_address'] = self.bank_address
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.bank_card_front_pic:
            if hasattr(self.bank_card_front_pic, 'to_alipay_dict'):
                params['bank_card_front_pic'] = self.bank_card_front_pic.to_alipay_dict()
            else:
                params['bank_card_front_pic'] = self.bank_card_front_pic
        if self.bank_card_number:
            if hasattr(self.bank_card_number, 'to_alipay_dict'):
                params['bank_card_number'] = self.bank_card_number.to_alipay_dict()
            else:
                params['bank_card_number'] = self.bank_card_number
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.business_entity_type:
            if hasattr(self.business_entity_type, 'to_alipay_dict'):
                params['business_entity_type'] = self.business_entity_type.to_alipay_dict()
            else:
                params['business_entity_type'] = self.business_entity_type
        if self.business_environment_pic:
            if hasattr(self.business_environment_pic, 'to_alipay_dict'):
                params['business_environment_pic'] = self.business_environment_pic.to_alipay_dict()
            else:
                params['business_environment_pic'] = self.business_environment_pic
        if self.business_license_end_date:
            if hasattr(self.business_license_end_date, 'to_alipay_dict'):
                params['business_license_end_date'] = self.business_license_end_date.to_alipay_dict()
            else:
                params['business_license_end_date'] = self.business_license_end_date
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.business_license_start_date:
            if hasattr(self.business_license_start_date, 'to_alipay_dict'):
                params['business_license_start_date'] = self.business_license_start_date.to_alipay_dict()
            else:
                params['business_license_start_date'] = self.business_license_start_date
        if self.cashier_desk_pic:
            if hasattr(self.cashier_desk_pic, 'to_alipay_dict'):
                params['cashier_desk_pic'] = self.cashier_desk_pic.to_alipay_dict()
            else:
                params['cashier_desk_pic'] = self.cashier_desk_pic
        if self.company_address:
            if hasattr(self.company_address, 'to_alipay_dict'):
                params['company_address'] = self.company_address.to_alipay_dict()
            else:
                params['company_address'] = self.company_address
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_code_type:
            if hasattr(self.company_code_type, 'to_alipay_dict'):
                params['company_code_type'] = self.company_code_type.to_alipay_dict()
            else:
                params['company_code_type'] = self.company_code_type
        if self.company_full_name:
            if hasattr(self.company_full_name, 'to_alipay_dict'):
                params['company_full_name'] = self.company_full_name.to_alipay_dict()
            else:
                params['company_full_name'] = self.company_full_name
        if self.emergency_contact_phone:
            if hasattr(self.emergency_contact_phone, 'to_alipay_dict'):
                params['emergency_contact_phone'] = self.emergency_contact_phone.to_alipay_dict()
            else:
                params['emergency_contact_phone'] = self.emergency_contact_phone
        if self.establishment_date:
            if hasattr(self.establishment_date, 'to_alipay_dict'):
                params['establishment_date'] = self.establishment_date.to_alipay_dict()
            else:
                params['establishment_date'] = self.establishment_date
        if self.id_card_address:
            if hasattr(self.id_card_address, 'to_alipay_dict'):
                params['id_card_address'] = self.id_card_address.to_alipay_dict()
            else:
                params['id_card_address'] = self.id_card_address
        if self.id_card_back_pic:
            if hasattr(self.id_card_back_pic, 'to_alipay_dict'):
                params['id_card_back_pic'] = self.id_card_back_pic.to_alipay_dict()
            else:
                params['id_card_back_pic'] = self.id_card_back_pic
        if self.id_card_end_date:
            if hasattr(self.id_card_end_date, 'to_alipay_dict'):
                params['id_card_end_date'] = self.id_card_end_date.to_alipay_dict()
            else:
                params['id_card_end_date'] = self.id_card_end_date
        if self.id_card_front_pic:
            if hasattr(self.id_card_front_pic, 'to_alipay_dict'):
                params['id_card_front_pic'] = self.id_card_front_pic.to_alipay_dict()
            else:
                params['id_card_front_pic'] = self.id_card_front_pic
        if self.id_card_start_date:
            if hasattr(self.id_card_start_date, 'to_alipay_dict'):
                params['id_card_start_date'] = self.id_card_start_date.to_alipay_dict()
            else:
                params['id_card_start_date'] = self.id_card_start_date
        if self.legal_person_id_number:
            if hasattr(self.legal_person_id_number, 'to_alipay_dict'):
                params['legal_person_id_number'] = self.legal_person_id_number.to_alipay_dict()
            else:
                params['legal_person_id_number'] = self.legal_person_id_number
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.legal_person_phone:
            if hasattr(self.legal_person_phone, 'to_alipay_dict'):
                params['legal_person_phone'] = self.legal_person_phone.to_alipay_dict()
            else:
                params['legal_person_phone'] = self.legal_person_phone
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_short_name:
            if hasattr(self.merchant_short_name, 'to_alipay_dict'):
                params['merchant_short_name'] = self.merchant_short_name.to_alipay_dict()
            else:
                params['merchant_short_name'] = self.merchant_short_name
        if self.out_door_pic:
            if hasattr(self.out_door_pic, 'to_alipay_dict'):
                params['out_door_pic'] = self.out_door_pic.to_alipay_dict()
            else:
                params['out_door_pic'] = self.out_door_pic
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.thirdpay_mer_id:
            if hasattr(self.thirdpay_mer_id, 'to_alipay_dict'):
                params['thirdpay_mer_id'] = self.thirdpay_mer_id.to_alipay_dict()
            else:
                params['thirdpay_mer_id'] = self.thirdpay_mer_id
        if self.thirdpay_org:
            if hasattr(self.thirdpay_org, 'to_alipay_dict'):
                params['thirdpay_org'] = self.thirdpay_org.to_alipay_dict()
            else:
                params['thirdpay_org'] = self.thirdpay_org
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddShopJoinNotifyModel()
        if 'audit_memo' in d:
            o.audit_memo = d['audit_memo']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'bank_account_type' in d:
            o.bank_account_type = d['bank_account_type']
        if 'bank_address' in d:
            o.bank_address = d['bank_address']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'bank_card_front_pic' in d:
            o.bank_card_front_pic = d['bank_card_front_pic']
        if 'bank_card_number' in d:
            o.bank_card_number = d['bank_card_number']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'business_entity_type' in d:
            o.business_entity_type = d['business_entity_type']
        if 'business_environment_pic' in d:
            o.business_environment_pic = d['business_environment_pic']
        if 'business_license_end_date' in d:
            o.business_license_end_date = d['business_license_end_date']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'business_license_start_date' in d:
            o.business_license_start_date = d['business_license_start_date']
        if 'cashier_desk_pic' in d:
            o.cashier_desk_pic = d['cashier_desk_pic']
        if 'company_address' in d:
            o.company_address = d['company_address']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_code_type' in d:
            o.company_code_type = d['company_code_type']
        if 'company_full_name' in d:
            o.company_full_name = d['company_full_name']
        if 'emergency_contact_phone' in d:
            o.emergency_contact_phone = d['emergency_contact_phone']
        if 'establishment_date' in d:
            o.establishment_date = d['establishment_date']
        if 'id_card_address' in d:
            o.id_card_address = d['id_card_address']
        if 'id_card_back_pic' in d:
            o.id_card_back_pic = d['id_card_back_pic']
        if 'id_card_end_date' in d:
            o.id_card_end_date = d['id_card_end_date']
        if 'id_card_front_pic' in d:
            o.id_card_front_pic = d['id_card_front_pic']
        if 'id_card_start_date' in d:
            o.id_card_start_date = d['id_card_start_date']
        if 'legal_person_id_number' in d:
            o.legal_person_id_number = d['legal_person_id_number']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'legal_person_phone' in d:
            o.legal_person_phone = d['legal_person_phone']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_short_name' in d:
            o.merchant_short_name = d['merchant_short_name']
        if 'out_door_pic' in d:
            o.out_door_pic = d['out_door_pic']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'thirdpay_mer_id' in d:
            o.thirdpay_mer_id = d['thirdpay_mer_id']
        if 'thirdpay_org' in d:
            o.thirdpay_org = d['thirdpay_org']
        return o


