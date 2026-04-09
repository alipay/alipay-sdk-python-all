#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SecondVehicleSales(object):

    def __init__(self):
        self._auction_address = None
        self._auction_bank_account = None
        self._auction_company = None
        self._auction_phone = None
        self._auction_tax_no = None
        self._buyer_address = None
        self._buyer_phone = None
        self._buyer_unit = None
        self._buyer_unit_code = None
        self._chassis_no = None
        self._factory_model = None
        self._license_plate_no = None
        self._machine_no = None
        self._market_address = None
        self._market_bank_account = None
        self._market_phone = None
        self._market_tax_no = None
        self._oil_flag = None
        self._registration_cert_no = None
        self._second_hand_market = None
        self._seller_address = None
        self._seller_phone = None
        self._seller_unit = None
        self._seller_unit_code = None
        self._toll_flag = None
        self._transfer_location = None
        self._vehicle_total_price = None
        self._vehicle_type = None
        self._verify_time = None
        self._zero_rate_flag = None

    @property
    def auction_address(self):
        return self._auction_address

    @auction_address.setter
    def auction_address(self, value):
        self._auction_address = value
    @property
    def auction_bank_account(self):
        return self._auction_bank_account

    @auction_bank_account.setter
    def auction_bank_account(self, value):
        self._auction_bank_account = value
    @property
    def auction_company(self):
        return self._auction_company

    @auction_company.setter
    def auction_company(self, value):
        self._auction_company = value
    @property
    def auction_phone(self):
        return self._auction_phone

    @auction_phone.setter
    def auction_phone(self, value):
        self._auction_phone = value
    @property
    def auction_tax_no(self):
        return self._auction_tax_no

    @auction_tax_no.setter
    def auction_tax_no(self, value):
        self._auction_tax_no = value
    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_phone(self):
        return self._buyer_phone

    @buyer_phone.setter
    def buyer_phone(self, value):
        self._buyer_phone = value
    @property
    def buyer_unit(self):
        return self._buyer_unit

    @buyer_unit.setter
    def buyer_unit(self, value):
        self._buyer_unit = value
    @property
    def buyer_unit_code(self):
        return self._buyer_unit_code

    @buyer_unit_code.setter
    def buyer_unit_code(self, value):
        self._buyer_unit_code = value
    @property
    def chassis_no(self):
        return self._chassis_no

    @chassis_no.setter
    def chassis_no(self, value):
        self._chassis_no = value
    @property
    def factory_model(self):
        return self._factory_model

    @factory_model.setter
    def factory_model(self, value):
        self._factory_model = value
    @property
    def license_plate_no(self):
        return self._license_plate_no

    @license_plate_no.setter
    def license_plate_no(self, value):
        self._license_plate_no = value
    @property
    def machine_no(self):
        return self._machine_no

    @machine_no.setter
    def machine_no(self, value):
        self._machine_no = value
    @property
    def market_address(self):
        return self._market_address

    @market_address.setter
    def market_address(self, value):
        self._market_address = value
    @property
    def market_bank_account(self):
        return self._market_bank_account

    @market_bank_account.setter
    def market_bank_account(self, value):
        self._market_bank_account = value
    @property
    def market_phone(self):
        return self._market_phone

    @market_phone.setter
    def market_phone(self, value):
        self._market_phone = value
    @property
    def market_tax_no(self):
        return self._market_tax_no

    @market_tax_no.setter
    def market_tax_no(self, value):
        self._market_tax_no = value
    @property
    def oil_flag(self):
        return self._oil_flag

    @oil_flag.setter
    def oil_flag(self, value):
        self._oil_flag = value
    @property
    def registration_cert_no(self):
        return self._registration_cert_no

    @registration_cert_no.setter
    def registration_cert_no(self, value):
        self._registration_cert_no = value
    @property
    def second_hand_market(self):
        return self._second_hand_market

    @second_hand_market.setter
    def second_hand_market(self, value):
        self._second_hand_market = value
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_phone(self):
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, value):
        self._seller_phone = value
    @property
    def seller_unit(self):
        return self._seller_unit

    @seller_unit.setter
    def seller_unit(self, value):
        self._seller_unit = value
    @property
    def seller_unit_code(self):
        return self._seller_unit_code

    @seller_unit_code.setter
    def seller_unit_code(self, value):
        self._seller_unit_code = value
    @property
    def toll_flag(self):
        return self._toll_flag

    @toll_flag.setter
    def toll_flag(self, value):
        self._toll_flag = value
    @property
    def transfer_location(self):
        return self._transfer_location

    @transfer_location.setter
    def transfer_location(self, value):
        self._transfer_location = value
    @property
    def vehicle_total_price(self):
        return self._vehicle_total_price

    @vehicle_total_price.setter
    def vehicle_total_price(self, value):
        self._vehicle_total_price = value
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
    @property
    def zero_rate_flag(self):
        return self._zero_rate_flag

    @zero_rate_flag.setter
    def zero_rate_flag(self, value):
        self._zero_rate_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.auction_address:
            if hasattr(self.auction_address, 'to_alipay_dict'):
                params['auction_address'] = self.auction_address.to_alipay_dict()
            else:
                params['auction_address'] = self.auction_address
        if self.auction_bank_account:
            if hasattr(self.auction_bank_account, 'to_alipay_dict'):
                params['auction_bank_account'] = self.auction_bank_account.to_alipay_dict()
            else:
                params['auction_bank_account'] = self.auction_bank_account
        if self.auction_company:
            if hasattr(self.auction_company, 'to_alipay_dict'):
                params['auction_company'] = self.auction_company.to_alipay_dict()
            else:
                params['auction_company'] = self.auction_company
        if self.auction_phone:
            if hasattr(self.auction_phone, 'to_alipay_dict'):
                params['auction_phone'] = self.auction_phone.to_alipay_dict()
            else:
                params['auction_phone'] = self.auction_phone
        if self.auction_tax_no:
            if hasattr(self.auction_tax_no, 'to_alipay_dict'):
                params['auction_tax_no'] = self.auction_tax_no.to_alipay_dict()
            else:
                params['auction_tax_no'] = self.auction_tax_no
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_phone:
            if hasattr(self.buyer_phone, 'to_alipay_dict'):
                params['buyer_phone'] = self.buyer_phone.to_alipay_dict()
            else:
                params['buyer_phone'] = self.buyer_phone
        if self.buyer_unit:
            if hasattr(self.buyer_unit, 'to_alipay_dict'):
                params['buyer_unit'] = self.buyer_unit.to_alipay_dict()
            else:
                params['buyer_unit'] = self.buyer_unit
        if self.buyer_unit_code:
            if hasattr(self.buyer_unit_code, 'to_alipay_dict'):
                params['buyer_unit_code'] = self.buyer_unit_code.to_alipay_dict()
            else:
                params['buyer_unit_code'] = self.buyer_unit_code
        if self.chassis_no:
            if hasattr(self.chassis_no, 'to_alipay_dict'):
                params['chassis_no'] = self.chassis_no.to_alipay_dict()
            else:
                params['chassis_no'] = self.chassis_no
        if self.factory_model:
            if hasattr(self.factory_model, 'to_alipay_dict'):
                params['factory_model'] = self.factory_model.to_alipay_dict()
            else:
                params['factory_model'] = self.factory_model
        if self.license_plate_no:
            if hasattr(self.license_plate_no, 'to_alipay_dict'):
                params['license_plate_no'] = self.license_plate_no.to_alipay_dict()
            else:
                params['license_plate_no'] = self.license_plate_no
        if self.machine_no:
            if hasattr(self.machine_no, 'to_alipay_dict'):
                params['machine_no'] = self.machine_no.to_alipay_dict()
            else:
                params['machine_no'] = self.machine_no
        if self.market_address:
            if hasattr(self.market_address, 'to_alipay_dict'):
                params['market_address'] = self.market_address.to_alipay_dict()
            else:
                params['market_address'] = self.market_address
        if self.market_bank_account:
            if hasattr(self.market_bank_account, 'to_alipay_dict'):
                params['market_bank_account'] = self.market_bank_account.to_alipay_dict()
            else:
                params['market_bank_account'] = self.market_bank_account
        if self.market_phone:
            if hasattr(self.market_phone, 'to_alipay_dict'):
                params['market_phone'] = self.market_phone.to_alipay_dict()
            else:
                params['market_phone'] = self.market_phone
        if self.market_tax_no:
            if hasattr(self.market_tax_no, 'to_alipay_dict'):
                params['market_tax_no'] = self.market_tax_no.to_alipay_dict()
            else:
                params['market_tax_no'] = self.market_tax_no
        if self.oil_flag:
            if hasattr(self.oil_flag, 'to_alipay_dict'):
                params['oil_flag'] = self.oil_flag.to_alipay_dict()
            else:
                params['oil_flag'] = self.oil_flag
        if self.registration_cert_no:
            if hasattr(self.registration_cert_no, 'to_alipay_dict'):
                params['registration_cert_no'] = self.registration_cert_no.to_alipay_dict()
            else:
                params['registration_cert_no'] = self.registration_cert_no
        if self.second_hand_market:
            if hasattr(self.second_hand_market, 'to_alipay_dict'):
                params['second_hand_market'] = self.second_hand_market.to_alipay_dict()
            else:
                params['second_hand_market'] = self.second_hand_market
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_phone:
            if hasattr(self.seller_phone, 'to_alipay_dict'):
                params['seller_phone'] = self.seller_phone.to_alipay_dict()
            else:
                params['seller_phone'] = self.seller_phone
        if self.seller_unit:
            if hasattr(self.seller_unit, 'to_alipay_dict'):
                params['seller_unit'] = self.seller_unit.to_alipay_dict()
            else:
                params['seller_unit'] = self.seller_unit
        if self.seller_unit_code:
            if hasattr(self.seller_unit_code, 'to_alipay_dict'):
                params['seller_unit_code'] = self.seller_unit_code.to_alipay_dict()
            else:
                params['seller_unit_code'] = self.seller_unit_code
        if self.toll_flag:
            if hasattr(self.toll_flag, 'to_alipay_dict'):
                params['toll_flag'] = self.toll_flag.to_alipay_dict()
            else:
                params['toll_flag'] = self.toll_flag
        if self.transfer_location:
            if hasattr(self.transfer_location, 'to_alipay_dict'):
                params['transfer_location'] = self.transfer_location.to_alipay_dict()
            else:
                params['transfer_location'] = self.transfer_location
        if self.vehicle_total_price:
            if hasattr(self.vehicle_total_price, 'to_alipay_dict'):
                params['vehicle_total_price'] = self.vehicle_total_price.to_alipay_dict()
            else:
                params['vehicle_total_price'] = self.vehicle_total_price
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
        if self.zero_rate_flag:
            if hasattr(self.zero_rate_flag, 'to_alipay_dict'):
                params['zero_rate_flag'] = self.zero_rate_flag.to_alipay_dict()
            else:
                params['zero_rate_flag'] = self.zero_rate_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecondVehicleSales()
        if 'auction_address' in d:
            o.auction_address = d['auction_address']
        if 'auction_bank_account' in d:
            o.auction_bank_account = d['auction_bank_account']
        if 'auction_company' in d:
            o.auction_company = d['auction_company']
        if 'auction_phone' in d:
            o.auction_phone = d['auction_phone']
        if 'auction_tax_no' in d:
            o.auction_tax_no = d['auction_tax_no']
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_phone' in d:
            o.buyer_phone = d['buyer_phone']
        if 'buyer_unit' in d:
            o.buyer_unit = d['buyer_unit']
        if 'buyer_unit_code' in d:
            o.buyer_unit_code = d['buyer_unit_code']
        if 'chassis_no' in d:
            o.chassis_no = d['chassis_no']
        if 'factory_model' in d:
            o.factory_model = d['factory_model']
        if 'license_plate_no' in d:
            o.license_plate_no = d['license_plate_no']
        if 'machine_no' in d:
            o.machine_no = d['machine_no']
        if 'market_address' in d:
            o.market_address = d['market_address']
        if 'market_bank_account' in d:
            o.market_bank_account = d['market_bank_account']
        if 'market_phone' in d:
            o.market_phone = d['market_phone']
        if 'market_tax_no' in d:
            o.market_tax_no = d['market_tax_no']
        if 'oil_flag' in d:
            o.oil_flag = d['oil_flag']
        if 'registration_cert_no' in d:
            o.registration_cert_no = d['registration_cert_no']
        if 'second_hand_market' in d:
            o.second_hand_market = d['second_hand_market']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_phone' in d:
            o.seller_phone = d['seller_phone']
        if 'seller_unit' in d:
            o.seller_unit = d['seller_unit']
        if 'seller_unit_code' in d:
            o.seller_unit_code = d['seller_unit_code']
        if 'toll_flag' in d:
            o.toll_flag = d['toll_flag']
        if 'transfer_location' in d:
            o.transfer_location = d['transfer_location']
        if 'vehicle_total_price' in d:
            o.vehicle_total_price = d['vehicle_total_price']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'verify_time' in d:
            o.verify_time = d['verify_time']
        if 'zero_rate_flag' in d:
            o.zero_rate_flag = d['zero_rate_flag']
        return o


