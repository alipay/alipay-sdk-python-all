#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItem import InvoiceItem


class AlipayEbppInvoiceApplyInvUploadModel(object):

    def __init__(self):
        self._anti_fake_code = None
        self._apply_id = None
        self._biz_error_code = None
        self._biz_error_msg = None
        self._business_type = None
        self._check_code = None
        self._create_result = None
        self._device_no = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_file_content = None
        self._invoice_file_type = None
        self._invoice_items = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_no = None
        self._invoice_type = None
        self._levy_type = None
        self._normal_invoice_code = None
        self._normal_invoice_no = None
        self._payee_address = None
        self._payee_bank_account_id = None
        self._payee_bank_name = None
        self._payee_checker = None
        self._payee_name = None
        self._payee_operator = None
        self._payee_phone = None
        self._payee_receiver = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_account_id = None
        self._payer_bank_name = None
        self._payer_email = None
        self._payer_name = None
        self._payer_phone = None
        self._payer_register_no = None
        self._platform_code = None
        self._platform_tid = None
        self._platform_user_id = None
        self._qr_code = None
        self._receive_mobile = None
        self._red_notice_no = None
        self._serial_no = None
        self._source = None
        self._special_flag = None
        self._sum_price = None
        self._sum_tax = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_msg(self):
        return self._biz_error_msg

    @biz_error_msg.setter
    def biz_error_msg(self, value):
        self._biz_error_msg = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def create_result(self):
        return self._create_result

    @create_result.setter
    def create_result(self, value):
        self._create_result = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
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
    def invoice_file_content(self):
        return self._invoice_file_content

    @invoice_file_content.setter
    def invoice_file_content(self, value):
        self._invoice_file_content = value
    @property
    def invoice_file_type(self):
        return self._invoice_file_type

    @invoice_file_type.setter
    def invoice_file_type(self, value):
        self._invoice_file_type = value
    @property
    def invoice_items(self):
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, value):
        if isinstance(value, InvoiceItem):
            self._invoice_items = value
        else:
            self._invoice_items = InvoiceItem.from_alipay_dict(value)
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_memo(self):
        return self._invoice_memo

    @invoice_memo.setter
    def invoice_memo(self, value):
        self._invoice_memo = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def levy_type(self):
        return self._levy_type

    @levy_type.setter
    def levy_type(self, value):
        self._levy_type = value
    @property
    def normal_invoice_code(self):
        return self._normal_invoice_code

    @normal_invoice_code.setter
    def normal_invoice_code(self, value):
        self._normal_invoice_code = value
    @property
    def normal_invoice_no(self):
        return self._normal_invoice_no

    @normal_invoice_no.setter
    def normal_invoice_no(self, value):
        self._normal_invoice_no = value
    @property
    def payee_address(self):
        return self._payee_address

    @payee_address.setter
    def payee_address(self, value):
        self._payee_address = value
    @property
    def payee_bank_account_id(self):
        return self._payee_bank_account_id

    @payee_bank_account_id.setter
    def payee_bank_account_id(self, value):
        self._payee_bank_account_id = value
    @property
    def payee_bank_name(self):
        return self._payee_bank_name

    @payee_bank_name.setter
    def payee_bank_name(self, value):
        self._payee_bank_name = value
    @property
    def payee_checker(self):
        return self._payee_checker

    @payee_checker.setter
    def payee_checker(self, value):
        self._payee_checker = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_operator(self):
        return self._payee_operator

    @payee_operator.setter
    def payee_operator(self, value):
        self._payee_operator = value
    @property
    def payee_phone(self):
        return self._payee_phone

    @payee_phone.setter
    def payee_phone(self, value):
        self._payee_phone = value
    @property
    def payee_receiver(self):
        return self._payee_receiver

    @payee_receiver.setter
    def payee_receiver(self, value):
        self._payee_receiver = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
    @property
    def payer_address(self):
        return self._payer_address

    @payer_address.setter
    def payer_address(self, value):
        self._payer_address = value
    @property
    def payer_bank_account_id(self):
        return self._payer_bank_account_id

    @payer_bank_account_id.setter
    def payer_bank_account_id(self, value):
        self._payer_bank_account_id = value
    @property
    def payer_bank_name(self):
        return self._payer_bank_name

    @payer_bank_name.setter
    def payer_bank_name(self, value):
        self._payer_bank_name = value
    @property
    def payer_email(self):
        return self._payer_email

    @payer_email.setter
    def payer_email(self, value):
        self._payer_email = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_phone(self):
        return self._payer_phone

    @payer_phone.setter
    def payer_phone(self, value):
        self._payer_phone = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def platform_tid(self):
        return self._platform_tid

    @platform_tid.setter
    def platform_tid(self, value):
        self._platform_tid = value
    @property
    def platform_user_id(self):
        return self._platform_user_id

    @platform_user_id.setter
    def platform_user_id(self, value):
        self._platform_user_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def receive_mobile(self):
        return self._receive_mobile

    @receive_mobile.setter
    def receive_mobile(self, value):
        self._receive_mobile = value
    @property
    def red_notice_no(self):
        return self._red_notice_no

    @red_notice_no.setter
    def red_notice_no(self, value):
        self._red_notice_no = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def special_flag(self):
        return self._special_flag

    @special_flag.setter
    def special_flag(self, value):
        self._special_flag = value
    @property
    def sum_price(self):
        return self._sum_price

    @sum_price.setter
    def sum_price(self, value):
        self._sum_price = value
    @property
    def sum_tax(self):
        return self._sum_tax

    @sum_tax.setter
    def sum_tax(self, value):
        self._sum_tax = value


    def to_alipay_dict(self):
        params = dict()
        if self.anti_fake_code:
            if hasattr(self.anti_fake_code, 'to_alipay_dict'):
                params['anti_fake_code'] = self.anti_fake_code.to_alipay_dict()
            else:
                params['anti_fake_code'] = self.anti_fake_code
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.biz_error_code:
            if hasattr(self.biz_error_code, 'to_alipay_dict'):
                params['biz_error_code'] = self.biz_error_code.to_alipay_dict()
            else:
                params['biz_error_code'] = self.biz_error_code
        if self.biz_error_msg:
            if hasattr(self.biz_error_msg, 'to_alipay_dict'):
                params['biz_error_msg'] = self.biz_error_msg.to_alipay_dict()
            else:
                params['biz_error_msg'] = self.biz_error_msg
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.create_result:
            if hasattr(self.create_result, 'to_alipay_dict'):
                params['create_result'] = self.create_result.to_alipay_dict()
            else:
                params['create_result'] = self.create_result
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
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
        if self.invoice_file_content:
            if hasattr(self.invoice_file_content, 'to_alipay_dict'):
                params['invoice_file_content'] = self.invoice_file_content.to_alipay_dict()
            else:
                params['invoice_file_content'] = self.invoice_file_content
        if self.invoice_file_type:
            if hasattr(self.invoice_file_type, 'to_alipay_dict'):
                params['invoice_file_type'] = self.invoice_file_type.to_alipay_dict()
            else:
                params['invoice_file_type'] = self.invoice_file_type
        if self.invoice_items:
            if hasattr(self.invoice_items, 'to_alipay_dict'):
                params['invoice_items'] = self.invoice_items.to_alipay_dict()
            else:
                params['invoice_items'] = self.invoice_items
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.invoice_memo:
            if hasattr(self.invoice_memo, 'to_alipay_dict'):
                params['invoice_memo'] = self.invoice_memo.to_alipay_dict()
            else:
                params['invoice_memo'] = self.invoice_memo
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.levy_type:
            if hasattr(self.levy_type, 'to_alipay_dict'):
                params['levy_type'] = self.levy_type.to_alipay_dict()
            else:
                params['levy_type'] = self.levy_type
        if self.normal_invoice_code:
            if hasattr(self.normal_invoice_code, 'to_alipay_dict'):
                params['normal_invoice_code'] = self.normal_invoice_code.to_alipay_dict()
            else:
                params['normal_invoice_code'] = self.normal_invoice_code
        if self.normal_invoice_no:
            if hasattr(self.normal_invoice_no, 'to_alipay_dict'):
                params['normal_invoice_no'] = self.normal_invoice_no.to_alipay_dict()
            else:
                params['normal_invoice_no'] = self.normal_invoice_no
        if self.payee_address:
            if hasattr(self.payee_address, 'to_alipay_dict'):
                params['payee_address'] = self.payee_address.to_alipay_dict()
            else:
                params['payee_address'] = self.payee_address
        if self.payee_bank_account_id:
            if hasattr(self.payee_bank_account_id, 'to_alipay_dict'):
                params['payee_bank_account_id'] = self.payee_bank_account_id.to_alipay_dict()
            else:
                params['payee_bank_account_id'] = self.payee_bank_account_id
        if self.payee_bank_name:
            if hasattr(self.payee_bank_name, 'to_alipay_dict'):
                params['payee_bank_name'] = self.payee_bank_name.to_alipay_dict()
            else:
                params['payee_bank_name'] = self.payee_bank_name
        if self.payee_checker:
            if hasattr(self.payee_checker, 'to_alipay_dict'):
                params['payee_checker'] = self.payee_checker.to_alipay_dict()
            else:
                params['payee_checker'] = self.payee_checker
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_operator:
            if hasattr(self.payee_operator, 'to_alipay_dict'):
                params['payee_operator'] = self.payee_operator.to_alipay_dict()
            else:
                params['payee_operator'] = self.payee_operator
        if self.payee_phone:
            if hasattr(self.payee_phone, 'to_alipay_dict'):
                params['payee_phone'] = self.payee_phone.to_alipay_dict()
            else:
                params['payee_phone'] = self.payee_phone
        if self.payee_receiver:
            if hasattr(self.payee_receiver, 'to_alipay_dict'):
                params['payee_receiver'] = self.payee_receiver.to_alipay_dict()
            else:
                params['payee_receiver'] = self.payee_receiver
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.payer_address:
            if hasattr(self.payer_address, 'to_alipay_dict'):
                params['payer_address'] = self.payer_address.to_alipay_dict()
            else:
                params['payer_address'] = self.payer_address
        if self.payer_bank_account_id:
            if hasattr(self.payer_bank_account_id, 'to_alipay_dict'):
                params['payer_bank_account_id'] = self.payer_bank_account_id.to_alipay_dict()
            else:
                params['payer_bank_account_id'] = self.payer_bank_account_id
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_email:
            if hasattr(self.payer_email, 'to_alipay_dict'):
                params['payer_email'] = self.payer_email.to_alipay_dict()
            else:
                params['payer_email'] = self.payer_email
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_phone:
            if hasattr(self.payer_phone, 'to_alipay_dict'):
                params['payer_phone'] = self.payer_phone.to_alipay_dict()
            else:
                params['payer_phone'] = self.payer_phone
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.platform_tid:
            if hasattr(self.platform_tid, 'to_alipay_dict'):
                params['platform_tid'] = self.platform_tid.to_alipay_dict()
            else:
                params['platform_tid'] = self.platform_tid
        if self.platform_user_id:
            if hasattr(self.platform_user_id, 'to_alipay_dict'):
                params['platform_user_id'] = self.platform_user_id.to_alipay_dict()
            else:
                params['platform_user_id'] = self.platform_user_id
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.receive_mobile:
            if hasattr(self.receive_mobile, 'to_alipay_dict'):
                params['receive_mobile'] = self.receive_mobile.to_alipay_dict()
            else:
                params['receive_mobile'] = self.receive_mobile
        if self.red_notice_no:
            if hasattr(self.red_notice_no, 'to_alipay_dict'):
                params['red_notice_no'] = self.red_notice_no.to_alipay_dict()
            else:
                params['red_notice_no'] = self.red_notice_no
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.special_flag:
            if hasattr(self.special_flag, 'to_alipay_dict'):
                params['special_flag'] = self.special_flag.to_alipay_dict()
            else:
                params['special_flag'] = self.special_flag
        if self.sum_price:
            if hasattr(self.sum_price, 'to_alipay_dict'):
                params['sum_price'] = self.sum_price.to_alipay_dict()
            else:
                params['sum_price'] = self.sum_price
        if self.sum_tax:
            if hasattr(self.sum_tax, 'to_alipay_dict'):
                params['sum_tax'] = self.sum_tax.to_alipay_dict()
            else:
                params['sum_tax'] = self.sum_tax
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceApplyInvUploadModel()
        if 'anti_fake_code' in d:
            o.anti_fake_code = d['anti_fake_code']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'biz_error_code' in d:
            o.biz_error_code = d['biz_error_code']
        if 'biz_error_msg' in d:
            o.biz_error_msg = d['biz_error_msg']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'create_result' in d:
            o.create_result = d['create_result']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_file_content' in d:
            o.invoice_file_content = d['invoice_file_content']
        if 'invoice_file_type' in d:
            o.invoice_file_type = d['invoice_file_type']
        if 'invoice_items' in d:
            o.invoice_items = d['invoice_items']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'levy_type' in d:
            o.levy_type = d['levy_type']
        if 'normal_invoice_code' in d:
            o.normal_invoice_code = d['normal_invoice_code']
        if 'normal_invoice_no' in d:
            o.normal_invoice_no = d['normal_invoice_no']
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_account_id' in d:
            o.payee_bank_account_id = d['payee_bank_account_id']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_checker' in d:
            o.payee_checker = d['payee_checker']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_operator' in d:
            o.payee_operator = d['payee_operator']
        if 'payee_phone' in d:
            o.payee_phone = d['payee_phone']
        if 'payee_receiver' in d:
            o.payee_receiver = d['payee_receiver']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_account_id' in d:
            o.payer_bank_account_id = d['payer_bank_account_id']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_email' in d:
            o.payer_email = d['payer_email']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_phone' in d:
            o.payer_phone = d['payer_phone']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_tid' in d:
            o.platform_tid = d['platform_tid']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'receive_mobile' in d:
            o.receive_mobile = d['receive_mobile']
        if 'red_notice_no' in d:
            o.red_notice_no = d['red_notice_no']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'source' in d:
            o.source = d['source']
        if 'special_flag' in d:
            o.special_flag = d['special_flag']
        if 'sum_price' in d:
            o.sum_price = d['sum_price']
        if 'sum_tax' in d:
            o.sum_tax = d['sum_tax']
        return o


