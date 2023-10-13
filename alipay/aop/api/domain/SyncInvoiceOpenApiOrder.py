#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceReimburseInfoOpenApiOrder import InvoiceReimburseInfoOpenApiOrder
from alipay.aop.api.domain.SyncInvoiceLineOpenApiOrder import SyncInvoiceLineOpenApiOrder


class SyncInvoiceOpenApiOrder(object):

    def __init__(self):
        self._boarding_time = None
        self._buyer_address_tel = None
        self._buyer_bank_info = None
        self._buyer_company_name = None
        self._buyer_ou_code = None
        self._buyer_tax_no = None
        self._certify_state = None
        self._check_code = None
        self._check_state = None
        self._city = None
        self._currency = None
        self._drive_date = None
        self._end_station = None
        self._file_name = None
        self._file_url = None
        self._fuel_surcharge = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_note = None
        self._invoice_reimburse_info_order_list = None
        self._invoice_type = None
        self._off_time = None
        self._platform_code = None
        self._reimburse_state = None
        self._seat = None
        self._seller_address_tel = None
        self._seller_bank_info = None
        self._seller_company_name = None
        self._seller_tax_no = None
        self._start_station = None
        self._sync_invoice_line_order_list = None
        self._tax_amt = None
        self._tax_exclusive_amt = None

    @property
    def boarding_time(self):
        return self._boarding_time

    @boarding_time.setter
    def boarding_time(self, value):
        self._boarding_time = value
    @property
    def buyer_address_tel(self):
        return self._buyer_address_tel

    @buyer_address_tel.setter
    def buyer_address_tel(self, value):
        self._buyer_address_tel = value
    @property
    def buyer_bank_info(self):
        return self._buyer_bank_info

    @buyer_bank_info.setter
    def buyer_bank_info(self, value):
        self._buyer_bank_info = value
    @property
    def buyer_company_name(self):
        return self._buyer_company_name

    @buyer_company_name.setter
    def buyer_company_name(self, value):
        self._buyer_company_name = value
    @property
    def buyer_ou_code(self):
        return self._buyer_ou_code

    @buyer_ou_code.setter
    def buyer_ou_code(self, value):
        self._buyer_ou_code = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def certify_state(self):
        return self._certify_state

    @certify_state.setter
    def certify_state(self, value):
        self._certify_state = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_state(self):
        return self._check_state

    @check_state.setter
    def check_state(self, value):
        self._check_state = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def drive_date(self):
        return self._drive_date

    @drive_date.setter
    def drive_date(self, value):
        self._drive_date = value
    @property
    def end_station(self):
        return self._end_station

    @end_station.setter
    def end_station(self, value):
        self._end_station = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def fuel_surcharge(self):
        return self._fuel_surcharge

    @fuel_surcharge.setter
    def fuel_surcharge(self, value):
        self._fuel_surcharge = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        self._invoice_amt = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_reimburse_info_order_list(self):
        return self._invoice_reimburse_info_order_list

    @invoice_reimburse_info_order_list.setter
    def invoice_reimburse_info_order_list(self, value):
        if isinstance(value, list):
            self._invoice_reimburse_info_order_list = list()
            for i in value:
                if isinstance(i, InvoiceReimburseInfoOpenApiOrder):
                    self._invoice_reimburse_info_order_list.append(i)
                else:
                    self._invoice_reimburse_info_order_list.append(InvoiceReimburseInfoOpenApiOrder.from_alipay_dict(i))
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def off_time(self):
        return self._off_time

    @off_time.setter
    def off_time(self, value):
        self._off_time = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def reimburse_state(self):
        return self._reimburse_state

    @reimburse_state.setter
    def reimburse_state(self, value):
        self._reimburse_state = value
    @property
    def seat(self):
        return self._seat

    @seat.setter
    def seat(self, value):
        self._seat = value
    @property
    def seller_address_tel(self):
        return self._seller_address_tel

    @seller_address_tel.setter
    def seller_address_tel(self, value):
        self._seller_address_tel = value
    @property
    def seller_bank_info(self):
        return self._seller_bank_info

    @seller_bank_info.setter
    def seller_bank_info(self, value):
        self._seller_bank_info = value
    @property
    def seller_company_name(self):
        return self._seller_company_name

    @seller_company_name.setter
    def seller_company_name(self, value):
        self._seller_company_name = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def start_station(self):
        return self._start_station

    @start_station.setter
    def start_station(self, value):
        self._start_station = value
    @property
    def sync_invoice_line_order_list(self):
        return self._sync_invoice_line_order_list

    @sync_invoice_line_order_list.setter
    def sync_invoice_line_order_list(self, value):
        if isinstance(value, list):
            self._sync_invoice_line_order_list = list()
            for i in value:
                if isinstance(i, SyncInvoiceLineOpenApiOrder):
                    self._sync_invoice_line_order_list.append(i)
                else:
                    self._sync_invoice_line_order_list.append(SyncInvoiceLineOpenApiOrder.from_alipay_dict(i))
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        self._tax_amt = value
    @property
    def tax_exclusive_amt(self):
        return self._tax_exclusive_amt

    @tax_exclusive_amt.setter
    def tax_exclusive_amt(self, value):
        self._tax_exclusive_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.boarding_time:
            if hasattr(self.boarding_time, 'to_alipay_dict'):
                params['boarding_time'] = self.boarding_time.to_alipay_dict()
            else:
                params['boarding_time'] = self.boarding_time
        if self.buyer_address_tel:
            if hasattr(self.buyer_address_tel, 'to_alipay_dict'):
                params['buyer_address_tel'] = self.buyer_address_tel.to_alipay_dict()
            else:
                params['buyer_address_tel'] = self.buyer_address_tel
        if self.buyer_bank_info:
            if hasattr(self.buyer_bank_info, 'to_alipay_dict'):
                params['buyer_bank_info'] = self.buyer_bank_info.to_alipay_dict()
            else:
                params['buyer_bank_info'] = self.buyer_bank_info
        if self.buyer_company_name:
            if hasattr(self.buyer_company_name, 'to_alipay_dict'):
                params['buyer_company_name'] = self.buyer_company_name.to_alipay_dict()
            else:
                params['buyer_company_name'] = self.buyer_company_name
        if self.buyer_ou_code:
            if hasattr(self.buyer_ou_code, 'to_alipay_dict'):
                params['buyer_ou_code'] = self.buyer_ou_code.to_alipay_dict()
            else:
                params['buyer_ou_code'] = self.buyer_ou_code
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.certify_state:
            if hasattr(self.certify_state, 'to_alipay_dict'):
                params['certify_state'] = self.certify_state.to_alipay_dict()
            else:
                params['certify_state'] = self.certify_state
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.check_state:
            if hasattr(self.check_state, 'to_alipay_dict'):
                params['check_state'] = self.check_state.to_alipay_dict()
            else:
                params['check_state'] = self.check_state
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.drive_date:
            if hasattr(self.drive_date, 'to_alipay_dict'):
                params['drive_date'] = self.drive_date.to_alipay_dict()
            else:
                params['drive_date'] = self.drive_date
        if self.end_station:
            if hasattr(self.end_station, 'to_alipay_dict'):
                params['end_station'] = self.end_station.to_alipay_dict()
            else:
                params['end_station'] = self.end_station
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.fuel_surcharge:
            if hasattr(self.fuel_surcharge, 'to_alipay_dict'):
                params['fuel_surcharge'] = self.fuel_surcharge.to_alipay_dict()
            else:
                params['fuel_surcharge'] = self.fuel_surcharge
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_reimburse_info_order_list:
            if isinstance(self.invoice_reimburse_info_order_list, list):
                for i in range(0, len(self.invoice_reimburse_info_order_list)):
                    element = self.invoice_reimburse_info_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_reimburse_info_order_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_reimburse_info_order_list, 'to_alipay_dict'):
                params['invoice_reimburse_info_order_list'] = self.invoice_reimburse_info_order_list.to_alipay_dict()
            else:
                params['invoice_reimburse_info_order_list'] = self.invoice_reimburse_info_order_list
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.off_time:
            if hasattr(self.off_time, 'to_alipay_dict'):
                params['off_time'] = self.off_time.to_alipay_dict()
            else:
                params['off_time'] = self.off_time
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.reimburse_state:
            if hasattr(self.reimburse_state, 'to_alipay_dict'):
                params['reimburse_state'] = self.reimburse_state.to_alipay_dict()
            else:
                params['reimburse_state'] = self.reimburse_state
        if self.seat:
            if hasattr(self.seat, 'to_alipay_dict'):
                params['seat'] = self.seat.to_alipay_dict()
            else:
                params['seat'] = self.seat
        if self.seller_address_tel:
            if hasattr(self.seller_address_tel, 'to_alipay_dict'):
                params['seller_address_tel'] = self.seller_address_tel.to_alipay_dict()
            else:
                params['seller_address_tel'] = self.seller_address_tel
        if self.seller_bank_info:
            if hasattr(self.seller_bank_info, 'to_alipay_dict'):
                params['seller_bank_info'] = self.seller_bank_info.to_alipay_dict()
            else:
                params['seller_bank_info'] = self.seller_bank_info
        if self.seller_company_name:
            if hasattr(self.seller_company_name, 'to_alipay_dict'):
                params['seller_company_name'] = self.seller_company_name.to_alipay_dict()
            else:
                params['seller_company_name'] = self.seller_company_name
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.start_station:
            if hasattr(self.start_station, 'to_alipay_dict'):
                params['start_station'] = self.start_station.to_alipay_dict()
            else:
                params['start_station'] = self.start_station
        if self.sync_invoice_line_order_list:
            if isinstance(self.sync_invoice_line_order_list, list):
                for i in range(0, len(self.sync_invoice_line_order_list)):
                    element = self.sync_invoice_line_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sync_invoice_line_order_list[i] = element.to_alipay_dict()
            if hasattr(self.sync_invoice_line_order_list, 'to_alipay_dict'):
                params['sync_invoice_line_order_list'] = self.sync_invoice_line_order_list.to_alipay_dict()
            else:
                params['sync_invoice_line_order_list'] = self.sync_invoice_line_order_list
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_exclusive_amt:
            if hasattr(self.tax_exclusive_amt, 'to_alipay_dict'):
                params['tax_exclusive_amt'] = self.tax_exclusive_amt.to_alipay_dict()
            else:
                params['tax_exclusive_amt'] = self.tax_exclusive_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SyncInvoiceOpenApiOrder()
        if 'boarding_time' in d:
            o.boarding_time = d['boarding_time']
        if 'buyer_address_tel' in d:
            o.buyer_address_tel = d['buyer_address_tel']
        if 'buyer_bank_info' in d:
            o.buyer_bank_info = d['buyer_bank_info']
        if 'buyer_company_name' in d:
            o.buyer_company_name = d['buyer_company_name']
        if 'buyer_ou_code' in d:
            o.buyer_ou_code = d['buyer_ou_code']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'certify_state' in d:
            o.certify_state = d['certify_state']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'check_state' in d:
            o.check_state = d['check_state']
        if 'city' in d:
            o.city = d['city']
        if 'currency' in d:
            o.currency = d['currency']
        if 'drive_date' in d:
            o.drive_date = d['drive_date']
        if 'end_station' in d:
            o.end_station = d['end_station']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'fuel_surcharge' in d:
            o.fuel_surcharge = d['fuel_surcharge']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_reimburse_info_order_list' in d:
            o.invoice_reimburse_info_order_list = d['invoice_reimburse_info_order_list']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'off_time' in d:
            o.off_time = d['off_time']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'reimburse_state' in d:
            o.reimburse_state = d['reimburse_state']
        if 'seat' in d:
            o.seat = d['seat']
        if 'seller_address_tel' in d:
            o.seller_address_tel = d['seller_address_tel']
        if 'seller_bank_info' in d:
            o.seller_bank_info = d['seller_bank_info']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'start_station' in d:
            o.start_station = d['start_station']
        if 'sync_invoice_line_order_list' in d:
            o.sync_invoice_line_order_list = d['sync_invoice_line_order_list']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_exclusive_amt' in d:
            o.tax_exclusive_amt = d['tax_exclusive_amt']
        return o


