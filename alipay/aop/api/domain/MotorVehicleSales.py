#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MotorVehicleSales(object):

    def __init__(self):
        self._amount = None
        self._buyer_name = None
        self._buyer_org_code = None
        self._buyer_tax_no = None
        self._certificate_no = None
        self._engine_no = None
        self._factory_model = None
        self._import_proof_no = None
        self._inspection_no = None
        self._machine_no = None
        self._origin_place = None
        self._passenger_capacity = None
        self._payment_voucher_no = None
        self._seller_account = None
        self._seller_address = None
        self._seller_bank = None
        self._seller_name = None
        self._seller_tax_no = None
        self._seller_tel = None
        self._tax_amount = None
        self._tax_authority = None
        self._tax_authority_code = None
        self._tax_rate = None
        self._tonnage = None
        self._total_amount = None
        self._vehicle_identification_no = None
        self._vehicle_type = None
        self._verify_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_org_code(self):
        return self._buyer_org_code

    @buyer_org_code.setter
    def buyer_org_code(self, value):
        self._buyer_org_code = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def certificate_no(self):
        return self._certificate_no

    @certificate_no.setter
    def certificate_no(self, value):
        self._certificate_no = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def factory_model(self):
        return self._factory_model

    @factory_model.setter
    def factory_model(self, value):
        self._factory_model = value
    @property
    def import_proof_no(self):
        return self._import_proof_no

    @import_proof_no.setter
    def import_proof_no(self, value):
        self._import_proof_no = value
    @property
    def inspection_no(self):
        return self._inspection_no

    @inspection_no.setter
    def inspection_no(self, value):
        self._inspection_no = value
    @property
    def machine_no(self):
        return self._machine_no

    @machine_no.setter
    def machine_no(self, value):
        self._machine_no = value
    @property
    def origin_place(self):
        return self._origin_place

    @origin_place.setter
    def origin_place(self, value):
        self._origin_place = value
    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        self._passenger_capacity = value
    @property
    def payment_voucher_no(self):
        return self._payment_voucher_no

    @payment_voucher_no.setter
    def payment_voucher_no(self, value):
        self._payment_voucher_no = value
    @property
    def seller_account(self):
        return self._seller_account

    @seller_account.setter
    def seller_account(self, value):
        self._seller_account = value
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank(self):
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, value):
        self._seller_bank = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_tel(self):
        return self._seller_tel

    @seller_tel.setter
    def seller_tel(self, value):
        self._seller_tel = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_authority(self):
        return self._tax_authority

    @tax_authority.setter
    def tax_authority(self, value):
        self._tax_authority = value
    @property
    def tax_authority_code(self):
        return self._tax_authority_code

    @tax_authority_code.setter
    def tax_authority_code(self, value):
        self._tax_authority_code = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tonnage(self):
        return self._tonnage

    @tonnage.setter
    def tonnage(self, value):
        self._tonnage = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def vehicle_identification_no(self):
        return self._vehicle_identification_no

    @vehicle_identification_no.setter
    def vehicle_identification_no(self, value):
        self._vehicle_identification_no = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def verify_time(self):
        return self._verify_time

    @verify_time.setter
    def verify_time(self, value):
        self._verify_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_org_code:
            if hasattr(self.buyer_org_code, 'to_alipay_dict'):
                params['buyer_org_code'] = self.buyer_org_code.to_alipay_dict()
            else:
                params['buyer_org_code'] = self.buyer_org_code
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.certificate_no:
            if hasattr(self.certificate_no, 'to_alipay_dict'):
                params['certificate_no'] = self.certificate_no.to_alipay_dict()
            else:
                params['certificate_no'] = self.certificate_no
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.factory_model:
            if hasattr(self.factory_model, 'to_alipay_dict'):
                params['factory_model'] = self.factory_model.to_alipay_dict()
            else:
                params['factory_model'] = self.factory_model
        if self.import_proof_no:
            if hasattr(self.import_proof_no, 'to_alipay_dict'):
                params['import_proof_no'] = self.import_proof_no.to_alipay_dict()
            else:
                params['import_proof_no'] = self.import_proof_no
        if self.inspection_no:
            if hasattr(self.inspection_no, 'to_alipay_dict'):
                params['inspection_no'] = self.inspection_no.to_alipay_dict()
            else:
                params['inspection_no'] = self.inspection_no
        if self.machine_no:
            if hasattr(self.machine_no, 'to_alipay_dict'):
                params['machine_no'] = self.machine_no.to_alipay_dict()
            else:
                params['machine_no'] = self.machine_no
        if self.origin_place:
            if hasattr(self.origin_place, 'to_alipay_dict'):
                params['origin_place'] = self.origin_place.to_alipay_dict()
            else:
                params['origin_place'] = self.origin_place
        if self.passenger_capacity:
            if hasattr(self.passenger_capacity, 'to_alipay_dict'):
                params['passenger_capacity'] = self.passenger_capacity.to_alipay_dict()
            else:
                params['passenger_capacity'] = self.passenger_capacity
        if self.payment_voucher_no:
            if hasattr(self.payment_voucher_no, 'to_alipay_dict'):
                params['payment_voucher_no'] = self.payment_voucher_no.to_alipay_dict()
            else:
                params['payment_voucher_no'] = self.payment_voucher_no
        if self.seller_account:
            if hasattr(self.seller_account, 'to_alipay_dict'):
                params['seller_account'] = self.seller_account.to_alipay_dict()
            else:
                params['seller_account'] = self.seller_account
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank:
            if hasattr(self.seller_bank, 'to_alipay_dict'):
                params['seller_bank'] = self.seller_bank.to_alipay_dict()
            else:
                params['seller_bank'] = self.seller_bank
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_tel:
            if hasattr(self.seller_tel, 'to_alipay_dict'):
                params['seller_tel'] = self.seller_tel.to_alipay_dict()
            else:
                params['seller_tel'] = self.seller_tel
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_authority:
            if hasattr(self.tax_authority, 'to_alipay_dict'):
                params['tax_authority'] = self.tax_authority.to_alipay_dict()
            else:
                params['tax_authority'] = self.tax_authority
        if self.tax_authority_code:
            if hasattr(self.tax_authority_code, 'to_alipay_dict'):
                params['tax_authority_code'] = self.tax_authority_code.to_alipay_dict()
            else:
                params['tax_authority_code'] = self.tax_authority_code
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tonnage:
            if hasattr(self.tonnage, 'to_alipay_dict'):
                params['tonnage'] = self.tonnage.to_alipay_dict()
            else:
                params['tonnage'] = self.tonnage
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.vehicle_identification_no:
            if hasattr(self.vehicle_identification_no, 'to_alipay_dict'):
                params['vehicle_identification_no'] = self.vehicle_identification_no.to_alipay_dict()
            else:
                params['vehicle_identification_no'] = self.vehicle_identification_no
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.verify_time:
            if hasattr(self.verify_time, 'to_alipay_dict'):
                params['verify_time'] = self.verify_time.to_alipay_dict()
            else:
                params['verify_time'] = self.verify_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MotorVehicleSales()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_org_code' in d:
            o.buyer_org_code = d['buyer_org_code']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'factory_model' in d:
            o.factory_model = d['factory_model']
        if 'import_proof_no' in d:
            o.import_proof_no = d['import_proof_no']
        if 'inspection_no' in d:
            o.inspection_no = d['inspection_no']
        if 'machine_no' in d:
            o.machine_no = d['machine_no']
        if 'origin_place' in d:
            o.origin_place = d['origin_place']
        if 'passenger_capacity' in d:
            o.passenger_capacity = d['passenger_capacity']
        if 'payment_voucher_no' in d:
            o.payment_voucher_no = d['payment_voucher_no']
        if 'seller_account' in d:
            o.seller_account = d['seller_account']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank' in d:
            o.seller_bank = d['seller_bank']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_tel' in d:
            o.seller_tel = d['seller_tel']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_authority' in d:
            o.tax_authority = d['tax_authority']
        if 'tax_authority_code' in d:
            o.tax_authority_code = d['tax_authority_code']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tonnage' in d:
            o.tonnage = d['tonnage']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'vehicle_identification_no' in d:
            o.vehicle_identification_no = d['vehicle_identification_no']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'verify_time' in d:
            o.verify_time = d['verify_time']
        return o


